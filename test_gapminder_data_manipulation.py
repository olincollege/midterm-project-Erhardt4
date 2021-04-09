"""
Library for testing gapminder_data_manipulation.py
through pytest.
"""
import pytest
import pandas
from gapminder_data_manipulation import(
    create_data_frame,
    get_specific_countries_data,
    get_country_name_list,
    get_year_list,
    get_greatest_variance_countries,
    get_rates,
)

# Dataframe of EIU_democracy_index.csv
democracy_index_data = pandas.read_csv("EIU_Democracy_Index.csv")

# Define sets of test cases

create_data_frame_cases = [
    # Check that the downloaded data is properly imported as a pandas dataframe
    ("EIU_Democracy_Index.csv", pandas.read_csv("EIU_Democracy_Index.csv")),
]
get_specific_countries_data_cases = [
    #Check that the data of a specific country is properly gotten
    ([pandas.read_csv("EIU_Democracy_Index.csv"),[1]],
     {"Albania": democracy_index_data.iloc[1, 1:14]}),
    #Check that the data of a two countries are properly gotten
    ([pandas.read_csv("EIU_Democracy_Index.csv"),[1,5]],
     {"Albania": democracy_index_data.iloc[1, 1:14],
      "Armenia": democracy_index_data.iloc[5, 1:14]}),
    #Check that the data of several countries country are properly gotten
    ([pandas.read_csv("EIU_Democracy_Index.csv"),[1,50,100,150]],
     {"Albania": democracy_index_data.iloc[1, 1:14],
      "Ethiopia": democracy_index_data.iloc[50, 1:14],
      "Morocco":  democracy_index_data.iloc[100, 1:14],
      "Turkey": democracy_index_data.iloc[150, 1:14]}),
]

get_country_name_list_cases = [
    #Check that the correct country list is generated
    ("EIU_Democracy_Index.csv",['Afghanistan', 'Albania', 'Algeria','Angola',
                                'Argentina', 'Armenia', 'Australia', 'Austria',
                                'Azerbaijan', 'Bahrain', 'Bangladesh', 'Belarus',
                                'Belgium', 'Benin', 'Bhutan', 'Bolivia',
                                'Bosnia and Herzegovina', 'Botswana', 'Brazil',
                                'Bulgaria', 'Burkina Faso', 'Burundi', 'Cambodia',
                                'Cameroon', 'Canada', 'Cape Verde', 'Central African Republic',
                                'Chad', 'Chile', 'China', 'Colombia', 'Comoros',
                                'Congo, Dem. Rep.', 'Congo, Rep.', 'Costa Rica',
                                "Cote d'Ivoire", 'Croatia', 'Cuba', 'Cyprus',
                                'Czech Republic', 'Denmark', 'Djibouti',
                                'Dominican Republic', 'Ecuador', 'Egypt',
                                'El Salvador', 'Equatorial Guinea', 'Eritrea',
                                'Estonia', 'Eswatini', 'Ethiopia', 'Fiji',
                                'Finland', 'France', 'Gabon', 'Gambia',
                                'Germany', 'Ghana', 'Greece', 'Guatemala',
                                'Guinea', 'Guinea-Bissau', 'Guyana', 'Haiti',
                                'Honduras', 'Hungary', 'Iceland', 'India',
                                'Indonesia', 'Iran', 'Iraq', 'Ireland', 'Israel',
                                'Italy', 'Jamaica', 'Japan', 'Jordan', 'Kazakhstan',
                                'Kenya', 'Kuwait', 'Kyrgyz Republic', 'Lao',
                                'Latvia', 'Lebanon', 'Lesotho', 'Liberia', 'Libya',
                                'Lithuania', 'Luxembourg', 'Madagascar', 'Malawi',
                                'Malaysia', 'Mali', 'Malta', 'Mauritania',
                                'Mauritius', 'Mexico', 'Moldova', 'Mongolia',
                                'Montenegro', 'Morocco', 'Mozambique', 'Myanmar',
                                'Namibia', 'Nepal', 'Netherlands', 'New Zealand',
                                'Nicaragua', 'Niger', 'Nigeria', 'North Korea',
                                'North Macedonia', 'Norway', 'Oman', 'Pakistan',
                                'Palestine', 'Panama', 'Papua New Guinea', 'Paraguay',
                                'Peru', 'Philippines', 'Poland', 'Portugal', 'Qatar',
                                'Romania', 'Russia', 'Rwanda', 'Saudi Arabia',
                                'Senegal', 'Serbia', 'Sierra Leone', 'Singapore',
                                'Slovak Republic', 'Slovenia', 'South Africa',
                                'South Korea', 'Spain', 'Sri Lanka', 'Sudan',
                                'Suriname', 'Sweden', 'Switzerland', 'Syria',
                                'Tajikistan', 'Tanzania', 'Thailand', 'Timor-Leste',
                                'Togo', 'Trinidad and Tobago', 'Tunisia', 'Turkey',
                                'Turkmenistan', 'Uganda', 'Ukraine',
                                'United Arab Emirates', 'United Kingdom', 'United States',
                                'Uruguay', 'Uzbekistan', 'Venezuela', 'Vietnam',
                                'Yemen', 'Zambia', 'Zimbabwe'])
]

get_year_list_cases = [
    #Check that the correct year list is generated
    ("EIU_Democracy_Index.csv",
     [2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018]),
]

get_greatest_variance_countries_cases = [
    #Check that a typical threshold returns the correct country list
    (0.05,[14, 21, 51, 55, 57, 86, 89, 101, 102, 104, 107, 115, 125, 145, 147, 149, 153, 159]),
    #Check that a threshold below every country returns the full country list
    (0,[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23,
        24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44,
        45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65,
        66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86,
        87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106,
        107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123,
        124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140,
        141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157,
        158, 159, 160, 161, 162, 163]),
    #Check that threshold with no countries above it returns an emptry list
    (1,[]),
]

get_rates_cases = [
    #Check an empty list of countries
    ([],{}),
    #Check a list of one country results in the correct rate data
    ([1], {"Albania": [0.0, 0.0, -0.33840947546531336, -0.5093378607809852,
                       -0.8532423208191133, -2.409638554216851, 0.0, 0.0,
                       4.232804232804217, 0.0, 1.1844331641285966, 0.0]}),
    #Check a list of several country results in the correct rate data
    ([1, 50, 100, 150], {"Albania": [0.0, 0.0, -0.33840947546531336,
                                     -0.5093378607809852, -0.8532423208191133, -2.409638554216851,
                                     0.0, 0.0, 4.232804232804217, 0.0, 1.1844331641285966, 0.0],
                         "Ethiopia": [-2.1186440677966116, -2.1645021645021667, -9.292035398230096,
                                      -10.243902439024387, 2.9891304347826115, -1.84696569920843,
                                      2.9569892473118005, -2.8720626631853525, 2.9569892473118005,
                                      -6.005221932114875, -4.999999999999989, -2.046783625730996],
                         'Morocco': [-0.2564102564102566, -0.2570694087403744, -1.0309278350515332,
                                     -1.3020833333333344, 1.0554089709762395, 6.2663185378590285,
                                     0.0, -1.7199017199017212, 16.5, 2.3605150214592294,
                                     2.0964360587002115, 2.464065708418882],
                         'Turkey': [0.0, -0.17543859649122825, 0.3514938488576648,
                                    0.3502626970227479, 0.0, 0.5235602094241036,
                                    -2.2569444444444655, -9.05861456483125, 0.0,
                                    -1.5625000000000013, -3.174603174603177, -10.450819672131134]}),
]
@pytest.mark.parametrize("filename, dataframe", create_data_frame_cases)
def test_create_data_frame(filename, dataframe):
    """
    Test that the create_data_frame function properly creates a dataframe.

    Args:
        filename: A string representing the name of the file being
                  converted to a dataframe.
        dataframe: A dataframe representing the expected output of
                   the create_data_frame function.
    """
    assert create_data_frame(filename).equals(dataframe)

@pytest.mark.parametrize("country_list, data", get_specific_countries_data_cases)
def test_get_specific_countries_data(country_list, data):
    """
    Test that the get_specific_countries_data function properly returns
    the correct data of the correct country.

    Args:
        country_list: A list containing country index numbers.
        data: A dictionary representing the expected output of the
              getspecific_countries_data function.
    """
    is_equal = 0
    specific_countries_data = get_specific_countries_data(country_list[0], country_list[1])
    for key in specific_countries_data:
        if not (key in data and specific_countries_data[key].equals(data[key])):
            is_equal = 1
    assert is_equal == 0

@pytest.mark.parametrize("filename, country_list", get_country_name_list_cases)
def test_get_country_name_list(filename, country_list):
    """
    Test that the get_country_name_list function properly returns the
    correct country name list.

    Args:
        filename: A string representing the name of the file the
                  data is being taken from.
        country_list: A list representing the expected output of
                     the get_country_name_list function.
    """
    assert get_country_name_list(filename) == country_list

@pytest.mark.parametrize("filename, year_list", get_year_list_cases)
def test_get_year_list(filename, year_list):
    """
    Test that the get_year_list function properly returns the
    correct year list.

    Args:
        filename: A string representing the name of the file the
                  data is being taken from.
        year_list: A list representing the expected output of
                     the get_year_list function.
    """
    assert get_year_list(filename) == year_list

@pytest.mark.parametrize("threshold, country_list", get_greatest_variance_countries_cases)
def test_get_greatest_variance_countries(threshold, country_list):
    """
     Test that the get_greatest_variance_countries function properly
     returns the correct country list.

     Args:
        threshold: An integer representing the value of the
                   threshold used to filter out countries.
        country_list: A list representing the expected output of
                     the get_greatest_variance_counties function.
    """
    assert get_greatest_variance_countries(threshold) == country_list

@pytest.mark.parametrize("country_list, rate_data", get_rates_cases)
def test_get_rates(country_list, rate_data):
    """
    Test that the get_rates function properly returns the correct
    rate data.

    Args:
        country_list: A list of country indexes representing the
                     countries that rate data is wanted.
        rate_data: A dictionary representing the expected output
                  of the get_rates function.
    """
    assert get_rates(country_list) == rate_data
