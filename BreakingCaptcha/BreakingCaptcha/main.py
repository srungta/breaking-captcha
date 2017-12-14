from pre_process import distribution,file_helper

#Constants
ALL_IMAGES = "captcha_images"
TEST_IMAGES = "TESTSET"
TRAIN_IMAGES = "TRAINSET"
VALIDATION_IMAGES = "VALIDATIONSET"

all_files = file_helper.get_filenames_from_folder(ALL_IMAGES)
train, validate, test = distribution.create_data_sets(all_files, 70, 20, 10)




