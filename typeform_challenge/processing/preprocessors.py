import numpy as np
import pandas as pd

from sklearn.base import BaseEstimator, TransformerMixin


class ReorderDiscreteVars(BaseEstimator, TransformerMixin):
    def __init__(self, variables=None):
        if not isinstance(variables, list):
            self.variables = [variables]
        else:
            self.variables = variables

    def fit(self, X, y):
        temp = pd.concat([X, y], axis=1)
        temp.columns = list(X.columns) + ["target"]

        # persist transforming dictionary
        self.encoder_dict_ = {}

        for var in self.variables:
            # median() or mean()?
            t = temp.groupby([var])["target"].median().sort_values(ascending=True).index
            self.encoder_dict_[var] = {k: i for i, k in enumerate(t, 0)}

        return self

    def assign_encoding_id(self, variable, x):
        try:
            return self.encoder_dict_[variable][x]
        except:
            self.encoder_dict_[variable][x] = (
                list(self.encoder_dict_[variable].keys())[-1] + 1
            )
            return self.encoder_dict_[variable][x]

    def transform(self, X):
        # encode labels
        X = X.copy()
        for feature in self.variables:
            # X[feature] = X[feature].map(self.encoder_dict_[feature])
            X[feature] = X[feature].apply(lambda x: self.assign_encoding_id(feature, x))

        return X


class DropUnwanted(BaseEstimator, TransformerMixin):
    def __init__(self, variables_to_drop=None):

        self.variables = variables_to_drop

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        # encode labels
        X = X.copy()
        X = X.drop(self.variables, axis=1)

        return X


class RemoveCorrelated(BaseEstimator, TransformerMixin):
    def __init__(self, variables=None):

        self.variables = variables

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        # encode labels
        X = X.copy()
        X = X.drop(self.variables, axis=1)

        return X
