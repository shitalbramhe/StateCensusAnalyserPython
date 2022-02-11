"""
@Author: Shital Bajait
@Date: 11-02-2022 15:09:00
@Last Modified by: Shital Bajait 
@Last Modified time: 11-02-2022 15:09:00
@Title : Save the State Census Data into a Json File
"""
import csv
import json

class StateSensusHandler():
    def state_census_csv_convert(csv_path, json_path):
        jsonData = {}
        with open(csv_path, encoding='utf-8') as csvfile:
            csvData = csv.DictReader(csvfile)
            for rows in csvData:
                key = rows['State']
                jsonData[key] = rows

        with open(json_path,'w',encoding='utf-8') as jsonfile:
            jsonfile.write(json.dumps(jsonData, indent=5))

class CSVStateCensus():
    def state_code_csv_convert(csv_code, json_code):
        jsonData = {}
        with open(csv_code, encoding='utf-8') as csvfile:
            csvData = csv.DictReader(csvfile)
            for rows in csvData:
                key = rows['SrNo']
                jsonData[key] = rows

        with open(json_code,'w',encoding='utf-8') as jsonfile:
            jsonfile.write(json.dumps(jsonData,indent=5))
        
if __name__ == '__main__':
    csv_path = r'StateCensusData.csv'
    json_path =r'StateCensusData.json'
    csv_code = r'StateCode.csv'
    json_code =r'StateCode.json'
    StateSensusHandler.state_census_csv_convert(csv_path, json_path)
    CSVStateCensus.state_code_csv_convert(csv_code, json_code)