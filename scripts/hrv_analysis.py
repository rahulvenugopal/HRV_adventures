# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 14:55:51 2021
Explore HRV analysis on data acquired from brain products system
1. Check data quality
2. Do appropriate pre-processing for HRV analyss
3. Deploy Neurokit2 analysis
4. Visualisations

TODO
1. Epoch level analysis
2.Cut out ECG data based on markers (Eyes open, closed etc)
3. Understand and interpret the new parameters

Resources:
    1. Read the paper - https://link.springer.com/article/10.3758%2Fs13428-020-01516-y
    2. Github repo - https://github.com/neuropsychology/NeuroKit
    3. Interval-related Analysis - https://neurokit2.readthedocs.io/en/latest/examples/intervalrelated.html
    4. HRV - https://neurokit2.readthedocs.io/en/latest/examples/hrv.html

@author: Rahul Venugopal
"""
#%% Load libraries
import os
import numpy as np
import mne
from tkinter import filedialog
from glob import glob
import matplotlib.pyplot as plt
import pandas as pd

import neurokit2 as nk
plt.rcParams['figure.figsize'] = [15, 9]  # Bigger images
plt.rcParams['font.size']= 13

#%% Load data

data_dir = filedialog.askdirectory(title='Please select a directory with data files')

os.chdir(data_dir) # Changing directory to data folder

filelist = glob('*.vhdr')

pretask = mne.io.read_raw_brainvision(filelist[0],preload=True)
pretask.info

# select ECG channels
ecg_channels = ['ECG1', 'ECG2']

pretask.pick_channels(ecg_channels)

pretask.filter(0.1,None,fir_design='firwin').load_data()
pretask.filter(None,40,fir_design='firwin').load_data()

pretask_bp = mne.set_bipolar_reference(pretask, anode='ECG1', cathode='ECG2')

# visualise ECG data
pretask_bp.plot()

# finding events in the data file
events = np.array(mne.events_from_annotations(pretask))
print(events)

#%% HRV analysis pipleine
ecg_data = pretask_bp[0,:][0] * 1e6
ecg_data = np.transpose(ecg_data)
ecg_df = pd.DataFrame(ecg_data, columns = ['ECG'])

# saving data for further explorations
ecg_df.to_csv('ecg_data_sorted.csv',
                      index=None)


# Find peaks
peaks, info = nk.ecg_peaks(ecg_df["ECG"], sampling_rate=1000)

# count the number of heart beats (same info in info)
peaks['ECG_R_Peaks'].value_counts()

RR_intervals_locations = list(info.values())[0]

# time-domain analysis
# Extract clean EDA and SCR features
hrv_time = nk.hrv_time(info, sampling_rate=1000, show=True)
hrv_time

# frequency domain analysis
hrv_freq = nk.hrv_frequency(info, sampling_rate=1000, show=True)
hrv_freq

# non-linear analysis
hrv_non = nk.hrv_nonlinear(info, sampling_rate=1000, show=True)
hrv_non

# All parameters
hrv_indices = nk.hrv(peaks, sampling_rate=1000, show=True)
hrv_indices

#%% Visualise HRV and extract features
# Process ecg
ecg_signals, info = nk.ecg_process(ecg_df["ECG"], sampling_rate=1000)

# Visual quality checks
plot = nk.ecg_plot(ecg_signals[:30000])

# extract features
all_params_hrv = nk.ecg_intervalrelated(ecg_signals)

all_params_hrv.to_csv('hrv_features.csv',
                      index=None)
