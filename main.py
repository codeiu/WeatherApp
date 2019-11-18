import weatherdata
import graphing
import dataAnalysis
# import getForms
import mailTest
import personal

if __name__ == "__main__":
    weatherdata.getWeather()
    graphing.graphs()
    analytics,interpretation,analyticsHTML,interpretationHTML = dataAnalysis.weatherStats()
    name = 'Arthur, King of the Britons'
    date = personal.getDate()
    mailTest.makeMessage(name,date,analytics,interpretation,analyticsHTML,interpretationHTML)