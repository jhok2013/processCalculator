import unittest

from context import processcalculator
from processcalculator import SimpleBreakEven

class TestBreakEven(unittest.TestCase):

    def test_setter_methods(self):

        #Arrange
        data = {
            "process1": {
                "fixed": 122.00,
                "variable": [34.00]
            },
            "process2": {
                "fixed": 353.22,
                "variable": [15.34]
            }
        }
        be = SimpleBreakEven.SimpleBreakEven()

        #Act
        be.set_fixed1(data["process1"]["fixed"])
        be.set_variable1(data["process1"]["variable"][0])
        be.set_fixed2(data["process2"]["fixed"])
        be.set_variable2(data["process2"]["variable"][0])

        fixed1 = be.fixed1
        variable1 = be.variable1
        fixed2 = be.fixed2
        variable2 = be.variable2

        #Assert
        self.assertEqual(fixed1, data["process1"]["fixed"]) 
        self.assertEqual(variable1, data["process1"]["variable"][0]) 
        self.assertEqual(fixed2, data["process2"]["fixed"]) 
        self.assertEqual(variable2, data["process2"]["variable"][0]) 

    def test_set_constructor(self):

        # Arrange
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

        # Act
        be = SimpleBreakEven.SimpleBreakEven(
            fixed1=data["process1"]["fixed"],
            variable1=data["process1"]["variable"],
            fixed2=data["process2"]["fixed"],
            variable2=data["process2"]["variable"]
        )

        # Assert
        self.assertEqual(be.variable1, data["process1"]["variable"])
        self.assertEqual(be.variable2, data["process2"]["variable"])

    def test_simple_calc_single_value(self):

        # Arrange
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
        be = SimpleBreakEven.SimpleBreakEven(
            fixed1=data["process1"]["fixed"],
            variable1=data["process1"]["variable"][0],
            fixed2=data["process2"]["fixed"],
            variable2=data["process2"]["variable"][0]
        )

        # Act
        bePoint = be.calc_simple_be()

        # Assert
        self.assertEqual(bePoint, actualBePoint)

    def test_simple_calc_multiple_values(self):

        # Arrange
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
        be = SimpleBreakEven.SimpleBreakEven(
            fixed1=data["process1"]["fixed"],
            variable1=data["process1"]["variable"],
            fixed2=data["process2"]["fixed"],
            variable2=data["process2"]["variable"]
        )

        # Act
        bePoint = be.calc_simple_be()
        
        # Assert
        self.assertEqual(bePoint, actualBePoint)

if __name__ == "__main__":
    unittest.main() 