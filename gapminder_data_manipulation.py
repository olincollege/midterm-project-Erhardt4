"""
Functions for accessing, manipulating, and plotting
EIU Democracy Index Data
"""

import statistics
import csv
import pandas
import matplotlib.pyplot as plt


def create_data_frame(filename):
    """
    Create a a pandas dataframe from a ,csv.

    Args:
        filename: A string representing the name of the
                  .csv file containing the data.
    Returns:
        A pandas dataframe of the data in the file.
    """
    dataframe = pandas.read_csv(filename)
    return dataframe


def get_specific_countries_data(dataframe, country_list):
    """
    Gets the EIU Index Data of specific countries.

    Args:
        datarame: A pandas dataframe containing the EIU Democracy
                  Index values of each of the countries
        country_list: A list containing country indexes of the countries
                     which data is needed.
    Returns:
        A dictionary containing the country name as the key and a pandas
        dataframe containing the EIU Index values of the specific country
        as the value.
    """
    data = {}
    country_name_list = get_country_name_list("EIU_Democracy_Index.csv")
    for index in country_list:
        data[country_name_list[index]] = dataframe.iloc[index, 1:14]
    return data


def get_country_name_list(filename):
    """
    Generates a list of all the country names.

    Args:
        filename: A string representing the name of the file which the
                  data is being accessed.
    Returns:
        A list of strings containing each country's name.plot_c
    """
    read = csv.reader(open(filename, "r"))
    country_list = []
    for row in read:
        country_list.append(row[0])
    return country_list[1:]


def get_year_list(filename):
    """
    Generates a list of all the years.

    Args:
        filename: A string representing the name of the file which the
                  data is being accessed.
    Returns:
        A list of integers containing all the years the data is from.
    """
    read = csv.reader(open(filename, "r"))
    counter = True
    for row in read:
        if counter:
            year_list = row[1:]
            counter = False
    for count, value in enumerate(year_list):
        year_list[count] = int(value)
    return year_list


def get_greatest_variance_countries(threshold):
    """
    Gets countries whose variance is above a certain threshold.

    Args:
        threshold: An integer representing the threshold of the
                   countries EIU Index data variance.
    Returns:
        A list containing country indexes of countries which
        variances are above the threshold.
    """
    countries_above_threshold = []
    dataframe = create_data_frame("EIU_Democracy_Index.csv")
    for i in range(164):
        data = dataframe.iloc[i, 1:14]
        if statistics.pstdev(data) > threshold:
            countries_above_threshold.append(i)
    return countries_above_threshold


def plot_data(data):
    """
    Plots a line graph of given data.

    Args:
        data: a dictionary of pandas dataframes as keys or a
              single pandas dataframe containing the data that
              needs to be plotted.
    """
    plt.figure()
    year_list = get_year_list("EIU_Democracy_Index.csv")
    for element in data:
        plt.plot(year_list, data[element], marker='+')

    plt.xlabel("Years")
    plt.ylabel("EIU Democracy Index Value")
    plt.xlim(2006, 2020)
    plt.ylim(0, 1)
    plt.legend(data.keys(), loc='best')
    plt.title("EIU Democracy Index Value Over Time")


def plot_chosen_countries(country_list):
    """
    Plots a line graph of the EIU Indexes of specific countries.

    Args:
        country_list: A list of country indexes of countries that
                     need to be plotted.
    """
    dataframe = create_data_frame("EIU_Democracy_Index.csv")
    data = get_specific_countries_data(dataframe, country_list)
    plot_data(data)


def get_rates(country_list):
    """
    Gets the rates of changes of the EIU Index Values of a list
    of countries.

    Args:
        country_list: A list of country indexes of countries that
                     need rates.
    Returns:
        A dictionary containing the country name as the key and a pandas
        dataframe containing the rate of change of EIU Index values as a
        percent of the specific country as the value.
    """
    dataframe = create_data_frame("EIU_Democracy_Index.csv")
    data = get_specific_countries_data(dataframe, country_list)
    rates = {}
    for key in data:
        value = []
        for i in range(len(data[key])-1):
            value.append(((data[key][i+1]-data[key][i])/data[key][i])*100)
        rates[key] = value
    return rates


def plot_rates(data):
    """
    Plots a line graph of the rate of changes of EIU Indexes of
    specific countries.

    Args:
        data: a dictionary of pandas dataframes as keys or a
              single pandas dataframe containing the rate data
              that needs to be plotted.
    """
    plt.figure()
    year_list = get_year_list("EIU_Democracy_Index.csv")
    year_list = year_list[1:]
    for element in data:
        plt.plot(year_list, data[element], marker='+')
    plt.xlabel("Years")
    plt.ylabel("Rate of Change of EIU Index Value (%)")
    plt.xlim(2006, 2020)
    # plt.ylim(-90,110)
    plt.legend(data.keys(), loc='best')
    plt.title("Rate of Change of EIU Democracy Index Value Over Time")


def plot_rate_chosen_countries(country_list):
    """
    Plots a line graph of the rate of change of EIU Indexes of
    specific countries.

    Args:
        country_list: A list of country indexes of countries that
                     need to be plotted.
    """
    rates = get_rates(country_list)
    plot_rates(rates)


def plot_histogram(year_index):
    """
    Plots a histogram of the EIU Index Values of all countries
    in a given year.

    Args:
        year_index: An integer representing the year of the indexes
                   that need to be plotted.
    """
    dataframe = create_data_frame("EIU_Democracy_Index.csv")
    all_countries = range(0, 164)
    all_data = get_specific_countries_data(dataframe, all_countries)
    data = []
    for element in all_data:
        data.append(all_data[element][year_index])
    plt.figure()
    plt.hist(data)
    plt.xlabel("EIU Index Scores")
    plt.ylabel("Frequency")


def plot_histogram_all_years():
    """
    Plots a histogram of the EIU Index Value of all countries
    for each year there is data for.
    """
    _, axs = plt.subplots(5, 3, sharey='row', figsize=(20, 30))
    dataframe = create_data_frame("EIU_Democracy_Index.csv")
    all_countries = range(0, 164)
    all_data = get_specific_countries_data(dataframe, all_countries)
    for i in range(13):
        data = []
        for element in all_data:
            data.append(all_data[element][i])
        axes = axs[i//3, i % 3]
        axes.hist(data, bins=20, color='blue', alpha=0.75)
        axes.set_xlabel("EIU Index")
        axes.set_ylabel("Frequency")
        axes.set_title(f"EIU Index of Each Country in {i+2006}")


def plot_histogram_all_data():
    """
    Plots a histogram of the EIU Index Value of all the countries
    for all the years there is data for.
    """
    dataframe = create_data_frame("EIU_Democracy_Index.csv")
    all_countries = range(0, 164)
    all_data = get_specific_countries_data(dataframe, all_countries)
    data = []
    for element in all_data:
        for i in range(13):
            data.append(all_data[element][i])
    plt.figure()
    plt.hist(data, bins=20, color='blue')
    plt.xlabel("EIU Index Scores")
    plt.ylabel("Frequency")
    plt.title("EIU Index of Each Country")
