import altair as alt
import numpy as np
import pandas as pd
import pytest

from src.eda_analysis import eda_analysis as eda


def helper_create_data(n=500):
    """
    Helper function for creating dataframe for testing

    Parameters
    -----------
    n: int (default value = 500)
        Number of rows to be generated for the dataframe

    Returns
    --------
    pandas.DataFrame
        Returns a dataframe to be used for testing

    Examples
    ---------
    >>> helper_create_data()
    """
    N1 = list(np.random.exponential(3, n))
    N2 = list(np.random.normal(2, 2, n))
    N3 = list(np.random.normal(10, 3, n))
    C1 = list(np.random.binomial(1, 0.7, n))
    C2 = list(np.random.poisson(1, n))
    C3 = list(np.random.binomial(5, 0.4, n))
    a = ['cat', 'dog', 'lion']
    C4 = list(np.random.choice(a, n))
    df = pd.DataFrame({
        'C1': C1,
        'C2': C2,
        'C3': C3,
        'N1': N1,
        'N2': N2,
        'N3': N3,
        'C4': C4
    })
    rows = list(np.random.randint(0, n, 20))
    cols = list(np.random.randint(0, 7, 5))
    df.iloc[rows, cols] = np.nan

    return df


def test_generate_report():
    """
    Tests the generate_report function to make sure the outputs are correct.

    Returns
    --------
    None
        The test should pass and no asserts should be displayed.
    """
    # Calling helper function to create data
    data = helper_create_data()
    cat_vars = ['C1', 'C2', 'C3', 'C4']
    num_vars = ['N1', 'N2', 'N3']

    # Positive test case: Checking whether the function runs properly or not
    assert eda.generate_report(data, cat_vars, num_vars), \
        "Expected True but False returned"

    # Negative test case: Checking whether the function returns False
    # fr wrong output
    assert not eda.generate_report(data, cat_vars, "String Input"), \
        "Expected False but True returned"


def test_describe_cat_var():
    """
    Tests the describe_cat_var function to make sure the outputs are correct.

    Returns
    --------
    None
        The test should pass and no asserts should be displayed.
    """
    # Calling helper function to create data
    data = helper_create_data()
    cat_vars = ['C1', 'C2', 'C3', 'C4']
    # Testing data frame exception
    x = [1, 2, 3]
    try:
        eda.describe_cat_var(x, cat_vars)
        assert False, 'Exception must be thorwn for this test case'
    except Exception as ex:
        assert "The value of the argument 'dataframe' must be of type " \
               "'pandas.DataFrame'" == str(ex), 'Expected exception not thrown'

    # Testing categorical variable exception
    try:
        eda.describe_cat_var(data, x)
        assert False, 'Exception must be thorwn for this test case'
    except Exception as ex:
        assert "The value of the argument 'cat_vars' must be" \
               " a list of strings" == str(ex), 'Expected exception not thrown'

    # Testing columns subset exception
    try:
        cols = ['Y1', 'Y2']
        eda.describe_cat_var(data, cols)
        assert False, 'Exception must be thorwn for this test case'
    except Exception as ex:
        assert "The input categorical column names must belong" \
               " to the dataframe" == str(ex), 'Expected exception not thrown'

    # Testing non-zero input is being passed to n_col
    try:
        eda.describe_cat_var(data, cat_vars, 0)
        assert False, 'Exception must be thorwn for this test case'
    except Exception as ex:
        assert "The value of the argument 'n_cols' must be a positive " \
               "non zero integer" == str(ex), 'Expected exception not thrown'

    # testing integer is passed to n_col
    try:
        eda.describe_cat_var(data, cat_vars, "z")
        assert False, 'Exception must be thorwn for this test case'
    except Exception as ex:
        assert "The value of the argument 'n_cols' must be a positive" + \
               " non zero integer" == str(ex), 'Expected exception not thrown'

    # Testing type of returned value
    p = eda.describe_cat_var(data, cat_vars)
    assert isinstance(p, alt.vegalite.v3.api.VConcatChart), \
        'The function must return an altair plot'

    # Testing if the specified columns has been plotted or not
    p = eda.describe_cat_var(data, cat_vars)
    assert set(p.data.columns) == set(cat_vars), \
        'The specified categorical columns were not plotted'


def test_calc_cor():
    """
    Tests the correlation function calc_cor to make sure the outputs are
    correctly rendering.

    Returns
    --------
    None
        The test should pass and no asserts should be displayed.
    """

    data = helper_create_data()
    num_vars = ["N1", "N2", "N3"]
    chart = eda.calc_cor(data, num_vars)

    # Check the data in the correlation matrix to be between -1 and 1
    for i in range(0, len(chart.data)):
        assert chart.data.iloc[i, 2] >= -1, \
            "Out of range values: lower than -1"
        assert chart.data.iloc[i, 2] <= 1, \
            "Out of range values: higher than 1"

    # Tests if the first and last value is 1 since it correlates to itself
    assert chart.data.iloc[0, 2] == 1, \
        "The first value should be 1 because it is correlated to itself"
    assert chart.data.iloc[-1, 2] == 1, \
        "The last value should be 1 because it is correlated to itself"

    # Test that Var1 and Var2 are equal in the first and last row
    assert chart.data.iloc[0, 0] == chart.data.iloc[0, 1], \
        "The Var1 should equal Var2 in the first row"
    assert chart.data.iloc[-1, 0] == chart.data.iloc[-1, 1], \
        "The Var1 should equal Var2 in the last row"

    # Test if the axes are properly mapped to the correct field
    spec = chart.to_dict()
    assert spec["layer"][1]["encoding"]["x"]["field"] == 'Var1', \
        "Plot x-axis should be mapped to Var1"
    assert spec["layer"][1]["encoding"]["y"]["field"] == 'Var2', \
        "Plot y-axis should be mapped to Var2"

    # Tests if the plot type is correct
    assert "altair" in str(type(chart)), "Plot type is not an Altair object"

    # Tests the exception is correctly raised when columns are not numeric
    with pytest.raises(Exception) as e:
        assert eda.calc_cor(data, ["C4"])
    assert str(e.value) == "Columns are not all numeric"

    # Tests the exception is correctly raised when
    # 'columns are not numeric 'dataframe' is not the correct type.
    with pytest.raises(Exception) as e:
        assert eda.calc_cor(["N1"], ["N1"])
    assert str(e.value) == "Input 'dataframe' is not a dataframe"

    # Tests the exception is correctly raised when 'num_vars' is not a string.
    with pytest.raises(Exception) as e:
        assert eda.calc_cor(data, ['N1', 1])
    assert str(e.value) == "The value of the argument 'num_vars' should be" \
                           " a list of strings."

    # Tests the exception is correctly raised when 'num_vars' is not a string
    with pytest.raises(Exception) as e:
        assert eda.calc_cor(data, 'N1')
    assert str(e.value) == "The value of the argument 'num_vars' should be" \
                           " a list of strings."

    # Tests the exception is correctly raised when
    # elements in 'num_vars' are not unique.
    with pytest.raises(Exception) as e:
        assert eda.calc_cor(data, ['N1', 'N1'])
    assert str(e.value) == "The elements in the argument 'num_vars' " \
                           "should be unique."

    # Test the Exception is correctly raised when 'num_vars' argument
    # is not a subset of the column names of the dataframe
    with pytest.raises(Exception) as e:
        assert eda.calc_cor(data, ["N1", "abc"])
    assert str(e.value) == "The argument 'num_vars' should be a subset " \
                           "of the column names from the dataframe."
    # Generate test data from the helper function.


# noinspection PyBroadException
def test_describe_na_value():
    """
    Tests the test_describe_na_value function
    to make sure the outputs are correct.

    Returns
    --------
    None
        The test should pass and no asserts should be displayed.
    """
    no_na_dataframe = pd.DataFrame({"col_1": [0, 2],
                                    "col_2": [0.5, 0.1],
                                    "col_3": ["a", "b"]})

    na_numerical_dataframe = pd.DataFrame({"col_1": [0, 2],
                                           "col_2": [np.nan, 0.1],
                                           "col_3": ["a", "b"]})

    na_categorical_dataframe = pd.DataFrame({"col_1": [0, 2],
                                             "col_2": [0.5, 0.1],
                                             "col_3": [np.nan, "b"]})

    not_a_dataframe = [[0, 2],
                       [0.5, 0.1],
                       ["a", "b"]]

    try:
        eda.describe_na_values(not_a_dataframe)
    except Exception:
        pass
    else:
        raise Exception("expected an Exception, but none were raised")

    assert isinstance(eda.describe_na_values(no_na_dataframe),
                      pd.DataFrame)
    assert np.array_equiv(eda.describe_na_values(no_na_dataframe),
                          pd.DataFrame([[1, 1],
                                        [1, 1],
                                        [1, 1]],
                                       index=no_na_dataframe.columns))

    assert isinstance(eda.describe_na_values(na_numerical_dataframe),
                      pd.DataFrame)
    assert np.array_equiv(eda.describe_na_values(na_numerical_dataframe),
                          pd.DataFrame([[1, 1],
                                        [0, 1],
                                        [1, 1]],
                                       index=na_numerical_dataframe.columns))

    assert isinstance(eda.describe_na_values(na_categorical_dataframe),
                      pd.DataFrame)
    assert np.array_equiv(eda.describe_na_values(na_categorical_dataframe),
                          pd.DataFrame([[1, 1],
                                        [1, 1],
                                        [0, 1]],
                                       index=na_categorical_dataframe.columns))


def test_describe_num_var():
    """
    Tests the describe_num_var function to make sure the outputs are correct.

    Returns
    --------
    None
        The test should pass and no asserts should be displayed.
    """
    # Generate test data from the helper function.
    test_data = helper_create_data()
    test_col = test_data['N1']

    # Test the results when the input is correct.
    summary, plot = eda.describe_num_var(test_data, ['N1', 'N2'])

    # Test if the statistical summary is correctly calculated.
    assert summary['N1'][0] == np.nanquantile(test_col, 0.25), \
        "25% quantile is not correctly calculated."
    assert summary['N1'][1] == np.nanquantile(test_col, 0.75), \
        "75% quantile is not correctly calculated."
    assert summary['N1'][2] == np.nanmin(test_col), \
        "Minimal value is not correctly calculated."
    assert summary['N1'][3] == np.nanmax(test_col), \
        "Maximal value is not correctly calculated."
    assert summary['N1'][4] == np.nanmedian(test_col), \
        "Median value is not correctly calculated."
    assert summary['N1'][5] == np.nanmean(test_col), \
        "Mean value is not correctly calculated."
    assert summary['N1'][6] == np.nanstd(test_col), \
        "Standard deviation is not correctly calculated."

    # Test the plot type is correct.
    assert isinstance(plot, alt.vegalite.v3.api.FacetChart), \
        "Plot type is not an Altair object."
    assert plot.to_dict()['spec']['mark'] == 'bar', \
        "The plot should be a bar chart."

    # Test the axes of the plot is correctly mapped.
    assert plot.to_dict()['spec']['encoding']['x']['field'] == 'value', \
        "Plot x-axis should be mapped to value."
    assert plot.to_dict()['spec']['encoding']['y']['aggregate'] == 'count', \
        "Plot y-axis should be mapped to value after aggregating with count()."

    # Test the Exception is correctly raised when the type of `dataframe`
    # argument is wrong.
    with pytest.raises(Exception) as e:
        assert eda.describe_num_var('abc', ['N1', 'N2'])
    assert str(e.value) == "The value of the argument 'dataframe'" \
                           " should be of type pandas dataframe."

    # Test the Exception is correctly raised when the type of `num_vars`
    # argument is wrong.
    with pytest.raises(Exception) as e:
        assert eda.describe_num_var(test_data, ['N1', 1])
    assert str(e.value) == "The value of the argument 'num_vars' " \
                           "should be a list of strings."

    # Test the Exception is correctly raised when the type of `num_vars`
    # argument is wrong.
    with pytest.raises(Exception) as e:
        assert eda.describe_num_var(test_data, 'N1')
    assert str(e.value) == "The value of the argument 'num_vars' " \
                           "should be a list of strings."

    # Test the Exception is correctly raised when the elements in
    # `num_vars` argument are not unique.
    with pytest.raises(Exception) as e:
        assert eda.describe_num_var(test_data, ['N1', 'N1'])
    assert str(e.value) == "The elements in the argument 'num_vars' " \
                           "should be unique."

    # Test the Exception is correctly raised when `num_vars` argument
    # is not a subset of
    # the column names of the dataframe.
    with pytest.raises(Exception) as e:
        assert eda.describe_num_var(test_data, ['N1', 'abc'])
    assert str(e.value) == "The argument 'num_vars' should be " \
                           "a subset of the column names from the dataframe."

    # Test the Exception is correctly raised when `num_vars` argument
    # contains categorical columns of the dataframe.
    with pytest.raises(Exception) as e:
        assert eda.describe_num_var(test_data, ['N1', 'C4'])
    assert str(e.value) == "Only numeric columns expected," \
                           " please check the input."
