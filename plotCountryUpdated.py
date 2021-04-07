from pytrends.request import TrendReq
import pandas
import matplotlib.pyplot as plt
import pylab as pl

pytrends = TrendReq(hl='en-US', tz=360)


def makePlots(countryData, countryList):
    """
    This function makes a plot of the given data and inputs the appropriate
    axis and titles to this plot. 

    Args:
        countryData: A dataframe with columns of a country's interest 
        value and time.
        countryList: A list of the countries that are being plotted.

    Returns:
        No returns, instead inserts a plot
    """
    hold()
    hold(True)
    countryData.plot()
    plt.xlabel("Years")
    plt.ylabel("Relative Interest (0-100)")
    plt.legend(countryData, loc='best', fancybox=True)
    stringCountry = listToString(countryList)
    plt.title(stringCountry + ",\" of Interest In the US over Time")
    hold(False)


def listToString(countryList):
    """
    This function returns a single string from a list of strings by using
    the join function, and adds a commas (',') and a space (' '). 

    Args:
        countryList: A list of the countries.

    Returns:
        stringCountry: A single string containing all the countries
    """
    stringCountry = ", ".join(countryList)
    return stringCountry


def rollingAveragePct(countryData, keywords, months):
    """
    This function makes a rolling average rate of change plot. It first takes
    the data and takes a rolling average based on the number of points, months.
    Then, the data is made into a percent change. As a result of these averages
    and changes, the length of the plot changes substracted the value of months.
    Finally, the function plots the data with the correct labels. 

    Args:
        countryData: A dataframe with columns of a country's interest 
        value and time. 
        keywords: A list of the countries that are being plotted.
        months: An int, the number of months to average the data by.
    Returns:
        No returns, inserts a plot
    """
    b = countryData.rolling(months).mean()  # Rolling Average
    b = b.pct_change()  # Percent Change
    b.plot()
    hold()
    hold(True)
    plt.xlabel("Years")
    plt.ylabel("ROC (times 100%)")
    plt.legend(countryData, loc='best', fancybox=True)
    stringCountry = listToString(keywords)
    plt.title(str(months) + " Month Rolling Average ROC for, \"" +
              stringCountry + ",\" of Interest In the US over Time")
    hold(False)


def rollingAverage(countryData, keywords, months):
    """
    This function makes a rolling average plot. It first takes
    the data and takes a rolling average based on the number of points, months.
    As a result of these averages and changes, the length of the plot changes
    substracted the value of months.
    Finally, the function plots the data with the correct labels. 

    Args:
        countryData: A dataframe with columns of a country's interest 
        value and time. 
        keywords: A list of the countries that are being plotted.
        months: An int, the number of months to average the data by.
    Returns:
        No returns, inserts a plot
    """
    b = countryData.rolling(months).mean()  # Rolling Average
    b.plot()
    hold()
    hold(True)
    plt.xlabel("Years")
    plt.ylabel("Interest Level")
    plt.legend(countryData, loc='best', fancybox=True)
    stringCountry = listToString(keywords)
    plt.title(str(months) + " Month Rolling Average for, \"" +
              stringCountry + ",\" of Interest In the US over Time")
    hold(False)


def histograms(countryData, keyword):
    """
    This function makes a histogram of the given data and inputs the appropriate
    axis and titles to this histogram using the pandas dataframe functions. 

    Args:
        countryData: A dataframe with columns of a country's interest value.
        keyword: A string that is the column heading of the countryData
    Returns:
        No returns, inserts a plot
    """
    hold()
    hold(True)
    histdata = countryData.hist([keyword])
    pl.xlabel("Interest Value")
    pl.ylabel("Frequency")
    pl.title("Histogram of " + keyword)
    hold(False)


def boxplots(countryData, keyword):
    """
    This function makes a boxplot of the given data and inputs the appropriate
    axis and titles to this histogram using the pandas dataframe functions. 

    Args:
        countryData: A dataframe with columns of a country's interest value.
        keyword: A string that is the column heading of the countryData
    Returns:
        No returns, inserts a plot
    """
    hold()
    hold(True)
    boxdata = countryData.boxplot([keyword])
    # pl.xlabel("Value")
    pl.ylabel("Interest Value")
    pl.title("Boxplot of " + keyword)
    hold(False)
