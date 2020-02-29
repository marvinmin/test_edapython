# A Package for Exploratory Data Analysis

## Summary

Exploratory Data analysis is an important step in any data analysis. There are some general steps like describing the data, knowing `NA` values, plotting the distributions of the variables etc which are performed to understand the data well. All these tasks require a lot of coding effort. The package tries to address this issue by providing a singe function which will generate a general exploratory data analysis report. This report will contain the distribution plots of categorical and numerical variables, correlation matrix and a numerical and graphical representation to understand and identify `NA` values.

## Functions

1. `calc_cor`: This function will take in data frame and will plot correlation matrix of the features
2. `describe_na_values` : This function will take in data frame and will plot heat map to locate NA values in each feature and will also give a table listing number of NA values in each feature.
3. `describe_cat_var`: This function will take data frame and categorical variable names and will plot the histogram of each categorical variable
4. `describe_num_var`: This function will take data frame and numerical variable names and will plot the histogram of each numerical variable.
5. `generate_report`: This is a wrapper function which generates an EDA report by plotting graphs and tables for the numeric variables, categorical variables, NA values and correlation in a dataframe

## Package positioning

The package helps in the EDA process of Data analysis. There are other similar package which can be used for EDA analysis. A package which does a similar thing is [pandas profiling](https://github.com/pandas-profiling/pandas-profiling). This creates an HTML report but this package will give output in the ongoing code.


## eda_analysis 

![](https://github.com/sweber15/eda_analysis/workflows/build/badge.svg) [![codecov](https://codecov.io/gh/sweber15/eda_analysis/branch/master/graph/badge.svg)](https://codecov.io/gh/sweber15/eda_analysis) ![Release](https://github.com/sweber15/eda_analysis/workflows/Release/badge.svg)

[![Documentation Status](https://readthedocs.org/projects/eda_analysis/badge/?version=latest)](https://eda_analysis.readthedocs.io/en/latest/?badge=latest)

Conduct initial EDA for exploring ddata in a dataframe.

### Installation:

```
pip install -i https://test.pypi.org/simple/ eda_analysis
```

### Features
- TODO

### Dependencies

- TODO

### Usage

- TODO

### Documentation
The official documentation is hosted on Read the Docs: <https://eda_analysis.readthedocs.io/en/latest/>

### Credits
This package was created with Cookiecutter and the UBC-MDS/cookiecutter-ubc-mds project template, modified from the [pyOpenSci/cookiecutter-pyopensci](https://github.com/pyOpenSci/cookiecutter-pyopensci) project template and the [audreyr/cookiecutter-pypackage](https://github.com/audreyr/cookiecutter-pypackage).

