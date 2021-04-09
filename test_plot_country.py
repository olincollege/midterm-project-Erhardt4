"""
docstring
"""
import pytest
import pandas as pd
from plot_country import(
    read_csv,
    csv_name,
    list_to_string,
)

# read_csv preparation solutions
kw_list = ["Tunisia Democracy"]
data = pd.read_csv('pytrends_data/'+csv_name(kw_list)+'.csv')

# Define sets of test cases
read_csv_cases = [(kw_list, data)]

# Define sets of test cases
list_to_string_cases = [
    # Check that 1 length list is returned as string without commas
    (["Country 1"], 'Country 1'),
    # Check two countries are returned with a comma and space
    (["Country 1", "Country 2"], 'Country 1, Country 2'),
    # Check three countries are returned with a comma and space
    (["Country 1", "Country 2", "Country 3"], 'Country 1, Country 2, Country 3'),
    # Check four countries are returned with a comma and space
    (["Country 1", "Country 2", "Country 3", "Country 4"],
     'Country 1, Country 2, Country 3, Country 4'),
    # Check five (max) countries are returned with a comma and space
    (["Country 1", "Country 2", "Country 3", "Country 4", "Country 5"],
     'Country 1, Country 2, Country 3, Country 4, Country 5')
]

# Define sets of test cases
csv_name_cases = [
    # Check that 1 length list is returned as string without spaces
    (["Country 1"], 'Country1'),
    # Check two countries are returned with no spaces, '_' between indexes
    (["Country 1", "Country 2"], 'Country1_Country2'),
    # Check three countries are returned with no spaces, '_' between indexes
    (["Country 1", "Country 2", "Country 3"],
     'Country1_Country2_Country3'),
    # Check four countries are returned with no spaces, '_' between indexes
    (["Country 1", "Country 2", "Country 3", "Country 4"],
     'Country1_Country2_Country3_Country4'),
    # Check five countries are returned with no spaces, '_' between indexes
    (["Country 1", "Country 2", "Country 3", "Country 4", "Country 5"],
     'Country1_Country2_Country3_Country4_Country5')
]

@pytest.mark.parametrize("country_list, country_string", list_to_string_cases)
def test_list_to_string(country_list, country_string):
    """
    docstring
    """
    assert list_to_string(country_list) == country_string
@pytest.mark.parametrize("country_list, country_string", csv_name_cases)
def test_csv_name(country_list, country_string):
    """
    docstring
    """
    assert csv_name(country_list) == country_string
@pytest.mark.parametrize("function_data, data_sol", read_csv_cases)
def test_read_csv_cases(function_data, data_sol):
    """
    Receiving data from google to test read_csv function once. Done so to not ping
    Google constantly. No other way to construct the dataframe other than using
    the read_csv function, which would defeat the purpose of the test.
    """
    assert read_csv(function_data).equals(data_sol)
