from eda_analysis import eda_analysis
import pytest

def test_calc_cor():
    """
    Tests the corrleation function calc_cor to make sure the outputs are correctly rendering.

    Returns:
    --------
    None
        The test should pass and no asserts should be displayed. 
    """
    data = create_data()
    num_var = ["N1", "N2", "N3"]
    chart = calc_cor(data, num_var)
    
    for i in range(0, len(chart.data)):
        assert chart.data.iloc[i, 2] >= -1, "Out of range values: lower than -1"
        assert chart.data.iloc[i, 2] <= 1, "Out of range values: higher than 1"
        
    assert chart.data.iloc[0, 2] == 1, "The first value should be 1 because it is correlated to itself"
    assert chart.data.iloc[0, 0] == chart.data.iloc[0, 1], "The Var1 should equal Var2 in the first row"
    assert chart.data.iloc[-1, 2] == 1, "The last value should be 1 because it is correlated to itself"
    assert chart.data.iloc[-1, 0] == chart.data.iloc[-1, 1], "The Var1 should equal Var2 in the last row"
    
    spec = chart.to_dict()
    assert spec["layer"][1]["encoding"]["x"]["field"] == 'Var1', "Plot x-axis should be mapped to Var1"
    assert spec["layer"][1]["encoding"]["y"]["field"] == 'Var2', "Plot y-axis should be mapped to Var2"
    
    assert "altair" in str(type(chart)), "Plot type is not an Altair object"
    
    with pytest.raises(AssertionError, match="Columns are not all numeric"):
        assert calc_cor(data, ["C1"]), "No error thrown for categorical variables"
        
    with pytest.raises(AssertionError, match="Input 'df' is not a dataframe"):
        assert calc_cor(["N1"], ["N1"]), "No error thrown for non-dataframe input"