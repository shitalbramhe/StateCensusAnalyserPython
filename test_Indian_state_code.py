import unittest
import Indian_state_code
class Test(unittest.TestCase):
    def test_number_records_matches(self):
        result = Indian_state_code.CSVStateCode.count_number_records()
        expected = 30
        self.assertEqual(expected, result)

    def test_file(self):
        result = Indian_state_code.CSVStateCode.check_file()
        expected = "StateCode.csv"
        self.assertEqual(expected, result)
    
    def test_file_extension(self):
        result = Indian_state_code.CSVStateCode.check_file_extension()
        expected = ".csv"
        self.assertEqual(expected, result)

    def test_check_delimiter(self):
        result = Indian_state_code.CSVStateCode.check_delimiter()
        expected = ','
        self.assertEqual(expected, result)

    def test_check_header(self):
        result = Indian_state_code.CSVStateCode.check_header()
        expected = True
        self.assertEqual(expected, result)

if __name__ =='__main__':
    unittest.main()