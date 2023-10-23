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

# TotalPopulation = []
# FemalePopulation = []
# MalePopulation = []
# BirthRate = []
# DeathRate = []
# MaleExpectancy = []
# FemaleExpectancy = []
# PriEnroll = []
# TerEnroll = []
# PriComple = []
# LiterRate = []
# Year = []
# Country = []
def collect_data(countryCode, per_page, start_year, end_year):
    #TODO
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
    for indicator in INDICATORS:
        response = requests.get(f"http://api.worldbank.org/v2/countries/{countryCode}/indicators/{indicator}", params={
            "format": "xml",
            "per_page": per_page,
            "date": f"{start_year}:{end_year}"
        })
        #response = requests.get("http://api.worldbank.org/v2/countries/" + countryCode + "/indicators/" + indicator)
        root = ET.fromstring(response.content)
        namespace = {'wb': 'http://www.worldbank.org'}
        data = root.findall(".//wb:data",namespaces = namespace)
        tempCountry = []
        tempYear = []
        for element in data:
            countryElement = element.find("wb:countryiso3code", namespaces=namespace)
            dateElement = element.find("wb:date", namespaces=namespace)
            valueElement = element.find("wb:value", namespaces=namespace)
            tempCountry.append(countryElement.text)
            tempYear.append(dateElement.text)
            if indicator == INDICATORS[0]:
                if valueElement.text is None:
                    TotalPopulation.append("None")
                else:
                    TotalPopulation.append(float(valueElement.text))
            if indicator == INDICATORS[1]:
                if valueElement.text is None:
                    FemalePopulation.append("None")
                else:
                    FemalePopulation.append(float(valueElement.text))
            if indicator == INDICATORS[2]:
                if valueElement.text is None:
                    MalePopulation.append("None")
                else:
                    MalePopulation.append(float(valueElement.text))
            if indicator == INDICATORS[3]:
                if valueElement.text is None:
                    BirthRate.append("None")
                else:
                    BirthRate.append(float(valueElement.text))
            if indicator == INDICATORS[4]:
                if valueElement.text is None:
                    DeathRate.append("None")
                else:
                    DeathRate.append(float(valueElement.text))
            if indicator == INDICATORS[5]:
                if valueElement.text is None:
                    MaleExpectancy.append("None")
                else:
                    MaleExpectancy.append(float(valueElement.text))
            if indicator == INDICATORS[6]:
                if valueElement.text is None:
                    FemaleExpectancy.append("None")
                else:
                    FemaleExpectancy.append(float(valueElement.text))
            if indicator == INDICATORS[7]:
                if valueElement.text is None:
                    PriEnroll.append("None")
                else:
                    PriEnroll.append(float(valueElement.text))
            if indicator == INDICATORS[8]:
                if valueElement.text is None:
                    TerEnroll.append("None")
                else:
                    TerEnroll.append(float(valueElement.text))
            if indicator == INDICATORS[9]:
                if valueElement.text is None:
                    PriComple.append("None")
                else:
                    PriComple.append(float(valueElement.text))
            if indicator == INDICATORS[10]:
                if valueElement.text is None:
                    LiterRate.append("None")
                else:
                    LiterRate.append(float(valueElement.text))
        arrDate = np.array(tempCountry)
        arrCountry = np.array(tempYear)
        result = np.column_stack((arrDate, arrCountry))
    
    dataFrame = pd.DataFrame({"TotalPopulation": TotalPopulation,
                     "FemalePopulation": FemalePopulation,
                     "MalePopulation": MalePopulation,
                     "BirthRate": BirthRate,
                     "DeathRate": DeathRate,
                     "MaleExpectancy": MaleExpectancy,
                     "FemaleExpectancy":FemaleExpectancy,
                     "PriEnroll":PriEnroll,
                     "TerEnroll":TerEnroll,
                     "PriComple":PriComple,
                     "LiterRate":LiterRate,
                     "Country": tempCountry,
                     "Year": tempYear
                     },index = None)
    return dataFrame

    #raise NotImplementedError("not implement")
testUSA = collect_data("US", per_page = 100, start_year = 2000, end_year = 2022)
testUSA.to_csv("testUSA.csv",index=False)

# def Generate_Countries_Dataset(countryCode_list):
#     data = pd.DataFrame(index= None)
#     for countryCode in countryCode_list:
#         data = pd.concat([data, collect_data(countryCode = countryCode, per_page = 100, start_year = 2000, end_year = 2022)], axis=0)
#     return data

# data_countries = Generate_Countries_Dataset(COUNTRIES)
# data_countries.to_csv("countries.csv",index=False)