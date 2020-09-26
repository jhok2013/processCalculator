from context import processCalculator
from processCalculator import breakEven
import unittest

class testBreakEven(unittest.TestCase):
    def test_calcSimpleBE(self):
        #Create test data
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
        # Populate breakEven calculator
        be = breakEven.breakEven(
            fixed1      =data["process1"]["fixed"],
            variable1   =data["process1"]["variable"][0],
            fixed2      =data["process2"]["fixed"],
            variable2   =data["process2"]["variable"][0]
        )
        bePoint = be.calcSimpleBE(2) 

if __name__ == "__main__":
    unittest.main() 