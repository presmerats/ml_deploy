import pathlib

import typeform_challenge

import pandas as pd


pd.options.display.max_rows = 10
pd.options.display.max_columns = 10


PACKAGE_ROOT = pathlib.Path(typeform_challenge.__file__).resolve().parent
TRAINED_MODEL_DIR = PACKAGE_ROOT / "trained_models"
DATASET_DIR = PACKAGE_ROOT / "datasets"

# data
TESTING_DATA_FILE = "test.csv"
# TRAINING_DATA_FILE = "train.csv"
TRAINING_DATA_FILE = "completion_rate.csv"


# PIPELINE_NAME = "regression_pipe"

TARGET = "completion_rate"

# input variables
FEATURES = [
    "feat_01",
    "feat_02",
    "feat_03",
    "feat_04",
    "feat_05",
    "feat_06",
    "feat_07",
    "feat_08",
    "feat_09",
    "feat_10",
    "feat_11",
    "feat_12",
    "feat_13",
    "feat_14",
    "feat_15",
    "feat_16",
    "feat_17",
    "feat_18",
    "feat_19",
    "feat_20",
    "feat_21",
    "feat_22",
    "feat_23",
    "feat_24",
    "feat_25",
    "feat_26",
    "feat_27",
    "feat_28",
    "feat_29",
    "feat_30",
    "feat_31",
    "feat_32",
    "feat_33",
    "feat_34",
    "feat_35",
    "feat_36",
    "feat_37",
    "feat_38",
    "feat_39",
    "feat_40",
    "feat_41",
    "feat_42",
    "feat_43",
    "feat_44",
    "feat_45",
    "feat_46",
    "feat_47",
]


UNWANTED_VARS = [
    "form_id",
    "views",
    "submissions",
]


CORRELATED_VARS = [
    "feat_06",
    "feat_38",  # 36, 19, 40, 33
    "feat_36",  # 38, 19, 40
    "feat_19",  # 38, 36, 40, 33
    #'feat_40', # 19, 38, 36 -> don't removve
    "feat_43",
    "feat_07",  # 47, 30
    "feat_43",  # 42, 05
    "feat_46",
]

DISCRETE_VARS = [
    "feat_01",
    "feat_04",
    "feat_08",
    "feat_10",
    "feat_13",
    "feat_15",
    "feat_20",
    "feat_35",
    "feat_44",
]


PIPELINE_NAME = "typeform_challenge"
PIPELINE_SAVE_FILE = f"{PIPELINE_NAME}_output_v"

# used for differential testing
ACCEPTABLE_MODEL_DIFFERENCE = 0.05
