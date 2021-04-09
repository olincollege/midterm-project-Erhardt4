"""
This file does all the Pytrend analysis,
"""
from os import path
from pytrends.request import TrendReq
import pandas as pd
import matplotlib.pyplot as plt
import pylab as pl

pytrends = TrendReq(hl='en-US', tz=360)

def make_csv(country_list):
    """
    This function makes a csv in the 'pytrends_data' folder with an
    identifiable name of the csv based on the country_list. By having
    the country list, we can construct a data frame and save it. This
    reduces the number of times needed to ping Google.

    Args:
        country_list: A list of the country search terms

    Returns:
        No returns, makes a csv in folder 'pytrends_data' that saves a
        dataframe of interest over time.
    """
    pytrends.build_payload(country_list, cat=0, timeframe='2006-1-1 2019-01-1',
                           geo='US', gprop='')
    data = pytrends.interest_over_time()
    data = data[country_list]
    name = csv_name(country_list)
    data.to_csv(r'pytrends_data/'+name+'.csv')


def read_csv(country_list):
    """
    This function reads a csv in the 'pytrends_data' folder with an
    identifiable name of the csv in the country_list and returns a dataframe
    . This reduces the number of times needed to ping Google. If no csv
    exists, then the function will make a csv.

    Args:
        country_list: A list of the country search terms

    Returns:
        A dataframe of the interest over time of countries in country_list
    """
    name = csv_name(country_list)
    if not path.exists('pytrends_data/'+name+'.csv'):
        make_csv(country_list)
    data = pd.read_csv('pytrends_data/'+name+'.csv')
    return data

def country_data_pytrend(country_list):
    """
    This function gets data from Google directly and returns a dataframe.

    Args:
        country_list: A list of the country search terms
    Returns:
        A dataframe of the interest over time of countries in country_list
    """
    pytrends.build_payload(country_list, cat=0,
                           timeframe='2006-01-01 2019-01-1', geo='US', gprop='')
    country_data = pytrends.interest_over_time()
    country_data = country_data[country_list]
    return country_data

def csv_name(country_list):
    """
    This function returns a single string from a list of strings by using
    the join function, adds '_' to split keywords, and removes all spaces
    from the string to make file referencing easier.

    Args:
        country_list: A list of the country search terms

    Returns:
        string_country: A single string containing all the countries
    """
    string_country = "_".join(country_list)
    string_country = string_country.replace(" ", "")
    return string_country

def list_to_string(country_list):
    """
    This function returns a single string from a list of strings by using
    the join function, and adds a commas (',') and a space (' ').

    Args:
        country_list: A list of the country search terms

    Returns:
        string_country: A single string containing all the countries
    """
    string_country = ", ".join(country_list)
    return string_country

def make_plots(country_data, country_list):
    """
    This function makes a plot of the given data and inputs the appropriate
    axis and titles to this plot.

    Args:
        country_data: A dataframe with columns of a country's interest
        value and time.
        country_list: A list of the country search terms

    Returns:
        No returns, instead inserts a plot
    """
    country_data.plot()
    plt.xlabel("Years")
    plt.ylabel("Relative Interest (0-100)")
    plt.legend(country_data, loc='best', fancybox=True)
    string_country = list_to_string(country_list)
    plt.title(string_country + ",\" of Interest In the US over Time")

def rolling_average_pct(country_data, keywords, months):
    """
    This function makes a rolling average rate of change plot. It first takes
    the data and takes a rolling average based on the number of points, months.
    Then, the data is made into a percent change. As a result of these averages
    and changes, the length of the plot changes substracted the value of months.
    Finally, the function plots the data with the correct labels.

    Args:
        country_data: A dataframe with columns of a country's interest
        value and time.
        keywords: A list of the countries that are being plotted.
        months: An int, the number of months to average the data by.
    Returns:
        No returns, inserts a plot
    """
    plot_b = country_data.rolling(months).mean() # Rolling Average
    plot_c = plot_b.pct_change() # Percent Change
    plot_c.plot()
    plt.xlabel("Years")
    plt.ylabel("ROC (times 100%)")
    plt.legend(country_data, loc='best', fancybox=True)
    string_country = list_to_string(keywords)
    plt.title(str(months) + " Month Rolling Average ROC for, \"" +
              string_country + ",\" of Interest In the US over Time")


def rolling_average(country_data, keywords, months):
    """
    This function makes a rolling average plot. It first takes
    the data and takes a rolling average based on the number of points, months.
    As a result of these averages and changes, the length of the plot changes
    substracted the value of months.
    Finally, the function plots the data with the correct labels.

    Args:
        country_data: A dataframe with columns of a country's interest
        value and time.
        keywords: A list of the countries that are being plotted.
        months: An int, the number of months to average the data by.
    Returns:
        No returns, inserts a plot
    """
    plot_b = country_data.rolling(months).mean()  # Rolling Average
    plot_b.plot()
    plt.xlabel("Years")
    plt.ylabel("Interest Level")
    plt.legend(country_data, loc='best', fancybox=True)
    string_country = list_to_string(keywords)
    plt.title(str(months) + " Month Rolling Average for, \"" +
              string_country + ",\" of Interest In the US over Time")


def histograms(country_data, keyword):
    """
    This function makes a histogram of the given data and inputs the appropriate
    axis and titles to this histogram using the pandas dataframe functions.

    Args:
        country_data: A dataframe with columns of a country's interest value.
        This dataframe can only contain data for one keyword
        keyword: A string that is the column heading of the country_data
    Returns:
        No returns, inserts a plot
    """
    plt.figure()
    country_data.hist([keyword])
    pl.xlabel("Interest Value")
    pl.ylabel("Frequency")
    pl.title("Histogram of " + keyword)


def boxplots(country_data, keyword):
    """
    This function makes a boxplot of the given data and inputs the appropriate
    axis and titles to this histogram using the pandas dataframe functions.

    Args:
        country_data: A dataframe with columns of a country's interest value.
        This dataframe can only contain data for one keyword
        keyword: A string that is the column heading of the country_data
    Returns:
        No returns, inserts a plot
    """
    plt.figure()
    country_data.boxplot([keyword])
    pl.ylabel("Interest Value")
    pl.title("Boxplot of " + keyword)


def pytrend_analysis(data, country_list, keyword, months):
    """
    This function does a complete analysis of the country_list. It checks
    to see if the file for data analysis exists or not, and will make a csv
    or skip to reading the file. It makes a plot of the data, the rolling average
    percent changes, a histogram, and box plot of the data.

    Args:
        country_list:
        keyword: A string to specify the boxplot and histogram
        months: An int, the number of months to average the data by.
    """
    #name = csv_name(country_list)
    #if not path.exists('pytrends_data/'+name+'.csv'):
    #    make_csv(country_list)
    #data = read_csv(country_list)
    make_plots(data, country_list)
    rolling_average_pct(data, country_list, months)
    histograms(data, keyword)
    plt.figure()
    boxplots(data, keyword)
