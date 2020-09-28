from context import processcalculator
from processcalculator import breakEven
import unittest

class testBreakEven(unittest.TestCase):
    def test_setterMethods(self):
        #Arrange
        data = {
            "process1": {
                "fixed": 122.00,
                "variable": [34.00]
            },
            "process2": {
                "fixed": 353.22,
                "variable": [
                    15.34
                ]
            }
        }
        be = breakEven.breakEven()
        #Act
        be.setFixed1(data["process1"]["fixed"])
        be.setVariable1(data["process1"]["variable"][0])
        be.setFixed2(data["process2"]["fixed"])
        be.setVariable2(data["process2"]["variable"][0])
        fixed1      = be.fixed1
        variable1   = be.variable1
        fixed2      = be.fixed2
        variable2   = be.variable2
        #Assert
        self.assertEqual(fixed1, data["process1"]["fixed"]) 
        self.assertEqual(variable1, data["process1"]["variable"][0]) 
        self.assertEqual(fixed2, data["process2"]["fixed"]) 
        self.assertEqual(variable2, data["process2"]["variable"][0]) 

    def test_setvarlist_multipleCosts(self):
        #Create test data
        data = {
            "process1": {
                "fixed": 122.00,
                "variable": [
                    34.00,
                    22.34,
                    3.86
                ]
            },
            "process2": {
                "fixed": 353.22,
                "variable": [
                    15.34,
                    18.20,
                    4.55
                ]
            }
        }       
        # Populate breakEven calculator
        be = breakEven.breakEven(
            fixed1      =data["process1"]["fixed"],
            variable1   =data["process1"]["variable"],
            fixed2      =data["process2"]["fixed"],
            variable2   =data["process2"]["variable"]
        )
        # Assert
        self.assertEqual(be.variable1, data["process1"]["variable"])
        self.assertEqual(be.variable2, data["process2"]["variable"])

    def test_calcBE_singleVal(self):
        #Create test data
        data = {
            "process1": {
                "fixed": 122.00,
                "variable": [
                    34.00,
                    22.34,
                    3.86
                ]
            },
            "process2": {
                "fixed": 353.22,
                "variable": [
                    15.34,
                    18.20,
                    4.55
                ]
            }
        }       
        actualBePoint = 12.39
        # Populate breakEven calculator
        be = breakEven.breakEven(
            fixed1      =data["process1"]["fixed"],
            variable1   =data["process1"]["variable"][0],
            fixed2      =data["process2"]["fixed"],
            variable2   =data["process2"]["variable"][0]
        )
        #Calculate break even
        bePoint = be.calcSimpleBE()
        self.assertEqual(bePoint, actualBePoint)

    def test_calcBE_multipleValues(self):
        #Create test data
        data = {
            "process1": {
                "fixed": 122.00,
                "variable": [
                    34.00,
                    22.34,
                    3.86
                ]
            },
            "process2": {
                "fixed": 353.22,
                "variable": [
                    15.34,
                    18.20,
                    4.55
                ]
            }
        }       
        actualBePoint = 10.46
        # Populate breakEven calculator
        be = breakEven.breakEven(
            fixed1      =data["process1"]["fixed"],
            variable1   =data["process1"]["variable"],
            fixed2      =data["process2"]["fixed"],
            variable2   =data["process2"]["variable"]
        )
        #Calculate break even
        bePoint = be.calcSimpleBE()
        self.assertEqual(bePoint, actualBePoint)

if __name__ == "__main__":
    unittest.main() 