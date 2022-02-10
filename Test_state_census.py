import unittest
import IndianStateCensusAnalyser
class Test(unittest.TestCase):
    def test_number_records_matches(self):
        result = IndianStateCensusAnalyser.StateCensusAnalyser.count_number_records()
        expected = 30
        self.assertEqual(expected, result)

    def test_file(self):
        result = IndianStateCensusAnalyser.StateCensusAnalyser.check_file()
        expected = "StateCensusData.csv"
        self.assertEqual(expected, result)
    
    def test_file_extension(self):
        result = IndianStateCensusAnalyser.StateCensusAnalyser.check_file_extension()
        expected = ".csv"
        self.assertEqual(expected, result)


if __name__ =='__main__':
    unittest.main()