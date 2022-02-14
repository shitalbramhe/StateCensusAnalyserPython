import unittest
import Merge_two_csv_file

class Test(unittest.TestCase):
    def test_number_records_matches(self):
        result = Merge_two_csv_file.StateCensusData.count_number_records()
        expected = 30
        self.assertEqual(expected, result)

    def test_number_records_not_matches(self):
        result = Merge_two_csv_file.StateCensusData.count_number_records()
        expected = 31
        self.assertEqual(expected, result)

    def test_file_exist(self):
        result = Merge_two_csv_file.StateCensusData.check_file()
        expected = "resultfile.csv"
        self.assertEqual(expected, result)
    
    def test_file_notexist(self):
        result = Merge_two_csv_file.StateCensusData.check_file()
        expected = "file.csv"
        self.assertEqual(expected, result)
    
    def test_file_extension(self):
        result = Merge_two_csv_file.StateCensusData.check_file_extension()
        expected = ".csv"
        self.assertEqual(expected, result)

    def test_file_extension_other(self):
        result = Merge_two_csv_file.StateCensusData.check_file_extension()
        expected = ".json"
        self.assertEqual(expected, result)

    def test_check_delimiter(self):
        result = Merge_two_csv_file.StateCensusData.check_delimiter()
        expected = ','
        self.assertEqual(expected, result)

    def test_check_delimiter_not(self):
        result = Merge_two_csv_file.StateCensusData.check_delimiter()
        expected = '/'
        self.assertEqual(expected, result)    
    
    def test_check_header(self):
        result = Merge_two_csv_file.StateCensusData.check_header()
        expected = True
        self.assertEqual(expected, result)

    def test_check_header_not(self):
        result = Merge_two_csv_file.StateCensusData.check_header()
        expected = False
        self.assertEqual(expected, result)

if __name__ =='__main__':
    unittest.main()