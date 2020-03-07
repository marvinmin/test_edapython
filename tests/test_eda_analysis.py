from eda_analysis import eda_analysis as eda
import numpy as np
import pandas as pd
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

def test_describe_num_var():
    """
    Tests the describe_num_var function to make sure the outputs are correct.
    Returns:
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
    assert summary['N1'][0] == np.nanquantile(test_col, 0.25),\
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
    assert isinstance(plot, alt.vegalite.v3.api.FacetChart),\
    "Plot type is not an Altair object."
    assert plot.to_dict()['spec']['mark'] == 'bar',\
    "The plot should be a bar chart."
    
    # Test the axes of the plot is correctly mapped.
    assert plot.to_dict()['spec']['encoding']['x']['field'] == 'value',\
    "Plot x-axis should be mapped to value."
    assert plot.to_dict()['spec']['encoding']['y']['aggregate'] == 'count',\
    "Plot y-axis should be mapped to value after aggregating with count()."

    # Test the Exception is correctly raised when the type of `dataframe` argument is wrong.
    with pytest.raises(Exception) as e:
        assert eda.describe_num_var('abc', ['N1', 'N2'])
    assert str(e.value) == "The value of the argument 'dataframe' should be of type pandas dataframe."
    
    # Test the Exception is correctly raised when the type of `num_vars` argument is wrong.
    with pytest.raises(Exception) as e:
        assert eda.describe_num_var(test_data, ['N1', 1])
    assert str(e.value) == "The value of the argument 'num_vars' should be a list of strings."
    
    # Test the Exception is correctly raised when the type of `num_vars` argument is wrong.
    with pytest.raises(Exception) as e:
        assert eda.describe_num_var(test_data, 'N1')
    assert str(e.value) == "The value of the argument 'num_vars' should be a list of strings."
    
    # Test the Exception is correctly raised when the elements in `num_vars` argument are not unique.
    with pytest.raises(Exception) as e:
        assert eda.describe_num_var(test_data, ['N1', 'N1'])
    assert str(e.value) == "The elements in the argument 'num_vars' should be unique."
    
     # Test the Exception is correctly raised when `num_vars` argument is not a subset of 
    # the column names of the dataframe.
    with pytest.raises(Exception) as e:
        assert eda.describe_num_var(test_data, ['N1', 'abc'])
    assert str(e.value) == "The argument 'num_vars' should be a subset of the column names from the dataframe."
    
    # Test the Exception is correctly raised when `num_vars` argument contains categorical columns of the dataframe.
    with pytest.raises(Exception) as e:
        assert eda.describe_num_var(test_data, ['N1', 'C4'])
    assert str(e.value) == "Only numeric columns expected, please check the input."
