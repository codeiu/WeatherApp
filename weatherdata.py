import requests
from bs4 import BeautifulSoup
import pandas as pd
import csv
import random


city = ''
state = ''
location = ''
url = ''

def makeSoup():
    global city
    global state
    global location
    global url
    city = input('Please enter city name: ').lower().strip()
    state = input('Please enter state: ').lower().strip()
    location = city + '-' + state
    url = 'https://www.timeanddate.com/weather/usa/' + location + '/hourly'
    site = requests.get(url)
    soup = BeautifulSoup(site.text, 'html.parser')
    
    try:
        tag = soup.h1
        
        if ('Unknown address' in tag.string):
            url = 'https://www.timeanddate.com/weather/usa/' + city + '/hourly'
            site = requests.get(url)
            soup = BeautifulSoup(site.text, 'html.parser')
    except:
        return soup

    return soup

def cityCheck(soup):
    
    tag = soup.h1
    try:
        if ('Unknown address' in tag.string):
            print('Try Again')
            return False
        elif ('404' in tag.string):
            print('404')
            print('Try Again')
            return False
        else:
            return True
    except:
        print('Try Again')
        return False

def getTable(soup):

    bigTable = soup.tbody
    return bigTable

def getWeather():
    
    try:
        soup = makeSoup()
    except:
        soup = makeSoup()

    
    while not cityCheck(soup):
        soup = makeSoup()
    bigTable = getTable(soup)

    # Hours
    timeCells = bigTable.findAll('th')
    hour_lst = []
    for cell in timeCells:
        child = cell.contents[0]
        if child:
            hr24 = child
            if ('pm' in child) and (child != '12:00 pm'):
                hour = child.split(':')
                hour = str(int(hour[0])+12) + ':00'
                hr24 = hour
            elif ('am' in child) and (child != '12:00 am'):
                hour = child.split(':')
                hour = hour[0] + ':00'
                hr24 = hour
            elif child == '12:00 am':
                hr24 = '00:00'
            elif child == '12:00 pm':
                hr24 = '12:00'
            if len(hr24) < 5:
                hr24 = '0' + hr24
            hour_lst.append(hr24)

    # Temperatures
    tempAndPrecipCells = bigTable.findAll('tr')
    temperature_lst = []
    for cell in tempAndPrecipCells:
        child = cell.contents[2].string.strip('\xa0°F')
        temperature_lst.append(child)

    # Precipitation
    precip_lst = []
    for cell in tempAndPrecipCells:
        child = cell.contents[-2].string
        child = child[:-1]
        precip_lst.append(child)


    csv_template = [['index','Time', 'Temperature', 'Precipitation']]
    index = 0
    while index < len(hour_lst):
        #csv_template += item + ', ' + temperature_lst[hour_lst.index(item)] + '\n'
        row = [index+1,hour_lst[index], temperature_lst[index], precip_lst[index]]
        csv_template.append(row)
        index += 1

    # print(csv_template)

    with open ('timeanddate_scrape.csv', 'w') as new_file:
        csv_writer = csv.writer(new_file)
        for item in csv_template:
            csv_writer.writerow(item)