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

    def test_cal_density(self):
        res = physicsFormulaCalculator.cal_density(168,29)
        self.assertEqual(res,5.793103448275862)
        
    def test_cal_force(self):
        res = physicsFormulaCalculator.cal_force(50,5)
        self.assertEqual(res,250.0)

    def test_cal_power(self):
        res = physicsFormulaCalculator.cal_power(300,10)
        self.assertEqual(res,30.0)
    
    def test_cal_weight(self):
        res = physicsFormulaCalculator.cal_weight(60,1.625)
        self.assertEqual(res,97.5)

    def test_cal_pressure(self):
        res = physicsFormulaCalculator.cal_pressure(50,20)
        self.assertEqual(res,2.5)

    def test_cal_Kineticenergy(self):
        res = physicsFormulaCalculator.cal_Kineticenergy(60,6)
        self.assertEqual(res,1080.0)
    
    def test_cal_ohmslaw(self):
        res = physicsFormulaCalculator.cal_ohmslaw(50,4)
        self.assertEqual(res,200.0)

    def test_cal_frequency(self):
        res = physicsFormulaCalculator.cal_frequency(70,15)
        self.assertEqual(res,4.666666666666667)

    def test_capacitance(self):
        res = physicsFormulaCalculator.capacitance(50,6)
        self.assertEqual(res,8.333333333333334) 

    def test_gravity(self):
        res = physicsFormulaCalculator.gravity(70,80,20)
        self.assertEqual(res,280.0)

    def test_con_kmph_ms(self):
        res = physicsFormulaCalculator.con_kmph_ms(40)
        self.assertEqual(res,11.1111111108) 

    def test_con_ms_kmph(self):
        res = physicsFormulaCalculator.con_ms_kmph(40)
        self.assertEqual(res,144.0)


    


    




    
