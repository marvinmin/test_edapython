import numpy as np
import pandas as pd

"""Perform EDA analysis of the given DataFrame"""


def generate_report(dataframe, cat_vars, num_vars):
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


def describe_na_values(dataframe: pd.DataFrame):
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
    Examples:
    ---------
    >>> no_na_dataframe = pd.DataFrame({
                                    "col_1": [0, 2],
                                    "col_2": [0.5, 0.1],
                                    "col_3": ["a", "b"]
                                    })
    >>> describe_na_variable(no_na_dataframe)
    numpy.ndarray([1, 1],
                  [1, 1],
                  [1, 1])

    >>>  na_numerical_dataframe = pd.DataFrame({
                                           "col_1": [0, 2],
                                           "col_2": [numpy.nan, 0.1],
                                           "col_3": ["a", "b"]
                                           }),
    >>> describe_na_variable(na_numerical_dataframe)
    numpy.ndarray([1, 1],
                  [0, 1],
                  [1, 1])
    >>>  na_categorical_dataframe = pd.DataFrame({
                                           "col_1": [0, 2],
                                           "col_2": [0.5, 0.1],
                                           "col_3": [np.nan, "b"]
                                           }),
    >>> describe_na_variable(na_numerical_dataframe)
    numpy.ndarray([1, 1],
                  [1, 1],
                  [0, 1])

    '''
    bool_array = dataframe.isna()
    return np.array([[0 if val else 1 for val in bool_array[col]] for col in bool_array.columns])


def describe_cat_var(dataframe, cat_vars):
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

