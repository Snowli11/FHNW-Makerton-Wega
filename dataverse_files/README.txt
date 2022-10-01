#########################
Daily Living Activity Recognition Using Wearable Devices: A Features-rich Dataset and a Novel Approach.

#########################
Maurizio Leotta, Andrea Fasciglione, Alessandro Verri
DIBRIS - Dipartimento di Informatica, Bioingegneria, Robotica e Ingegneria dei Sistemi
Università degli Studi di Genova, Genoa, Italy

########################
In any work using this dataset cite the related publication: 

Maurizio Leotta, Andrea Fasciglione, Alessandro Verri. Daily Living Activity Recognition Using Wearable Devices: A Features-Rich Dataset and a Novel Approach. In: Del Bimbo A. et al. (eds) Pattern Recognition. ICPR International Workshops and Challenges. ICPR 2021. Lecture Notes in Computer Science, vol.12662, pp.171-187. Springer, Cham, 2021. DOI: 10.1007/978-3-030-68790-8_15.

For any question concerning the dataset please write to: maurizio.leotta@unige.it

########################

Terms of Use 
Creative Commons Attribution Non Commercial Share Alike 4.0 (CC BY NC SA 4.0) public license is applied. https://creativecommons.org/licenses/by-nc-sa/4.0/

Disclaimer 
All the information provided in this dataset is provided on an "as is" and "as available" basis and you agree that you use such information entirely at your own risk. The authors cannot guarantee the validity of the information in the dataset. The authors give no warranty and accepts no responsibility or liability for the accuracy or the completeness of the information and materials contained in this dataset. Under no circumstances will the authors be held responsible or liable in any way for any claims, damages, losses, expenses, costs or liabilities whatsoever (including, without limitation, any direct or indirect damages for loss of profits, business interruption or loss of information) resulting or arising directly or indirectly from your use of this dataset, or from your reliance on the information and material in this dataset, even if the authors have been advised of the possibility of such damages in advance.

#########################

The dataset includes data of 8 volunteers, aged between 23-37, with a weight between 52-90 kg and height
between 172-186 cm
All the subjects were healthy. 

Each person performed 17 different activities:     
(Group A)
RELAX, KEYBOARD, LAPTOP, HANDWRITING, HANDWASHING, FACEWASHING, TEETHBRUSH,
SWEEPING, VACUUMING, EATING, DUSTING, RUBBING
(Group B)
DOWNSTAIRS, WALKING, WALKING FAST, UPSTAIRS, UPSTAIRS FAST

Group A activities have been performed for a fixed time, while Group B not. 
In particular, Group A activities have been performed for more than 120 seconds (in general for about 150 seconds), 
and we included in the dataset the central 120 seconds of each execution in order to obtain cleaner data.
On the other hand, Group B includes: 
- WALKING performed for 160 meters (in at least 110 seconds); 
- WALKING_FAST performed for 205 meters (in at least 110 seconds); 
- DOWNSTAIRS, UPSTAIRS, UPSTAIRS_FAST performed using a single flight of stairs with no intermediate floors between 
the steps for an average time of 40 seconds.

While performing these activities, the subjects were wearing these three devices with the following settings:
- 1 Actigraph Centrepoint at the dominant wrist. Accelerometer recording at a sampling rate of 256 Hz
- 1 Actigraph GT9X Link at the right hip at the height of the iliac crest (using the device belt clip). 
    IMU (i.e., accelerometer, magnetometer, and gyroscope) recording at a sampling rate of 100 Hz.
- 1 Actigraph GT9X Link at the height of the right ankle placed, with the help of the belt clip, on the
    subject's right side of the shoe, over the malleolus. IMU recording at a sampling rate of 100 Hz.

#########################

Hereby the description of the files in this folder:

- 'README.txt': this file

- 'subjects_info.csv' : file containing additional informations about subjects that took part in the experiments

- 'ankle_*': all raw data coming from the device on the ankle
- 'hip_*': all raw data coming from the device on the hip
- 'wrist_*': all raw data coming from the device on the hip

- 'ankle_X_0*.csv': file containing raw data of the device on the ankle; the number of the subject has to
    be replaced to the * character: the 'X_01.csv' file will contain data of the subject 01, and so on...
    The file contains 11 columns:
    - 'Timestamp': timestamp of the sampled values
    - 'Accelerometer X, 'Accelerometer Y', 'Accelerometer Z': instantaneous accelerations for each axis, 
        measured in units of gravity (G)
    - 'Temperature': IMU temperature, in Celsius degree
    - 'Gyroscope X', 'Gyroscope Y', 'Gyroscope Z': instantaneous measure of the gyroscope for each axis,
        measured in degrees/sec
    - 'Magnetometer X', 'Magnetometer Y', 'Magnetometer Z': instantaneous measured magnetic field for each axis,
        measured in microTesla (mT)
- 'ankle_Y_0*.csv': file containing the labels of the activity performed; the number of the subject has to be
    replaced to the * character: the 'Y_01.csv' file will contain data of the subject 01, and so on...
    The file contains only 1 column, called 'label'. For each row, there is the label of the activity performed at
    the associated instant in the file 'X_0*.csv'
    Hereby the labels that are present in the Y files:
    - 0 = OTHER
    - 1 = RELAX
    - 2 = KEYBOARD_WRITING
    - 3 = LAPTOP
    - 4 = HANDWRITING
    - 5 = HANDWASHING
    - 6 = FACEWASHING
    - 7 = TEETHBRUSH
    - 8 = SWEEPING
    - 9 = VACUUMING
    - 10 = EATING
    - 11 = DUSTING
    - 12 = RUBBING
    - 13 = DOWNSTAIRS
    - 14 = WALKING
    - 15 = WALKING_FAST,
    - 16 = UPSTAIRS_FAST
    - 17 = UPSTAIRS

- 'hip_X_0*.csv' : analogously to the ankle device files
- 'hip_Y_0*.csv' : analogously to the ankle device files

- 'wrist_X_0*.csv' : analogously to the ankle device files
- 'wrist_Y_0*.csv' : analogously to the ankle device files