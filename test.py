#Necessary Packages
import time
import requests
import numpy as np
import pandas as pd
from bs4 import BeautifulSoup
# YOUR CODE HERE (OPTION)
# If you need other support packages
import xml.etree.ElementTree as ET  # for parsing XML

BASE_URL = 'http://api.worldbank.org/v2/'
COUNTRIES = ["US", "IN", "CN", "JP", "CA", "GB", "ZA"]
INDICATORS = ['SP.POP.TOTL',
             'SP.POP.TOTL.FE.IN',
             'SP.POP.TOTL.MA.IN',
             'SP.DYN.CBRT.IN',
             'SP.DYN.CDRT.IN',
             'SP.DYN.LE00.MA.IN',
             'SP.DYN.LE00.FE.IN',
             'SE.PRM.ENRR',
             'SE.TER.ENRR',
             'SE.PRM.CMPT.ZS',
             'SE.ADT.1524.LT.ZS']
Country = []
TotalPopulation = []
FemalePopulation = []
MalePopulation = []
BirthRate = []
DeathRate = []
MaleExpectancy = []
FemaleExpectancy = []
PriEnroll = []
TerEnroll = []
PriComple = []
LiterRate = []
Year = []
#TODO (option)
# If you need other initializations

def collect_data(countryCode, per_page, start_year, end_year):
    #TODO
    for indicator in INDICATORS:
        response = requests.get("http://api.worldbank.org/v2/countries/" + countryCode + "/indicators/" + indicator)
        root = ET.fromstring(response.content)
        namespace = {'wb': 'http://www.worldbank.org'}
        data_elements = root.findall(".//wb:data",namespaces = namespace)
        for data_element in data_elements:
            countryElement = data_element.find("wb:countryiso3code", namespaces=namespace)
            date_element = data_element.find("wb:date", namespaces=namespace)
            value_element = data_element.find("wb:value", namespaces=namespace)
            Country.append(countryElement.text)
            Year.append(data_element.text)
            if indicator == indicator[0]:
                TotalPopulation.append(value_element)
            if indicator == indicator[1]:
                FemalePopulation.append(value_element)
            if indicator == indicator[2]:
                MalePopulation.append(value_element)
            if indicator == indicator[3]:
                BirthRate.append(value_element)
            if indicator == indicator[4]:
                DeathRate.append(value_element)
            if indicator == indicator[5]:
                MaleExpectancy.append(value_element)
            if indicator == indicator[6]:
                FemaleExpectancy.append(value_element)
            if indicator == indicator[7]:
                PriEnroll.append(value_element)
            if indicator == indicator[8]:
                TerEnroll.append(value_element)
            if indicator == indicator[9]:
                PriComple.append(value_element)
            if indicator == indicator[10]:
                LiterRate.append(value_element)
            



    

    #raise NotImplementedError("not implement")

def Generate_Countries_Dataset(countryCode_list):
    data = pd.DataFrame()
    for countryCode in countryCode_list:
        data = pd.concat([data, collect_data(countryCode = countryCode, per_page = 100, start_year = 2000, end_year = 2022)], axis=0)
    return data

data_countries = Generate_Countries_Dataset(COUNTRIES)
print(data_countries)