from pytrends.request import TrendReq
import pandas
import matplotlib.pyplot as plt
pytrends = TrendReq(hl='en-US', tz=360)

def pytrendData(country, save_name="", directory="", category=0, time='all', loc=''):
    pytrends.build_payload(country, cat=category, timeframe=time, geo=loc, gprop='')
    countryData = pytrends.interest_over_time()
    return countryData
    
def pytrendPlot(country):
    data = pytrendData(country)
    data.plot()
    
def pytrendTable(country):
    countryData = pytrendData(country)
    
def getFirstCountry(fullCountryList):
    firstCountry = [] #pytrends requires list
    firstCountry.append(fullCountryList[0])
    return firstCountry

def makePlots(fullCountryList):
    while len(fullCountryList) > 0:
        country = getFirstCountry(fullCountryList)
        del fullCountryList[0];
        pytrendPlot(country)