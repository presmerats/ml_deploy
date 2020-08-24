import unittest
from unittest import mock
from unittest.mock import patch, Mock
from typeformtest.utils import (
    print_distribution,
    data_preparation_pipe,
    data_preparation_pipe2,
)
import pandas as pd
import numpy as np


class TestMyPlotGrid(unittest.TestCase):
    def setUp(self):
        self.setup_var = True

    def _test_iterator_creation(self):
        self.assertTrue(False)

    def _test_iterator_next(self):
        self.assertTrue(False)


class TestPipeline(unittest.TestCase):
    def setUp(self):
        self.setup_var = True

    def test_data_preparation_pipeline_new_column(self):

        # generate the fake dataset
        df = pd.DataFrame(
            {
                "form_id": [1, 2, 3],
                "views": [24, 301, 87],
                "submissions": [5, 96, 12],
                "feat_01": [2, 1, 3],
                "feat_02": [2, 1, 8],
            }
        )
        X_train_val = df

        target_column = "completion_ratio"
        X_train_val[target_column] = X_train_val["submissions"] / X_train_val["views"]

        # call the data_preparation_pipe without the model
        prep_pipe = data_preparation_pipe2(numerical_columns=["feat_01"],)

        prep_pipe.fit(X_train_val, X_train_val[target_column])
        X_result = prep_pipe.fit_transform(X_train_val, X_train_val[target_column])

        self.assertEqual(X_result.shape, (3, 1))
        self.assertEqual(X_result.max(), 1)
        self.assertEqual(X_result.min(), 0)

    def _test_data_preparation_pipeline_normalization(self):
        self.assertTrue(False)


if __name__ == "__main__":
    unittest.main()
