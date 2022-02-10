"""
@Author: Shital Bajait
@Date: 08-02-2022 13:12:00
@Last Modified by: Shital Bajait 
@Last Modified time: 10-02-2022 11:40:00
@Title : Given file type incorrect Returns a custom Exception
"""

import csv

class StateCensusAnalyser(Exception):
    def state_census():
        """
            Description:
                Function to load StateCensusData file
            Parameter:
                None
            Return:
                None
        """
        with open("E:\CFP\StateCensusAnalyserPython\StateCensusData.csv","r") as data:
            statecensus = csv.reader(data, delimiter=',')
            for i in statecensus:
                print(i)

    def count_number_records():
        """
            Description:
                Function to count number of records
            Parameter:
                None
            Return:
                rows of records
        """
        with open("E:\CFP\StateCensusAnalyserPython\StateCensusData.csv") as data:
            statecensus = csv.reader(data, delimiter=',')
            return len(list(statecensus))

    def check_file():
        """
            Description:
                Function to ccheck file is exist or not
            Parameter:
                None
            Return:
                None
        """
        try:
            f = open("E:\CFP\StateCensusAnalyserPython\StateCensusData.csv")
            f.close()
            return "StateCensusData.csv"
        except Exception:
            print("Sorry file does not exist")
    
    def check_file_extension():
        """
            Description:
                Function to check csv file exists or not
            Parameter:
                None
            Return:
                .csv
        """
        try:
            file = "StateCensusData.csv"
            result = file.endswith(".csv")
            if result:
                return ".csv"
            else:
                raise(StateCensusAnalyser)
        except StateCensusAnalyser:
            print("Sorry! CSV file does not exist")


if __name__ == '__main__':
    StateCensusAnalyser.state_census()
    print(StateCensusAnalyser.count_number_records())
    StateCensusAnalyser.check_file()
    StateCensusAnalyser.check_file_extension()