# HRV analysis
- Data was acquired using brain products actiChanp plus
- EEG electrodes (11 and 22) were used for ECG data collection in lead I config
- ECG1 going to 11 (left) and ECG2 to 22 (right) (Cross check once)
- Did ECG2-ECG1
- mne-python has good amount of features in in-built visualisation

# Neurokit2 based analysis and viz
Raw ECG trace looked like this with baseline correction
![Raw trace](https://github.com/rahulvenugopal/HRV_adventures/blob/main/results/After_baseline_correction.jpg)
---

Time domain, Frequency domain and Non-linear methods
![Parameters](https://github.com/rahulvenugopal/HRV_adventures/blob/main/results/All_parameters_HRV.jpeg)
---

General visualisations
![Overall viz](https://github.com/rahulvenugopal/HRV_adventures/blob/main/results/Summary_HRV.jpeg)
---

Documentation of features from functions [page](https://github.com/neuropsychology/NeuroKit/tree/master/neurokit2/hrv)
- Frequency domainulf=(0, 0.0033),
`vlf=(0.0033, 0.04)`
`lf=(0.04, 0.15)`
`hf=(0.15, 0.4)`
`vhf=(0.4, 0.5)`
- For instance, 1, 2 and 5 minutes of high quality signal are the recomended minima for HF, LF and LF/HF, respectively
---


        - **Characteristics of the Poincaré Plot Geometry**:
            - **SD1**: SD1 is a measure of the spread of RR intervals on the Poincaré plot
            perpendicular to the line of identity. It is an index of short-term RR interval
            fluctuations, i.e., beat-to-beat variability. It is equivalent (although on another
            scale) to RMSSD, and therefore it is redundant to report correlations with both
            (Ciccone, 2017).
            - **SD2**: SD2 is a measure of the spread of RR intervals on the Poincaré plot along the
            line of identity. It is an index of long-term RR interval fluctuations.
            - **SD1SD2**: the ratio between short and long term fluctuations of the RR intervals
            (SD1 divided by SD2).
            - **S**: Area of ellipse described by SD1 and SD2 (``pi * SD1 * SD2``). It is
            proportional to *SD1SD2*.
            - **CSI**: The Cardiac Sympathetic Index (Toichi, 1997), calculated by dividing the
            longitudinal variability of the Poincaré plot (``4*SD2``) by its transverse variability (``4*SD1``).
            - **CVI**: The Cardiac Vagal Index (Toichi, 1997), equal to the logarithm of the product of
            longitudinal (``4*SD2``) and transverse variability (``4*SD1``).
            - **CSI_Modified**: The modified CSI (Jeppesen, 2014) obtained by dividing the square of
            the longitudinal variability by its transverse variability.
        - **Indices of Heart Rate Asymmetry (HRA), i.e., asymmetry of the Poincaré plot** (Yan, 2017):
            - **GI**: Guzik's Index, defined as the distance of points above line of identity (LI)
            to LI divided by the distance of all points in Poincaré plot to LI except those that
            are located on LI.
            - **SI**: Slope Index, defined as the phase angle of points above LI divided by the
            phase angle of all points in Poincaré plot except those that are located on LI.
            - **AI**: Area Index, defined as the cumulative area of the sectors corresponding to
            the points that are located above LI divided by the cumulative area of sectors
            corresponding to all points in the Poincaré plot except those that are located on LI.
            - **PI**: Porta's Index, defined as the number of points below LI divided by the total
            number of points in Poincaré plot except those that are located on LI.
            - **SD1d** and **SD1a**: short-term variance of contributions of decelerations
            (prolongations of RR intervals) and accelerations (shortenings of RR intervals),
            respectively (Piskorski,  2011).
            - **C1d** and **C1a**: the contributions of heart rate decelerations and accelerations
            to short-term HRV, respectively (Piskorski,  2011).
            - **SD2d** and **SD2a**: long-term variance of contributions of decelerations
            (prolongations of RR intervals) and accelerations (shortenings of RR intervals),
            respectively (Piskorski,  2011).
            - **C2d** and **C2a**: the contributions of heart rate decelerations and accelerations
            to long-term HRV, respectively (Piskorski,  2011).
            - **SDNNd** and **SDNNa**: total variance of contributions of decelerations
            (prolongations of RR intervals) and accelerations (shortenings of RR intervals),
            respectively (Piskorski,  2011).
            - **Cd** and **Ca**: the total contributions of heart rate decelerations and
            accelerations to HRV.
        - **Indices of Heart Rate Fragmentation** (Costa, 2017):
            - **PIP**: Percentage of inflection points of the RR intervals series.
            - **IALS**: Inverse of the average length of the acceleration/deceleration segments.
            - **PSS**: Percentage of short segments.
            - **PAS**: IPercentage of NN intervals in alternation segments.
        - **Indices of Complexity**:
            - **ApEn**: The approximate entropy measure of HRV, calculated by `entropy_approximate()`.
            - **SampEn**: The sample entropy measure of HRV, calculated by `entropy_sample()`.
            - **ShanEn**: The Shannon entropy measure of HRV, calculated by `entropy_shannon()`.
            - **FuzzyEn**: The fuzzy entropy measure of HRV, calculated by `entropy_fuzzy()`.
            - **MSE**: The multiscale entropy measure of HRV, calculated by `entropy_multiscale()`.
            - **CMSE**: The composite multiscale entropy measure of HRV, calculated by `entropy_multiscale()`.
            - **RCMSE**: The refined composite multiscale entropy measure of HRV, calculated by `entropy_multiscale()`.
            - **CD**: The Correlation Dimension of the HR signal, calculated by `fractal_correlation()`.
            - **HFD**: The Higuchi's Fractal Dimension of the HR signal, calculated by `fractal_higuchi()`.
            kmax is set to "default".
            - **KFD**: The Katz's Fractal Dimension of the HR signal, calculated by `fractal_katz()`.
            - **LZC**: The Lempel-Ziv complexity of the HR signal, calculated by `fractal_lempelziv()`.
            - **DFA_alpha1**: The monofractal detrended fluctuation analysis of the HR signal corresponding
            to short-term correlations, calculated by `fractal_dfa()`.
            - **DFA_alpha2**: The monofractal detrended fluctuation analysis of the HR signal corresponding
            to long-term correlations, calculated by `fractal_dfa()`.
            - **DFA_alpha1_ExpRange**: The multifractal detrended fluctuation analysis of the HR signal
            corresponding to short-term correlations, calculated by `fractal_dfa()`. ExpRange is the range of
            singularity exponents, correspoinding to the width of the singularity spectrum.
            - **DFA_alpha2_ExpRange**: The multifractal detrended fluctuation analysis of the HR signal
            corresponding to long-term correlations, calculated by `fractal_dfa()`. ExpRange is the range of
            singularity exponents, correspoinding to the width of the singularity spectrum.
            - **DFA_alpha1_ExpMean**: Multifractal DFA. ExpMean is the mean of singularity exponents.
            - **DFA_alpha2_ExpMean**: Multifractal DFA. ExpMean is the mean of singularity exponents.
            - **DFA_alpha1_DimRange**: The multifractal detrended fluctuation analysis of the HR signal
            corresponding to short-term correlations, calculated by `fractal_dfa()`. DimRange is the range of
            singularity dimensions, correspoinding to the height of the singularity spectrum.
            - **DFA_alpha2_DimRange**: The multifractal detrended fluctuation analysis of the HR signal
            corresponding to long-term correlations, calculated by `fractal_dfa()`. DimRange is the range of
            singularity dimensions, correspoinding to the height of the singularity spectrum.
            - **DFA_alpha1_DimMean**: Multifractal DFA. Dimmean is the mean of singularity dimensions.
            - **DFA_alpha2_DimMean**: Multifractal DFA. Dimmean is the mean of singularity dimensions.

