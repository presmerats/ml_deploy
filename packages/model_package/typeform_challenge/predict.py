import pandas as pd
import json

from typeform_challenge.processing.data_management import load_pipeline
from typeform_challenge.config import config
from typeform_challenge.processing.validation import validate_inputs
from typeform_challenge import __version__ as _version

import logging


_logger = logging.getLogger(__name__)


pipeline_file_name = f"{config.PIPELINE_SAVE_FILE}{_version}.pkl"
_typeform_pipe = load_pipeline(file_name=pipeline_file_name)


def make_prediction(*, input_data) -> dict:
    """Make a prediction using the saved model pipeline."""

    # data = pd.read_json(input_data)
    _logger.info(f"input_data: {input_data}")

    data = pd.DataFrame(input_data)
    validated_data = validate_inputs(input_data=data)
    prediction = _typeform_pipe.predict(data[config.FEATURES])
    # inverse_transform (empty for now)
    output = prediction

    results = {"predictions": output, "version": _version}

    _logger.info(
        f"Making prgit edictions with model version: {_version} "
        f"Inputs: {validated_data} "
        f"Predictions: {results}"
    )

    return results
