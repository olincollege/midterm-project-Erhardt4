from pytrends.request import TrendReq
import pandas as pd
import matplotlib.pyplot as plt
import pylab as pl
import os.path
from os import path

pytrends = TrendReq(hl='en-US', tz=360)

def makeCSV(countryList):
    """
    This function makes a csv in the 'pytrends_Data' folder with an
    identifiable name of the csv based on the countryList. By having
    the country list, we can construct a data frame and save it. This
    reduces the number of times needed to ping Google.

    Args:
        countryList: A list of the country search terms

    Returns:
        No returns, makes a csv in folder 'Pytrends_Data' that saves a 
        dataframe of interest over time.
    """
    pytrends = TrendReq(hl='en-US', tz=360)
    pytrends.build_payload(countryList, cat=0, timeframe='all',
                           geo='US', gprop='')  
    data = pytrends.interest_over_time()
    data = data[countryList]
    name = csvName(countryList)
    data.to_csv(r'pytrends_Data/'+name+'.csv')

def readCSV(countryList):
    """
    This function reads a csv in the 'pytrends_Data' folder with an
    identifiable name of the csv in the countryList. This
    reduces the number of times needed to ping Google. If no csv
    exists, then the function will make a csv. 

    Args:
        countryList: A list of the country search terms

    Returns:
        A dataframe of the interest over time of countries in countryList
    """
    name = csvName(countryList)
    if(path.exists('pytrends_Data/'+name+'.csv') == False):
        makeCSV(countryList)
    data = pd.read_csv('pytrends_Data/'+name+'.csv')
    return data

def makePlots(countryData, countryList):
    """
    This function makes a plot of the given data and inputs the appropriate
    axis and titles to this plot. 

    Args:
        countryData: A dataframe with columns of a country's interest 
        value and time.
        countryList: A list of the country search terms

    Returns:
        No returns, instead inserts a plot
    """
    countryData.plot()
    plt.xlabel("Years")
    plt.ylabel("Relative Interest (0-100)")
    plt.legend(countryData, loc='best', fancybox=True)
    stringCountry = listToString(countryList)
    plt.title(stringCountry + ",\" of Interest In the US over Time")


def listToString(countryList):
    """
    This function returns a single string from a list of strings by using
    the join function, and adds a commas (',') and a space (' '). 

    Args:
        countryList: A list of the country search terms

    Returns:
        stringCountry: A single string containing all the countries
    """
    stringCountry = ", ".join(countryList)
    return stringCountry
                
def csvName(countryList):
    """
    This function returns a single string from a list of strings by using
    the join function, adds '_' to split keywords, and removes all spaces
    from the string to make file referencing easier. 

    Args:
        countryList: A list of the country search terms

    Returns:
        stringCountry: A single string containing all the countries
    """
    stringCountry = "_".join(countryList)
    stringCountry = stringCountry.replace(" ", "")
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

    plt.xlabel("Years")
    plt.ylabel("ROC (times 100%)")
    plt.legend(countryData, loc='best', fancybox=True)
    stringCountry = listToString(keywords)
    plt.title(str(months) + " Month Rolling Average ROC for, \"" +
              stringCountry + ",\" of Interest In the US over Time")


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

    plt.xlabel("Years")
    plt.ylabel("Interest Level")
    plt.legend(countryData, loc='best', fancybox=True)
    stringCountry = listToString(keywords)
    plt.title(str(months) + " Month Rolling Average for, \"" +
              stringCountry + ",\" of Interest In the US over Time")



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

    histdata = countryData.hist([keyword])
    pl.xlabel("Interest Value")
    pl.ylabel("Frequency")
    pl.title("Histogram of " + keyword)


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

    boxdata = countryData.boxplot([keyword])
    # pl.xlabel("Value")
    pl.ylabel("Interest Value")
    pl.title("Boxplot of " + keyword)
    
def pytrendAnalysis(countryList, keyword, months):
    """
    This function does a complete analysis of the countryList. It checks
    to see if the file for data analysis exists or not, and will make a csv
    or skip to reading the file. It makes a plot of the data, the rolling average
    percent changes, a histogram, and box plot of the data. 
    
    Args: 
        countryList:
        keyword: A string to specify the boxplot and histogram
        months: An int, the number of months to average the data by.
    """
    name = csvName(countryList)
    if(path.exists('pytrends_Data/'+name+'.csv') == False):
        makeCSV(countryList)
    data = readCSV(countryList)
    makePlots(data, countryList)
    rollingAveragePct(data, countryList, months)
    histograms(data, keyword)
    plt.figure(0)
    boxplots(data, keyword)