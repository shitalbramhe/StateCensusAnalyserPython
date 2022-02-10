import unittest
import IndianStateCensusAnalyser
class Test(unittest.TestCase):
    def test_number_records_matches(self):
        result = IndianStateCensusAnalyser.StateCensusAnalyser.count_number_records()
        expected = 30
        self.assertEqual(expected, result)

if __name__ =='__main__':
    unittest.main()