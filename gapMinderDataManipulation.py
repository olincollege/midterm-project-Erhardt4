import pandas
import statistics
import csv
import matplotlib.pyplot as plt


def createDataFrame(filename):
    """
    Createa a pandas dataframe from a ,csv.
    
    Args:
        filename: A string representing the name of the 
                  .csv file containing the data.
    Returns:
        A pandas dataframe of the data in the file.
    """
    dataframe = pandas.read_csv(filename)
    return dataframe


def getSpecificCountriesData(dataframe, countryList):
    """
    Gets the EIU Index Data of specific countries.
    
    Args:
        datarame: A pandas dataframe containing the EIU Democracy
                  Index values of each of the countries
        countryList: A list containing country indexes of the countries
                     which data is needed.
    Returns:
        A dictionary containing the country name as the key and a pandas
        dataframe containing the EIU Index values of the specific country
        as the value.
    """
    temp = {}
    countryNameList = getCountryNameList("EIU_Democracy_Index.csv")
    for index in countryList:
        temp[countryNameList[index]] = dataframe.iloc[index, 1:14]
    return temp


def getCountryNameList(filename):
    """
    Generates a list of all the country names.
    
    Args:
        filename: A string representing the name of the file which the
                  data is being accessed.
    Returns:
        A list of strings containing each country's name.
    """
    r = csv.reader(open(filename, "r"))
    countryList = []
    for row in r:
        countryList.append(row[0])
    return countryList[1:]


def getYearList(filename):
    """
    Generates a list of all the years.
    
    Args:
        filename: A string representing the name of the file which the
                  data is being accessed.
    Returns:
        A list of integers containing all the years the data is from.
    """
    r = csv.reader(open(filename, "r"))
    counter = True
    for row in r:
        if counter:
            yearList = row[1:]
            counter = False
    for i in range(len(yearList)):
        yearList[i] = int(yearList[i])
    return yearList


def getGreatestVarianceCountries(threshold):
    """
    Gets countries whose variance is above a certain threshold.
    
    Args:
        threshold: An integer representing the threshold of the
                   countries EIU Index data variance.
    Returns:
        A list containing country indexes of countries which
        variances are above the threshold.
    """
    countriesAboveThreshold = []
    dataframe = createDataFrame("EIU_Democracy_Index.csv")
    for i in range(164):
        temp = dataframe.iloc[i, 1:14]
        if statistics.pstdev(temp) > threshold:
            countriesAboveThreshold.append(i)
    return countriesAboveThreshold


def plotData(data):
    """
    Plots a line graph of given data.
    
    Args:
        data: a dictionary of pandas dataframes as keys or a 
              single pandas dataframe containing the data that
              needs to be plotted.
    """
    plt.figure()
    yearList = getYearList("EIU_Democracy_Index.csv")
    for element in data:
        plt.plot(yearList, data[element], marker='+')

    plt.xlabel("Years")
    plt.ylabel("EIU Democracy Index Value")
    plt.xlim(2006, 2020)
    plt.ylim(0, 1)
    plt.legend(data.keys(), loc='best')
    plt.title("EIU Democracy Index Value Over Time")


def plotChosenCountries(countryList):
    """
    Plots a line graph of the EIU Indexes of specific countries.
    
    Args:
        countryList: A list of country indexes of countries that
                     need to be plotted.
    """
    dataframe = createDataFrame("EIU_Democracy_Index.csv")
    data = getSpecificCountriesData(dataframe, countryList)
    plotData(data)


def getRates(countryList):
    """
    Gets the rates of changes of the EIU Index Values of a list
    of countries.
    
    Args:
        countryList: A list of country indexes of countries that
                     need rates.
    Returns:
        A dictionary containing the country name as the key and a pandas
        dataframe containing the rate of change of EIU Index values as a
        percent of the specific country as the value.
    """
    dataframe = createDataFrame("EIU_Democracy_Index.csv")
    data = getSpecificCountriesData(dataframe, countryList)
    rates = {}
    for key in data:
        temp = []
        for i in range(len(data[key])-1):
            temp.append(((data[key][i+1]-data[key][i])/data[key][i])*100)
        rates[key] = temp
    return rates


def plotRates(data):
    """
    Plots a line graph of the rate of changes of EIU Indexes of 
    specific countries.
    
    Args:
        data: a dictionary of pandas dataframes as keys or a 
              single pandas dataframe containing the rate data
              that needs to be plotted.
    """
    plt.figure()
    yearList = getYearList("EIU_Democracy_Index.csv")
    yearList = yearList[1:]
    for element in data:
        plt.plot(yearList, data[element], marker='+')
    plt.xlabel("Years")
    plt.ylabel("Rate of Change of EIU Index Value (%)")
    plt.xlim(2006, 2020)
    # plt.ylim(-90,110)
    plt.legend(data.keys(), loc='best')
    plt.title("Rate of Change of EIU Democracy Index Value Over Time")


def plotRateChosenCountries(countryList):
    """
    Plots a line graph of the rate of change of EIU Indexes of
    specific countries.
    
    Args:
        countryList: A list of country indexes of countries that
                     need to be plotted.
    """
    rates = getRates(countryList)
    plotRates(rates)


def plotHistogram(yearIndex):
    """
    Plots a histogram of the EIU Index Values of all countries 
    in a given year.
    
    Args:
        yearIndex: An integer representing the year of the indexes
                   that need to be plotted.
    """
    dataframe = createDataFrame("EIU_Democracy_Index.csv")
    allCountries = range(0, 164)
    allData = getSpecificCountriesData(dataframe, allCountries)
    data = []
    for element in allData:
        data.append(allData[element][yearIndex])
    plt.figure()
    plt.hist(data)
    plt.xlabel("EIU Index Scores")
    plt.ylabel("Frequency")


def plotHistogramAllYears():
    """
    Plots a histogram of the EIU Index Value of all countries
    for each year there is data for.
    """
    fig, axs = plt.subplots(5, 3, sharey='row', figsize=(20, 30))
    dataframe = createDataFrame("EIU_Democracy_Index.csv")
    allCountries = range(0, 164)
    allData = getSpecificCountriesData(dataframe, allCountries)
    for i in range(13):
        data = []
        for element in allData:
            data.append(allData[element][i])
        ax = axs[i//3, i % 3]
        ax.hist(data, bins=20, color='blue', alpha=0.75)
        ax.set_xlabel("EIU Index")
        ax.set_ylabel("Frequency")
        ax.set_title(f"EIU Index of Each Country in {i+2006}")


def plotHistogramAllData():
    """
    Plots a histogram of the EIU Index Value of all the countries
    for all the years there is data for.
    """
    dataframe = createDataFrame("EIU_Democracy_Index.csv")
    allCountries = range(0, 164)
    allData = getSpecificCountriesData(dataframe, allCountries)
    data = []
    for element in allData:
        for i in range(13):
            data.append(allData[element][i])
    plt.figure()
    plt.hist(data, bins=20, color='blue')
    plt.xlabel("EIU Index Scores")
    plt.ylabel("Frequency")
    plt.title("EIU Index of Each Country")
