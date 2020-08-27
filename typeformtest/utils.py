import math
import os
import sys

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import sklearn
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn import preprocessing
from sklearn.pipeline import FeatureUnion
from sklearn.pipeline import Pipeline
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import mean_squared_error
from sklearn.linear_model import LinearRegression, Ridge
from sklearn.ensemble import RandomForestRegressor
from sklearn.neighbors import KNeighborsRegressor


def print_distribution(dataf, column, axis):

    if dataf[column].dtype == "float64" or dataf[column].dtype == "int32":
        bins = int(len(dataf) * 0.01)
        axis.hist(dataf[column], color="blue", edgecolor="black", bins=bins)

        # Add labels
        axis.set_title(column)
        # axis.set(xlabel='x-label', ylabel='y-label')
        # axis.label_outer()

    else:
        vc = dataf[column].value_counts()
        counts = vc.values.tolist()
        labels = vc.keys().tolist()
        x = np.arange(len(labels))
        axis.bar(x, counts, label=column)

    axis.set_title(column)


class MyPlotGrid:
    def __init__(self, ncols, total_plots, figsize=(15, 10), padding=3.0):
        self.ncols = ncols
        self.total_plots = total_plots
        self.nrows = math.ceil(total_plots / ncols)
        print("num rows", self.nrows, "num cols", self.ncols, " total", total_plots)
        self.fig, self.axs = plt.subplots(self.nrows, self.ncols, figsize=figsize)
        self.fig.tight_layout(pad=padding)

    def __iter__(self):
        self.current_col = 0
        self.current_row = 0
        return self

    def __next__(self):
        if self.current_row < self.nrows:
            x = self.axs[self.current_row, self.current_col]
            self.current_col = self.current_col + 1
            if self.current_col == self.ncols:
                self.current_col = 0
                self.current_row += 1
            return x
        else:
            raise StopIteration


def my_distributions_view(df, selected_columns, ncols=2, figsize=(15, 25)):
    plot_grid = MyPlotGrid(
        ncols=ncols, total_plots=len(selected_columns), figsize=figsize
    )
    plot_grid_iter = iter(plot_grid)
    for column in selected_columns:
        plot_axis = next(plot_grid_iter)
        print_distribution(df, column, plot_axis)


def split_dataset(df):
    X = list(df.index)
    y = list(df.index)
    X_train_val, X_test, y_train_val, y_test = train_test_split(X, y, test_size=0.20)

    X_train, X_validation, y_train, y_validation = train_test_split(
        X_train_val, y_train_val, test_size=0.20
    )

    df_train_val = df.loc[X_train_val, :]
    df_train = df.loc[X_train, :]
    df_validation = df.loc[X_validation, :]
    df_test = df.loc[X_test, :]

    # transform to a numpy array for each case?

    return df_train_val, df_train, df_validation, df_test


class ItemSelector(BaseEstimator, TransformerMixin):
    """For data grouped by feature, select subset of data at a provided list of  keys.

    Parameters
    ----------
    keys : hashable, required
        The list of keys corresponding to the desired value in a mappable.
    """

    def __init__(self, keys):
        self.keys = keys

    def fit(self, x, y=None):
        return self

    def transform(self, df):
        # subset
        df2 = df.loc[:, self.keys]
        return df2


class TargetGenerator(BaseEstimator, TransformerMixin):
    """
    convert to numpy
    """

    def __init__(self, name, nominator, denominator):
        self.name = name
        self.nominator = nominator
        self.denominator = denominator
        self.x = None

    def fit(self, x, y=None):
        return self

    def transform(self, df):
        df[self.name] = df[self.nominator] / df[self.denominator]
        # must return a DataFrame and not a Series!
        return pd.DataFrame(df[self.name])


def data_preparation_pipe(numerical_columns=[]):

    pipe = Pipeline(
        [
            ("selector", ItemSelector(keys=numerical_columns)),
            # ("floatsonly", FloatCast()),
            # ("formatter", NumpyFormatter()),
            ("scaling", preprocessing.MinMaxScaler(),),
        ]
    )

    return pipe


def get_model(model_type):
    models = {
        "RandomForestRegressor": RandomForestRegressor(),
        "linearRegression": LinearRegression(),
        "Ridge": Ridge(),
        "KNeighborsRegressor": KNeighborsRegressor(),
    }

    return models.get(model_type, models["linearRegression"])


def global_pipeline_train(
    all_features,
    numerical_features,
    params_grid,
    score,
    score_cls,
    X_train_val,
    X_test,
    target_column,
    training_job_name,
    model_type,
):

    prep_pipe = data_preparation_pipe(numerical_columns=numerical_features,)

    target_column = "completion_ratio"
    X_train_val[target_column] = X_train_val["submissions"] / X_train_val["views"]
    X_test[target_column] = X_test["submissions"] / X_test["views"]

    training_model = get_model(model_type)
    pipe = Pipeline([("union", prep_pipe), ("clf", training_model),])
    grid = GridSearchCV(pipe, n_jobs=1, param_grid=params_grid, scoring=score)
    grid.fit(
        X_train_val.loc[:, all_features], X_train_val.loc[:, target_column],
    )

    y_true = X_test.loc[:, target_column]
    y_pred = grid.predict(X_test.loc[:, all_features])

    the_average = None
    if score.find("macro") > -1:
        the_average = "macro"
    elif score.find("micro") > -1:
        the_average = "micro"
    elif score.find("weighted") > -1:
        the_average = "weighted"

    result_line = {
        "name": training_job_name,
        "prefix": pipe.get_params()["steps"][1][0],
        "model_class": pipe.get_params()["steps"][1][1],
        "trained_score": grid.best_score_,
        "scorer_func": grid.scorer_._score_func.__name__,
        "params": grid.best_params_,
        "test_score": np.sqrt(
            score_cls(y_true, y_pred)
        ),  # f1_score(y_true, y_pred, average=the_average),
    }

    return result_line


def update_results(results, result_line):
    for k, v in result_line.items():
        results[k].append(v)


def classification_reporting(y, X_test):
    print(classification_report(y, X_test.loc[:, "Churn"]))

