# Mentat
EEG analysis project with Emotiv Epoc+. The virtual environment name is `brenv`

## Experiment 1: Music or No Music
This simple starter experiment will attempt to detect the difference between me listening to music and me not listening to music. 

Standard EEG bands range from 4hz-45hz.

### Procedure:
1. Record 3-Minute EEG without listening to music.
2. Record 3-Minute EEG while listening to music.
3. Clean data by cutting off very beginning of each recording (first 10 seconds = 10*128 = 1280 samples)
4. Split each recording into 

## Experiment 2: Button Press Predictor
This experiment is for predicting, based on raw EEG data, whether or not a user will press a button at the end of a chunk of EEG signal.
