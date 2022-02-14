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
            with open("E:\CFP\StateCensusAnalyserPython\StateCensusData.csv","r") as f1:
                csv_reader1 = csv.reader(f1, delimiter=',')
                fields = ['State','Population','TIN','StateCode']
                with open('resultfile.csv','w', newline='') as f3:
                    csv_writer = csv.writer(f3, delimiter=',')
                    csv_writer.writerow(fields)
                    for statecensus_row in csv_reader1:
                        with open("E:\CFP\StateCensusAnalyserPython\StateCode.csv","r") as f2:
                            csv_reader2 = csv.reader(f2, delimiter=',')
                            for statecode_row in csv_reader2:
                                if statecensus_row[0] == statecode_row[1]:
                                    temp = [statecensus_row[0],statecensus_row[1],statecode_row[2],statecode_row[3]] 
                                    csv_writer.writerow(temp)

if __name__ == '__main__':
    StateCensusData.state_census_code_combine()