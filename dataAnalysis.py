import pandas as pd
import random

tempRangeDict = {
    'coldRange': [-100,32],
    'chillyRange': [33,60],
    'warmRange': [61,80],
    'hotRange': [81,130]
    }

clothingTops = {
    'cold':['sweater','sweatshirt','coat'],
    'chilly':['light jacket','cardigan','sweatshirt','long sleeve t'],
    'warm':['t shirt'],
    'hot':['tank top','t shirt'],
    'rainy':['rain jacket'],
    'snowy':[]
}
clothingBottoms = {
    'chilly':['jeans','sweatpants','leggings'],
    'cold':['jeans','thick sweatpants','warm leggings'],
    'warm':['shorts'],
    'hot':['athletic shorts'],
    'rainy':[],
    'snowy':[]
}
clothingAccessories = {
    'chilly':[],
    'cold':['gloves','hat','fuzzy socks'],
    'warm':[],
    'hot':[],
    'rainy':['umbrella','rain boots'],
    'snowy':['gloves','boots','gloves','hat','skis']
}

def weatherStats():
    df = pd.read_csv('timeanddate_scrape.csv')
    tempMean = df.loc[:,'Temperature'].mean()
    tempHigh = df.loc[:,'Temperature'].max()
    tempLow = df.loc[:,'Temperature'].min()
    tempStDev = df.loc[:,'Temperature'].std()
    precipMean = df.loc[:,'Precipitation'].mean()
    precipStDev = df.loc[:,'Precipitation'].std()
    precipMax = df.loc[:, 'Precipitation'].max()
    analytics = f'Temp mean: {tempMean:.2f}\nTemp high: {tempHigh}\nTemp low: {tempLow}\nTemp standard dev: {tempStDev:.2f}\nPrecip mean: {precipMean:.2f}\nPrecip standard dev: {precipStDev:.2f}\nPrecip max: {precipMax}'
    analyticsHTML = analytics.split('\n')
    analyticsHTML = '<br>'.join(analyticsHTML)
    """
    print('Temp mean: ',str(tempMean))
    print('Temp high: ',str(tempHigh))
    print('Temp low: ',str(tempLow))
    print('Temp standard dev: ',str(tempStDev))
    print('Precip mean: ',str(precipMean))
    print('Precip standard dev: ',str(precipStDev))
    print('Precip max: ',str(precipMax))
    """

    

    # interpretation
    intepretation = ''
    if (int(tempMean) in range(tempRangeDict['coldRange'][0],tempRangeDict['coldRange'][1])):
        x = 'cold'
        interpretation = 'It\s going to be cold today. Wear a {0}, {1}, and bring {2}.'.format(random.choice(clothingTops[x]),random.choice(clothingBottoms[x]),random.choice(clothingAccessories[x]))
    elif (int(tempMean) in range(tempRangeDict['chillyRange'][0],tempRangeDict['chillyRange'][1])):
        x = 'chilly'
        interpretation = 'It\'s going to be chilly today. Wear a {0} and {1}.'.format(random.choice(clothingTops[x]),random.choice(clothingBottoms[x]))
    elif (int(tempMean) in range(tempRangeDict['warmRange'][0],tempRangeDict['warmRange'][1])):
        x = 'warm'
        interpretation = 'It\'s going to be warm today. Wear a {0} and {1}.'.format(random.choice(clothingTops[x]),random.choice(clothingBottoms[x]))
    elif (int(tempMean) in range(tempRangeDict['hotRange'][0],tempRangeDict['hotRange'][1])):
        x = 'hot'
        interpretation = 'It\'s going to be hot today. Wear a {0} and {1}.'.format(random.choice(clothingTops[x]),random.choice(clothingBottoms[x]))
    
    if tempStDev > 7:
        interpretation = interpretation + '\nThe temperature is going to vary a lot today. Bring layers.'

    if precipMax > 40:
        interpretation = interpretation + '\nIT GON RAIN'

    interpretationHTML = interpretation.split('\n')
    interpretationHTML = '<br>'.join(interpretationHTML)

    return (analytics,interpretation,analyticsHTML,interpretationHTML)