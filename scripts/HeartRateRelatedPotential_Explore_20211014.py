# -*- coding: utf-8 -*-
"""
Explore Heart Rate Related Potential  

Created on Thu Oct 14 09:29:20 2021

@author: Dr Arun Sasidharan
"""

#%% Import Libraries
from tkinter.filedialog import askopenfilename
from tkinter import Tk
import numpy as np
import matplotlib.pyplot as plt
import mne


#%% Select the EEG file
Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
eeg_filename = askopenfilename(title = "Select EEG Data file",
                              filetypes = (("EDF file","*.edf"),
                                           ("BrainAnalyser file","*.vhdr*"),
                                           ("SET file","*.set*")))

#%% Load EEG data
if eeg_filename.find('.edf')>0:
    raw = mne.io.read_raw_edf(eeg_filename, preload=True)
elif eeg_filename.find('.set')>0:
    raw = mne.io.read_raw_eeglab(eeg_filename, preload=True)

#%% Get EEG info
srate       = raw.info.get('sfreq')
times       = raw.times
chanlist    = raw.info.get('ch_names')

#%% Set channel info
raw.set_channel_types({'ECG1': 'ecg','ECG2': 'ecg'})
montage = mne.channels.make_standard_montage('standard_1005')
raw.set_montage(montage)

#%% Filter the data
raw.filter(0.5,None,fir_design='firwin').load_data()
raw.filter(None,40,fir_design='firwin').load_data()

#%% Gets events from annotation
events = np.array(mne.events_from_annotations(raw))
event_keys = list(events[1].keys())
event_values = list(events[1].values())

#%% ECG epochs
for i in range(len(event_keys)-1):
    
    # Create a segment around the annotation
    eegseg = raw.copy().crop(events[0][i,0]/srate,events[0][i+1,0]/srate)
    
    # rpeaks_mne = mne.preprocessing.find_ecg_events(raw, event_id=999, ch_name='ECG1')
    
    # Epoch based on R peaks from ECG
    ecgepochs = mne.preprocessing.create_ecg_epochs(
        eegseg, ch_name='ECG1', event_id=999, picks=None, 
        tmin=- 0.5, tmax=0.5,baseline=(-0.5,0.0))
    
    # Average the epochs
    ecgerp = ecgepochs.average() 
    
    # Plot the ERP
    ecgerp.plot()
    plt.ylim([-30,5])
    plt.title('%s' %(event_keys[event_values.index(i+1)]))
