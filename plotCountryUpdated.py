from pytrends.request import TrendReq
import pandas
import matplotlib.pyplot as plt
import pylab as pl

pytrends = TrendReq(hl='en-US', tz=360)

def makePlots(countryData, countryList):
    countryData.plot()
    plt.xlabel("Years")
    plt.ylabel("Relative Interest (0-100)")
    plt.legend(countryData, loc = 'best', fancybox = True)  
    stringCountry = listToString(countryList)
    plt.title("Keyword, \""+ stringCountry + ",\" of Interest In the US over Time")

def listToString(countryList):
    stringCountry = ", ".join(countryList)
    return stringCountry

def rollingAverage(countryData, keywords, months):
    b = countryData.rolling(months).mean()
    b.plot()
    plt.xlabel("Years")
    plt.ylabel("Relative Interest (0-100)")
    plt.legend(countryData, loc = 'best', fancybox = True)  
    stringCountry = listToString(keywords)
    plt.title(str(months) + " Month Rolling Average for Keywords, \""+ \
              stringCountry + ",\" of Interest In the US over Time")    
def histograms(countryData, keyword):
    histdata = countryData.hist([keyword])
    pl.xlabel("Value")
    pl.ylabel("Frequency")
    pl.title("Histogram of " + keyword)
    
def boxplots(countryData, keyword):
    boxdata = countryData.boxplot([keyword])
    #pl.xlabel("Value")
    pl.ylabel("Value")
    pl.title("Boxplot of " + keyword)    