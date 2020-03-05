import numpy as np
import pandas as pd

from eda_analysis import eda_analysis


def test_describe_na_value():
    no_na_dataframe = pd.DataFrame({"col_1": [0, 2],
                                    "col_2": [0.5, 0.1],
                                    "col_3": ["a", "b"]})

    na_numerical_dataframe = pd.DataFrame({"col_1": [0, 2],
                                           "col_2": [np.nan, 0.1],
                                           "col_3": ["a", "b"]})

    na_categorical_dataframe = pd.DataFrame({"col_1": [0, 2],
                                             "col_2": [0.5, 0.1],
                                             "col_3": [np.nan, "b"]})

    assert isinstance(eda_analysis.describe_na_values(no_na_dataframe), np.ndarray)
    assert np.array_equiv(eda_analysis.describe_na_values(no_na_dataframe), np.array([[1, 1],
                                                                                      [1, 1],
                                                                                      [1, 1]]))

    assert isinstance(eda_analysis.describe_na_values(na_numerical_dataframe), np.ndarray)
    assert np.array_equiv(eda_analysis.describe_na_values(na_numerical_dataframe), np.array([[1, 1],
                                                                                             [0, 1],
                                                                                             [1, 1]]))

    assert isinstance(eda_analysis.describe_na_values(na_categorical_dataframe), np.ndarray)
    assert np.array_equiv(eda_analysis.describe_na_values(na_categorical_dataframe), np.array([[1, 1],
                                                                                               [1, 1],
                                                                                               [0, 1]]))
