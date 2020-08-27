import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split
import joblib


from typeform_challenge import pipeline
from typeform_challenge.config import config
from typeform_challenge.processing.data_management import load_dataset, save_pipeline


def run_training() -> None:
    """Train the model."""

    # read training data
    data = load_dataset(file_name=config.TRAINING_DATA_FILE)

    # generate the target
    data["completion_rate"] = data["submissions"] / data["views"]

    # divide train and test
    X_train, X_test, y_train, y_test = train_test_split(
        data[config.FEATURES], data[config.TARGET], test_size=0.1, random_state=0
    )  # we are setting the seed here

    # transform the target
    # no transformation

    pipeline.typeform_pipe.fit(X_train[config.FEATURES], y_train)

    save_pipeline(pipeline_to_persist=pipeline.typeform_pipe)


if __name__ == "__main__":
    run_training()
