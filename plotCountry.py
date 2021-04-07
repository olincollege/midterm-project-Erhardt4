from pytrends.request import TrendReq
import pandas
import matplotlib.pyplot as plt
pytrends = TrendReq(hl='en-US', tz=360)


def pytrendData(country, save_name="", directory="", category=0, time='all', loc='US'):
    pytrends.build_payload(country, cat=category,
                           timeframe=time, geo=loc, gprop='')
    countryData = pytrends.interest_over_time()
    return countryData


def pytrendPlot(country):
    data = pytrendData(country)
    data.plot()
    plt.xlabel("Years")
    plt.ylabel("Relative Interest (0-100)")
    plt.legend(country, loc='best', fancybox=True)
    plt.title("Keyword, \"" + country[0] + ",\" Interest In the US over Time")


def pytrendTable(country):
    countryData = pytrendData(country)


def getFirstCountry(fullCountryList):
    firstCountry = []  # pytrends requires list
    firstCountry.append(fullCountryList[0])
    return firstCountry


def makePlots(fullCountryList):
    while len(fullCountryList) > 0:
        country = getFirstCountry(fullCountryList)
        del fullCountryList[0]
        pytrendPlot(country)


def getString(country):
    listToStr = " ".join(map(str, country))
    return listToStr


def getChange(country):
    data = pytrendData(country)
    data = data[country]
    i = 0
    sumThree = 0
    tempAvg = []
    counter = 0
    sumfin = 0
    for key in data:
        while i < (len(data[key]) - 3):
            sumThree = data[key][i] + data[key][i+1] + data[key][i+2]
            sumThree = sumThree/3
            tempAvg.append(sumThree)
            i = i + 3
            counter += 1
            data = data[key][(i+2):]
            sumThree = 0
        if len(data[key]) < 3 and len(data[key]) > 0:
            for i in data[key]:
                sumfin = data[key][i]
        tempAvg.append(sumfin/len(data[key]))
    return tempAvg


def getSpecificCountriesData(dataframe, keywordList):
    temp = {}

    for index in range(len(keywordList)):
        temp[keywordList[index]] = dataframe.set_index(keywordList[index])
    return temp


def getTime(dataframe):
    indexNamesArr = dataframe.index.values
    listOfRowIndexLabels = list(indexNamesArr)
    return listOfRowIndexLabels
