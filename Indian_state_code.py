"""
@Author: Shital Bajait
@Date: 10-02-2022 23:45:00
@Last Modified by: Shital Bajait 
@Last Modified time: 10-02-2022 23:45:00
@Title : load Indian States Code Information from a csv file and test cases
"""

import csv

class CSVStateCode(Exception):
    def state_code():
        """
            Description:
                Function to load StateCode file
            Parameter:
                None
            Return:
                None
        """
        with open("E:\CFP\StateCensusAnalyserPython\StateCode.csv","r") as data:
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
        with open("E:\CFP\StateCensusAnalyserPython\StateCode.csv") as data:
            statecode = csv.reader(data, delimiter=',')
            return len(list(statecode))

    def check_file():
        """
            Description:
                Function to check file is exist or not
            Parameter:
                None
            Return:
                None
        """
        try:
            f = open("E:\CFP\StateCensusAnalyserPython\StateCode.csv")
            f.close()
            return "StateCode.csv"
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
            file = "StateCode.csv"
            result = file.endswith(".csv")
            if result:
                return ".csv"
            else:
                raise(CSVStateCode)
        except CSVStateCode:
            print("Sorry! CSV file does not exist")

    def check_delimiter():
        """
            Description:
                Function to check delimiter is correct or not
            Parameter:
                None
            Return:
                delimiter
        """
        with open("E:\CFP\StateCensusAnalyserPython\StateCode.csv", newline="") as data:
            try:
                dialect = csv.Sniffer().sniff(data.read())
                if dialect.delimiter != ',':
                    return dialect.delimiter
                else:
                    raise(CSVStateCode)
            except CSVStateCode:
                print("Incorrect delimiter found")

    def check_header():
        """
            Description:
                Function to check header is present or not
            Parameter:
                None
            Return:
                .csv
        """
        with open("E:\CFP\StateCensusAnalyserPython\StateCode.csv") as data:
            try:
                headers = csv.Sniffer().has_header(data.read())
                if headers:
                    return headers
                else:
                    raise(CSVStateCode)
            except CSVStateCode:
                print("headers is not found")


if __name__ == '__main__':
    CSVStateCode.state_code()
    print(CSVStateCode.count_number_records())
    CSVStateCode.check_file()
    CSVStateCode.check_file_extension()
    CSVStateCode.check_delimiter()
    CSVStateCode.check_header()