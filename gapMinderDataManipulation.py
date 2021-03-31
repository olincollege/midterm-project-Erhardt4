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
    plt.xlim(2006, 2026)
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
    plt.xlim(2006, 2026)
    #plt.ylim(-90,110)
    plt.legend(data.keys(), loc = 'best')
    plt.title("Rate of Change of EIU Democracy Index Value Over Time")
    
def plotRateChosenCountries(countryList):
    rates = getRates(countryList)
    plotRates(rates)