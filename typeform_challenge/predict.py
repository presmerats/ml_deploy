import pandas as pd

from typeform_challenge.processing.data_management import load_pipeline
from typeform_challenge.config import config


pipeline_file_name = "typeform_challenge.pkl"
_typeform_pipe = load_pipeline(file_name=pipeline_file_name)


def make_prediction(*, input_data) -> dict:
    """Make a prediction using the saved model pipeline."""

    data = pd.read_json(input_data)
    prediction = _typeform_pipe.predict(data[config.FEATURES])
    # inverse_transform (empty for now)
    output = prediction
    response = {"predictions": output}

    return response
