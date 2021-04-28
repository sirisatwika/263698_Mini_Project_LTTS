import unittest
import physicsFormulaCalculator

class TestCalc(unittest.TestCase):
    def test_bmicalc(self):
        res = physicsFormulaCalculator.bmicalci(167.64,63)
        self.assertEqual(res,22.41740020670124)

    def test_celciustofarenheit(self):
        res = physicsFormulaCalculator.celciustofarenheit(63)
        self.assertEqual(res,17.22222222222222)

    def test_farenheittocelius(self):
        res = physicsFormulaCalculator.farenheittocelius(100)
        self.assertEqual(res,212.0)

    def test_cal_speed(self):
        res = physicsFormulaCalculator.cal_speed(125,60)
        self.assertEqual(res,2.0833333333333335)

    def test_cal_acceleration(self):
        res = physicsFormulaCalculator.cal_acceleration(3,5,5)
        self.assertEqual(res,0.4)

    
