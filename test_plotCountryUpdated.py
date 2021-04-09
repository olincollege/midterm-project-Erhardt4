from plotCountryUpdated import(
    # makePlots,
    readCSV,
    listToString,
    csvName,
    # rollingAverage,
    # histograms,
    # boxplots
    
    
)
from collections import Counter
import pytest
from pytrends.request import TrendReq
import pandas as pd

# readCSV preparation
kw_list = ["Tunisia Democracy"]  
data = pd.read_csv('pytrends_Data/'+csvName(kw_list)+'.csv')

readCSV_cases = [(kw_list, data)]
# Define sets of test cases
listToString_cases = [
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

csvName_cases = [
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

@pytest.mark.parametrize("countryList, countryString", listToString_cases)
def test_listToString(countryList, countryString):
    assert listToString(countryList) == countryString
    
@pytest.mark.parametrize("countryList, countryString", csvName_cases)
def test_csvName(countryList, countryString):
    assert csvName(countryList) == countryString
@pytest.mark.parametrize("countryList, countryString", csvName_cases)
def test_csvName(countryList, countryString):
    assert csvName(countryList) == countryString
@pytest.mark.parametrize("functionData, data", readCSV_cases)
def test_csvName(functionData, data):
    # Receiving data from google to test readCSV function once. Done so to not ping
    # Google constantly. No other way to construct the dataframe other than using
    # the readCSV function, which would defeat the purpose of the test. 
    assert readCSV(functionData).equals(data)
