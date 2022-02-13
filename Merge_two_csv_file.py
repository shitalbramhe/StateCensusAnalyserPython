"""
@Author: Shital Bajait
@Date: 10-02-2022 11:12:00
@Last Modified by: Shital Bajait 
@Last Modified time: 13-02-2022 13:20:00
@Title : To load StateCensusData and statecodeData to a new file
"""
import csv

class StateCensusData(Exception):

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
                                    csv_writer.writerow({statecensus_row[0]+","+statecensus_row[1]+","+statecode_row[2]+","+statecode_row[3]})

    def count_number_records():
        """
            Description:
                Function to count number of records
            Parameter:
                None
            Return:
                rows of records
        """
        with open('resultfile.csv') as data:
            result_file = csv.reader(data,delimiter=',')
            return(len(list(result_file)))
    
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
            f = open('resultfile.csv')
            f.close()
            return "resultfile.csv"
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
            file = "resultfile.csv"
            result = file.endswith(".csv")
            if result:
                return ".csv"
            else:
                raise(StateCensusData)
        except StateCensusData:
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
        try:
            with open('resultfile.csv') as data:
                dialect = csv.Sniffer().sniff(data.read())
                if dialect.delimiter == ',':
                    return dialect.delimiter
                else:
                    raise(StateCensusData)
        except StateCensusData:
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
        try:
            with open('resultfile.csv') as data:
                headers = csv.Sniffer().has_header(data.read())
                if headers:
                    return headers
                else:
                    raise(StateCensusData)
        except StateCensusData:
            print("headers Not found")

if __name__ == '__main__':
    StateCensusData.state_census_code_combine()
    StateCensusData.count_number_records()
    StateCensusData.check_file()
    StateCensusData.check_file_extension()
    StateCensusData.check_delimiter()
    StateCensusData.check_header()
    