"""
@Author: Shital Bajait
@Date: 08-02-2022 13:12:00
@Last Modified by: Shital Bajait 
@Last Modified time: 08-02-2022 13:12:00
@Title : To load CSV Data
"""

import csv

class StateCensusAnalyser:
    def state_census():
        with open("E:\CFP\StateCensusAnalyserPython\StateCensusData.csv","r") as data:
            statecensus = csv.reader(data, delimiter=',')
            for i in statecensus:
                print(i)

    def count_number_records():
        with open("E:\CFP\StateCensusAnalyserPython\StateCensusData.csv") as data:
            statecensus = csv.reader(data, delimiter=',')
            return len(list(statecensus))

class CSVStates:
    def state_code():
        with open("E:\CFP\StateCensusAnalyserPython\StateCode.csv", "r") as data:
            statecode = csv.reader(data, delimiter=',')
            for i in statecode:
                print(i)

    def count_number_records():
        with open("E:\CFP\StateCensusAnalyserPython\StateCode.csv") as data:
            statecode = csv.reader(data, delimiter=',')
            return (len(list(statecode)))

if __name__ == '__main__':
    StateCensusAnalyser.state_census()
    print(StateCensusAnalyser.count_number_records())
    CSVStates.state_code()
    print(CSVStates.count_number_records())