﻿from __future__ import print_function
import numpy as np
import sys
import os
import argparse


###################################################################
# Variables                                                       #
# When launching project or scripts from Visual Studio,           #
# input_dir and output_dir are passed as arguments.               #
# Users could set them from the project setting page.             #
###################################################################

input_dir = None
output_dir = None
log_dir = None


#################################################################################
# Keras configs.                                                                #
# Please refer to https://keras.io/backend .                                    #
#################################################################################

import keras
from keras import backend as K

#K.set_floatx('float32')
#String: 'float16', 'float32', or 'float64'.

#K.set_epsilon(1e-05)
#float. Sets the value of the fuzz factor used in numeric expressions.

#K.set_image_data_format('channels_first')
#data_format: string. 'channels_first' or 'channels_last'.


#################################################################################
# Keras imports.                                                                #
#################################################################################

from keras.models import Model
from keras.models import Sequential
from keras.layers import Input
from keras.layers import Lambda
from keras.layers import Layer
from keras.layers import Dense
from keras.layers import Dropout
from keras.layers import Activation
from keras.layers import Flatten
from keras.layers import Conv2D
from keras.layers import MaxPooling2D
from keras.optimizers import SGD
from keras.optimizers import RMSprop


def main():
    exit(0)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input_dir", type=str, 
                        default=None, 
                        help="Input directory where where training dataset and meta data are saved", 
                        required=False
                        )
    parser.add_argument("--output_dir", type=str, 
                        default=None, 
                        help="Input directory where where logs and models are saved", 
                        required=False
                        )

    args, unknown = parser.parse_known_args()
    input_dir = args.input_dir
    output_dir = args.output_dir
    log_dir = output_dir

    main()
