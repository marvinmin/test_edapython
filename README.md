# A Package for Exploratory Data Analysis

## Summary

Exploratory Data analysis is an important step in any data analysis. There are some general steps like describing the data, knowing `NA` values, plotting the distributions of the variables etc which are performed to understand the data well. All these tasks require a lot of coding effort. The package tries to address this issue by providing a singe function which will generate a general exploratory data analysis report. This report will contain the distribution plots of categorical and numerical variables, correlation matrix and a numerical and graphical representation to understand and identify `NA` values.

## Functions

1. `calc_cor`: This function will take in data frame and will plot correlation matrix of the features
2. `desc_na` : This function will take in data frame and will plot heat map to locate NA values in each feature and will also give a table listing number of NA values in each feature.
3. `desc_cat_var`: This function will take data frame and categorical variable names and will plot the histogram of each categorical variable
4. `desc_num_var`: This function will take data frame and numerical variable names and will plot the histogram of each numerical variable.
5. `generate_report`: This is a wrapper function which will combine all the above function to generate the report.

## Package positioning

The package helps in the EDA process of Data analysis. There are other similar package which can be used for EDA analysis. A package which does a similar thing is [pandas profiling](https://github.com/pandas-profiling/pandas-profiling). This creates an HTML report but this package will give output in the ongoing code.