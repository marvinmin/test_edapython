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


def test_describe_cat_var():
    #Calling helper function to create data
    data = helper_create_data()
    cat_vars = ['C1','C2','C3','C4']
    #Testing data frame exception
    x = [1,2,3]
    try:
        eda.describe_cat_var(x,cat_vars)
        assert False,'Exception must be thorwn for this test case'
    except Exception as ex:
        assert "The value of the argument 'dataframe' must be of type 'pandas.DataFrame'" == str(ex), 'Expected exception not thrown'
    
    #Testing categorical variable exception
    try:
        eda.describe_cat_var(data,x)
        assert False,'Exception must be thorwn for this test case'
    except Exception as ex:
        assert "The value of the argument 'cat_vars' must be a list of strings" == str(ex), 'Expected exception not thrown'
    
    #Testing columns subset exception
    try:
        cols = ['Y1','Y2']
        eda.describe_cat_var(data,cols)
        assert False,'Exception must be thorwn for this test case'
    except Exception as ex:
        assert "The input categorical column names must belong to the dataframe" == str(ex), 'Expected exception not thrown'
    
    #Testing type of returned value
    p = eda.describe_cat_var(data,cat_vars)
    assert isinstance(p,alt.vegalite.v3.api.VConcatChart),'The function must return an altair plot'
    
    #Testing if the specified columns has been plotted or not
    p = eda.describe_cat_var(data,cat_vars)
    assert list(p.data.columns) == cat_vars, 'The specified categorical columns were not plotted'
    


