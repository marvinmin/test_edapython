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