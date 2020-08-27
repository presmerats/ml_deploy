from sklearn.ensemble import RandomForestRegressor
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import MinMaxScaler

import preprocessors as pp
import config

"""
First version pipeline will include:

Sorting discrete values
Removing correlated features
MinMaxScaler

"""

price_pipe = Pipeline(
    [
        # ("remove_unwanted", pp.DropUnwanted(variables_to_drop=config.UNWANTED_VARS),),
        ("reorder_discrete", pp.ReorderDiscreteVars(variables=config.DISCRETE_VARS),),
        ("remove_correlated", pp.RemoveCorrelated(variables=config.CORRELATED_VARS),),
        ("scaler", MinMaxScaler()),
        (
            "regressor",
            RandomForestRegressor(
                max_depth=16, max_features=8, n_estimators=16, random_state=0
            ),
        ),
    ]
)
