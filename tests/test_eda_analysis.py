from eda_analysis import eda_analysis as eda
import numpy as np
import pandas as pd
import altair as alt
import pytest

def helper_create_data(n = 500):
    """
    Helper function for creating dataframe for testing
    
    Parameters:
    -----------
    n: int (default value = 500)
        Number of rows to be generated for the dataframe
    
    Returns:
    --------
    pandas.DataFrame
        Returns a dataframe to be used for testing
        
    Examples:
    ---------
    >>> helper_create_data()
    """
    N1 = list(np.random.exponential(3,n))
    N2 = list(np.random.normal(2,2,n))
    N3 = list(np.random.normal(10,3,n))
    C1 = list(np.random.binomial(1,0.7,n))
    C2 = list(np.random.poisson(1,n))
    C3 = list(np.random.binomial(5,0.4,n))
    a = ['cat','dog','lion']
    C4 = list(np.random.choice(a,n))
    df = pd.DataFrame({
        'C1':C1,
        'C2':C2,
        'C3':C3,
        'N1':N1,
        'N2':N2,
        'N3':N3, 
        'C4':C4
    })

    rows = list(np.random.randint(0,n,20))
    cols = list(np.random.randint(0,7,5))
    df.iloc[rows,cols] = np.nan

    return df

def test_calc_cor():
    """
    Tests the corrleation function calc_cor to make sure the outputs are correctly rendering.

    Returns:
    --------
    None
        The test should pass and no asserts should be displayed. 
    """
    data = helper_create_data()
    num_vars = ["N1", "N2", "N3"]
    chart = eda.calc_cor(data, num_vars)
    
    # Check the data in the correlation matrix to be between -1 and 1
    for i in range(0, len(chart.data)):
        assert chart.data.iloc[i, 2] >= -1, "Out of range values: lower than -1"
        assert chart.data.iloc[i, 2] <= 1, "Out of range values: higher than 1"
    
    # Tests if the first and last value is 1 since it correlates to itself
    assert chart.data.iloc[0, 2] == 1, "The first value should be 1 because it is correlated to itself"
    assert chart.data.iloc[-1, 2] == 1, "The last value should be 1 because it is correlated to itself"
    
    # Test that Var1 and Var2 are equal in the first and last row
    assert chart.data.iloc[0, 0] == chart.data.iloc[0, 1], "The Var1 should equal Var2 in the first row"
    assert chart.data.iloc[-1, 0] == chart.data.iloc[-1, 1], "The Var1 should equal Var2 in the last row"
    
    # Test if the axes are properly mapped to the correct field
    spec = chart.to_dict()
    assert spec["layer"][1]["encoding"]["x"]["field"] == 'Var1', "Plot x-axis should be mapped to Var1"
    assert spec["layer"][1]["encoding"]["y"]["field"] == 'Var2', "Plot y-axis should be mapped to Var2"
    
    # Tests if the plot type is correct
    assert "altair" in str(type(chart)), "Plot type is not an Altair object"
    
    # Tests the exception is correctly raised when columns are not numeric
    with pytest.raises(Exception) as e:
        assert eda.calc_cor(data, ["C4"])
    assert str(e.value) == "Columns are not all numeric"
    
    # Tests the exception is correctly raised when 'columns are not numeric 'dataframe' 
    # is not the correct type.
    with pytest.raises(Exception) as e:
        assert eda.calc_cor(["N1"], ["N1"])
    assert str(e.value) == "Input 'dataframe' is not a dataframe"

    # Tests the exception is correctly raised when 'num_vars' is not a string.
    with pytest.raises(Exception) as e:
        assert eda.calc_cor(data, ['N1', 1])
    assert str(e.value) == "The value of the argument 'num_vars' should be a list of strings."
    
    # Tests the exception is correctly raised when 'num_vars' is not a string
    with pytest.raises(Exception) as e:
        assert eda.calc_cor(data, 'N1')
    assert str(e.value) == "The value of the argument 'num_vars' should be a list of strings."

    # Tests the exception is correctly raised when elements in 'num_vars' are not unique.
    with pytest.raises(Exception) as e:
        assert eda.calc_cor(data, ['N1', 'N1'])
    assert str(e.value) == "The elements in the argument 'num_vars' should be unique."

    # Test the Exception is correctly raised when 'num_vars' argument is not a subset of 
    # the column names of the dataframe
    with pytest.raises(Exception) as e:
        assert eda.calc_cor(data, ["N1", "abc"])
    assert str(e.value) == "The argument 'num_vars' should be a subset of the column names from the dataframe."
