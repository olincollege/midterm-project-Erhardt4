import pandas
import statistics
import csv
import matplotlib.pyplot as plt

def createDataFrame(filename):
    dataframe = pandas.read_csv(filename)
    return dataframe

def getSpecificCountriesData(dataframe, countryList):
    temp = {}
    countryNameList = getCountryNameList("EIU_Democracy_Index.csv")
    for index in countryList:
        temp[countryNameList[index]] = dataframe.iloc[index,1:14]
    return temp

def getCountryNameList(filename):
    r = csv.reader(open(filename, "r"))
    countryList = []
    for row in r:
        countryList.append(row[0])
    return countryList[1:]

def getYearList(filename):
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
    countriesAboveThreshold = []
    dataframe = createDataFrame("EIU_Democracy_Index.csv")
    for i in range(164):
        temp = dataframe.iloc[i,1:14]
        if statistics.pstdev(temp) > threshold:
            countriesAboveThreshold.append(i)
    return countriesAboveThreshold
def plotData(data):
    plt.figure()
    yearList = getYearList("EIU_Democracy_Index.csv")
    for element in data:
        plt.plot(yearList, data[element], marker =  '+')

    plt.xlabel("Years")
    plt.ylabel("EIU Democracy Index Value")
    plt.xlim(2006, 2020)
    plt.ylim(0,1)
    plt.legend(data.keys(), loc = 'best')
    plt.title("EIU Democracy Index Value Over Time")

def plotChosenCountries(countryList):
    dataframe = createDataFrame("EIU_Democracy_Index.csv")
    data = getSpecificCountriesData(dataframe, countryList)
    plotData(data)
    
def getRates(countryList):
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
    plt.figure()
    yearList = getYearList("EIU_Democracy_Index.csv")
    yearList = yearList[1:]
    for element in data:
        plt.plot(yearList, data[element], marker =  '+')
    plt.xlabel("Years")
    plt.ylabel("Rate of Change of EIU Index Value (%)")
    plt.xlim(2006, 2020)
    #plt.ylim(-90,110)
    plt.legend(data.keys(), loc = 'best')
    plt.title("Rate of Change of EIU Democracy Index Value Over Time")
    
def plotRateChosenCountries(countryList):
    rates = getRates(countryList)
    plotRates(rates)
    
def plotHistogram(yearIndex):
    dataframe  = createDataFrame("EIU_Democracy_Index.csv")
    allCountries = range(0,164)
    allData = getSpecificCountriesData(dataframe, allCountries)
    data = []
    for element in allData:
        data.append(allData[element][yearIndex])
    plt.figure()
    plt.hist(data)
    plt.xlabel("EIU Index Scores")
    plt.ylabel("Frequency")

def plotHistogramAllYears():
    fig, axs = plt.subplots(5, 3, sharey='row', figsize=(20, 30))
    dataframe  = createDataFrame("EIU_Democracy_Index.csv")
    allCountries = range(0,164)
    allData = getSpecificCountriesData(dataframe, allCountries)
    for i in range(13):
        data = []
        for element in allData:
            data.append(allData[element][i])
        ax = axs[i//3,i%3]
        ax.hist(data, bins=20, color='blue', alpha=0.75)
        ax.set_xlabel("EIU Index")
        ax.set_ylabel("Frequency")
        ax.set_title(f"EIU Index of Each Country in {i+2006}")
def plotHistogramAllData():
    dataframe  = createDataFrame("EIU_Democracy_Index.csv")
    allCountries = range(0,164)
    allData = getSpecificCountriesData(dataframe, allCountries)
    data = []
    for element in allData:
        for i in range(13):
            data.append(allData[element][i])
    plt.figure()
    plt.hist(data, bins = 20, color='blue')
    plt.xlabel("EIU Index Scores")
    plt.ylabel("Frequency")
    plt.title("EIU Index of Each Country")