"""
@Author: Shital Bajait
@Date: 10-02-2022 11:12:00
@Last Modified by: Shital Bajait 
@Last Modified time: 10-02-2022 02:27:00
@Title : To load StateCensusData and statecodeData to a new file
"""
import csv

class StateCensusData():

    def state_census_code_combine():
            """
                Description:
                    Function to load StateCensusData and statecodeData to a new file
                Parameter:
                    None
                Return:
                    None
            """
            files = ["E:\CFP\StateCensusAnalyserPython\StateCensusData.csv","E:\CFP\StateCensusAnalyserPython\StateCode.csv"]
            for file in files:
                with open(file,"r") as f1:
                    csv_reader = csv.reader(f1, delimiter=',')
                    with open('resultfile.csv','a', newline='') as f2:
                        csv_writer = csv.writer(f2, delimiter=',')
                        for row in csv_reader:
                            csv_writer.writerow(row)

if __name__ == '__main__':
    StateCensusData.state_census_code_combine()