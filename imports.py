# to install uninstalled packages
#!{sys.executable} -m pip install --upgrade pip

# sys
import sys
import os
import time
import zipfile
import json
from collections import defaultdict
import re
import random

# notebook related
import tqdm

# num realted
import pandas as pd
import numpy as np
import scipy

# plotting related
import matplotlib.pyplot as plt
import seaborn as sns

# machine learning related
import sklearn
import lightgbm
import tensorflow as tf
from tensorflow import keras
L = keras.layers
K = keras.backend
from keras_utils import reset_tf_session
