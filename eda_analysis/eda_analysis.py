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

def describe_cat_var(dataframe,cat_vars):
    """
    This function will take data frame and categorical variable names and will 
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
     This function takes data frame and numeric variable names and provides 
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
    dataframe: pandas.DataFrame
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