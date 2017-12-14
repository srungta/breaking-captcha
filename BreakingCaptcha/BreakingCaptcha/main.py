import os
import numpy as np
from pre_process import distribution,file_helper

#Constants
CWD = os.getcwd()
ALL_IMAGES = CWD + "\\captcha_images"
TEST_IMAGES = CWD + "\\TESTSET"
TRAIN_IMAGES = CWD + "\\TRAINSET"
VALIDATION_IMAGES = CWD + "\\VALIDATIONSET"

#Create the folders for training , testing and validation images
file_helper.create_folder(TEST_IMAGES)
file_helper.create_folder(TRAIN_IMAGES)
file_helper.create_folder(VALIDATION_IMAGES)

#Move the files into respective folders
all_files = np.array(file_helper.get_filenames_from_folder(ALL_IMAGES))
train, validate, test = distribution.create_data_sets(all_files, 70, 20, 10)

for filename in train:
    file_helper.copy_file(os.path.join(ALL_IMAGES,filename), os.path.join(TRAIN_IMAGES,filename))

for filename in test:
    file_helper.copy_file(os.path.join(ALL_IMAGES,filename), os.path.join(TEST_IMAGES,filename))

for filename in validate:
    file_helper.copy_file(os.path.join(ALL_IMAGES,filename), os.path.join(VALIDATION_IMAGES,filename))




