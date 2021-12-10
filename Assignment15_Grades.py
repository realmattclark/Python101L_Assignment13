import unittest
import math
import Grades

class Grade_Test(unittest.TestCase):
    def test_total_returns_total_of_list(self):
        result = Grades.total([1, 10, 22])
        self.assertEqual(result, 33, 'The total function should return 33')

    def test_total_returns_0(self):
        result = Grades.total([])
        self.assertEqual(result, 0, 'The total of the function should return 0')

    def test_average_one(self):
        result = Grades.total([])
        self.assertAlmostEqual(.1 + .2 + .3, 3)
    
    def test_average_two(self):
        result = Grades.total([])
        self.assertAlmostEqual(2, 15, 22, 9)

    def test_average_returns_nan(self):
        result = Grades.total([])
        self.assertNotAlmostEqual([])
        return math.nan


unittest.main()