
import pandas as pd
import numpy as np
import altair as alt

"""Perform EDA analysis of the given DataFrame"""

def generate_report(dataframe,cat_vars,num_vars):
    """
    This function generates an EDA report by plotting graphs and tables for the 
    numeric variables, categorical variables, NA values and correlation in a dataframe
    
    Parameters:
    -----------
    dataframe: pandas.DataFrame
        The dataframe whose EDA analysis is to be performed
    cat_vars: list
        A list containing names of categorical variables
    num_vars: list
        A list containing names of numerical variable
        
    Returns:
    --------
    boolean
        It returns True on successful execution else returns False
        
    Examples:
    ---------
    >>> X= pandas.DataFrame({
    'type':['Car','Bus','Car']
    'height':[10,20,30]
    })
    >>>cat_vars = ['type']
    >>>num_vars = ['height']
    >>> describe_cat_variable(X,cat_vars,num_vars)
    
    """
    
    
def describe_na_values(dataframe):
    '''
    describes the na_values in an input pandas dataframe as a 2d array of 1's and 0's.

    Parameters
    ----------
    dataframe: Pandas.DataFrame
        the input pd.DataFrame object.

    Returns
    -------
    numpy.ndarray
        A 2d Numpy Array of 1's and 0's, corresponding to the value of each entry in the dataframe.
        0 represents an NA value, 1 represents a non-NA value.
    '''
    pass    

  
def describe_cat_var(dataframe,cat_vars):
    """
    This function will take dataframe and categorical variable names and will 
    plot the histogram of each categorical variable.
    
    Parameters:
    -----------
    dataframe: pandas.DataFrame
        The dataframe whose EDA analysis is to be performed
    cat_vars: list
        A list containing names of categorical variables
    
    Returns:
    --------
    altair
        a grid of altair plot containing all histograms
    
    Examples:
    ---------
    >>> X= pandas.DataFrame({
    'type':['Car','Bus','Car']
    'height':[10,20,30]
    })
    >>> cat_vars = ['type']
    >>> describe_cat_variable(X,cat_vars)
       
    """
    # Code 
    
    
def describe_num_var(dataframe, num_vars):
    """ 
    This function takes dataframe and numeric variable names and provides 
    statistical summary of the numeric variables for a dataframe.
    Also, the function plots the histogram of each numeric variable.

    Parameters:
    -----------
    dataframe: pandas.DataFrame
        The dataframe to be inspected.
    num_vars: list
        A list of character strings of the names of the numeric variables.
    
    Returns:
    --------
    tuple(pandas.DataFrame, altair)
        pandas.DataFrame
            statistical summary of the numeric variables
        altair
            a grid of altair plot containing all histograms
    
    Examples:
    ---------
    >>> X= pandas.DataFrame({
    'type':['Car', 'Bus', 'Car']
    'height':[10, 20, 30]
    })
    >>> num_vars = ['type']
    >>> describe_num_var(X, num_vars)
      
    """
    # Code


def calc_cor(dataframe, num_var):
    """
    This function evaluates the correlation between the numeric 
    variables of a given dataframe.


	Parameters:
    -----------
    dataframe: pandas.DataFrame
        The data frame whose EDA analysis is to be performed.
    num_var: list
        A list of strings of column names containing numeric variables.

    Returns:
    --------
    altair
        A correlogram plot labelled with the correlation coefficients 
        of -1 to 1 between each numeric column and other numeric variables
        in the dataframe.

    Examples:
    ---------
    >>> X= pandas.DataFrame({
    'type':['Car','Bus','Car']
    'width':[40, 10, 5]
    'height':[10,20,30]
    })
    >>>num_var = ['height', 'width']
    >>> calc_cor(X, num_vars)    
    """
    # Test input 'dataframe' is a dataframe
    assert isinstance(dataframe, pd.DataFrame), "Input 'dataframe' is not a dataframe"
    
    df_num = dataframe.loc[:, num_var]
    df_num = df_num.dropna()
    
    for i in num_var:
        assert np.issubdtype(dataframe[i].dtype, np.number), "Columns are not all numeric"

    df_corr = round(df_num.corr(method='pearson'), 2)
    
    # Code adapted from https://github.com/altair-viz/altair/pull/1945/files
    corr_list = sorted(df_corr.columns.to_list())
    corr_list_copy = corr_list.copy()
    rows = []
    
    # Format the data to make a lower triangle correlation maxtix
    for i in corr_list:
        for j in corr_list_copy:
            rows.append([i,j, df_num.corr().loc[i,j]])
        corr_list_copy.remove(i)

    # Create dataframe from list of rows
    new_df = pd.DataFrame(rows, columns=['Var1','Var2','Corr'])

    # Create the rectangle heatmap as the base with text layer
    heatmap = alt.Chart(new_df).mark_rect().encode(
        alt.X('Var1:O'),
        alt.Y('Var2:O', axis=alt.Axis(labelAngle=0)),
        alt.Color('Corr:Q', legend=alt.Legend(direction='horizontal'))
    ).properties(width = 400, height = 400, title = "Correlation matrix")

    text = heatmap.mark_text(baseline='middle', fontSize=20).encode(
        text=alt.Text('Corr:Q', format='.2'),
        color=alt.condition(
            alt.datum.Corr <= 0.2,
            alt.value('black'),
            alt.value('white')
        )
    )

    corr_chart = heatmap + text

    return corr_chart