import numpy as np
import pandas as pd
import requests
import json
import time 
import matplotlib.pyplot as plt
#%matplotlib inline
import seaborn as sns
import datetime

class Weather_Gov:
    def __init__(self, zipcode):
        self.zipcode = zipcode
        self.zip_to_latandlong()
        self.connect_weather()

    def zip_to_latandlong(self):
        if type(self.zipcode) == int:
            self.zipcode = str(self.zipcode)
        web_a = "https://public.opendatasoft.com/api/records/1.0/search/?dataset=us-zip-code-latitude-and-longitude&q="
        web_b = "&facet=state&facet=timezone&facet=dst"
        self.latlongrequest = requests.request("Get",web_a+self.zipcode+web_b)
        self.latlongOutput = self.latlongrequest.json()
        self.latlongOutput = self.latlongOutput['records']
        self.latlongOutput=self.latlongOutput[0]
        self.latlongOutput = self.latlongOutput['fields']
        self.latitude = str(self.latlongOutput['latitude'])
        self.longitude = str(self.latlongOutput['longitude'])
        print(self.latitude,self.longitude)
    def connect_weather(self):
        govweather_ = "https://api.weather.gov/points/"
        self.gov_response = requests.request("Get",govweather_+self.latitude+','+self.longitude)
        if self.gov_response.status_code == 400:
            print('400 failure')
        elif self.gov_response.status_code == 200:
            print("Connected!")
        else:
            print(self.gov_response.status_code)
        self.gov_response = self.gov_response.json()
    def forcaster(self):
        self.forcast = requests.request("Get",self.gov_response['properties']['forecast'])
        return self.forcast.json()['properties']['periods'][0]['detailedForecast']

def test_connect_weather():
    weather_report = Weather_Gov(zipcode= '60060')
    current_weather = weather_report.forcaster()
    print(current_weather)



if __name__ == '__main__':
    test_connect_weather()
