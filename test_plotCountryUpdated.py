from plotCountryUpdated import(
    # makePlots,
    listToString,
    # rollingAverage,
    # histograms,
    # boxplots
)
from collections import Counter
import pytest

from pytrends.request import TrendReq

pytrends = TrendReq(hl='en-US', tz=360)
kw_list = ["Tunisia Democracy", " hi"]  # , "Libya Democracy"
pytrends.build_payload(kw_list, cat=None, timeframe='all',
                       geo='US', gprop='')  # , cat=0 not included


# Define sets of test cases
listToString_test = [
    # Check that 1 length list is returned as string without commas
    (["Country 1"], 'Country 1'),
    # Check two countries are return with a comma and space
    (["Country 1", "Country 2"], 'Country 1, Country 2'),
    # Check three countries are return with a comma and space
    (["Country 1", "Country 2", "Country 3"], 'Country 1, Country 2, Country 3'),
    # Check four countries are return with a comma and space
    (["Country 1", "Country 2", "Country 3", "Country 4"],
     'Country 1, Country 2, Country 3, Country 4'),
    # Check five (max) countries are return with a comma and space
    (["Country 1", "Country 2", "Country 3", "Country 4", "Country 5"],
     'Country 1, Country 2, Country 3, Country 4, Country 5')
]


def function_id(fixture_value):
    """
    Get the identifier of a function name from a Pytest fixture value.
    """
    return fixture_value[0]


@pytest.fixture(params=FUNCTIONS, ids=function_id)
def implementation(request):
    """
    Get a specific implementation of a parenthesis matching checker.
    """
    return request.param


def case_id(fixture_value):
    """
    Create a test case identifier to display in Pytest output.
    """
    return f"{fixture_value[0]}-{fixture_value[1]}"


@pytest.fixture(params=listToString_test, ids=case_id)
def unit_test_case(request):
    """
    Get a specific test case identifier.
    """
    return request.param


def test_correctness(implementation, unit_test_case):  # pylint: disable=redefined-outer-name, line-too-long
    """
    Check that an implementation of parenthesis match checking passes a test
    case.
    """
    string, matches = unit_test_case
    assert implementation[1](string) == matches
