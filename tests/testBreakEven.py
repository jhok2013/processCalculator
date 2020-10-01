import unittest

from context import processcalculator
from processcalculator import SimpleBreakEven

# Declare test data that can be accessed from the test class

TEST_DATA: dict = {
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
    
SBE: SimpleBreakEven = SimpleBreakEven.SimpleBreakEven()

class TestBreakEven(unittest.TestCase):
    '''

    '''

    def test_setter_methods(self):
        '''

        '''

        # Arrange
        test_fixed1: float = TEST_DATA["process1"]["fixed"]
        test_fixed2: float = TEST_DATA["process2"]["fixed"]
        test_variable1: float = TEST_DATA["process1"]["variable"][0]
        test_variable2: float = TEST_DATA["process2"]["variable"][0]

        #Act
        SBE.set_fixed1(test_fixed1)
        SBE.set_fixed2(test_fixed2)
        SBE.set_variable1(test_variable1)
        SBE.set_variable2(test_variable2)

        #Assert
        self.assertEqual(SBE.fixed1, test_fixed1)
        self.assertEqual(SBE.fixed2, test_fixed2)
        self.assertEqual(SBE.variable1, test_variable1)
        self.assertEqual(SBE.variable2, test_variable2)

    def test_set_constructor(self):
        '''

        '''

        # Arrange
        test_fixed1: float = TEST_DATA["process1"]["fixed"]
        test_fixed2: float = TEST_DATA["process2"]["fixed"]
        test_variable1: float = TEST_DATA["process1"]["variable"][0]
        test_variable2: float = TEST_DATA["process2"]["variable"][0]


        # Act
        SBE = SimpleBreakEven.SimpleBreakEven(
            fixed1=test_fixed1,
            variable1=test_variable1,
            fixed2=test_fixed2,
            variable2=test_variable2
        )

        # Assert
        self.assertEqual(SBE.fixed1, test_fixed1)
        self.assertEqual(SBE.fixed2, test_fixed2)
        self.assertEqual(SBE.variable1, test_variable1)
        self.assertEqual(SBE.variable2, test_variable2)

    def test_simple_calc_single_value(self):
        '''

        '''

        # Arrange
        actual_break_even_point: float = 12.39
        SBE = SimpleBreakEven.SimpleBreakEven(
            fixed1=TEST_DATA["process1"]["fixed"],
            variable1=TEST_DATA["process1"]["variable"][0],
            fixed2=TEST_DATA["process2"]["fixed"],
            variable2=TEST_DATA["process2"]["variable"][0]
        )

        # Act
        break_even_point: float = SBE.calc_simple_be()

        # Assert
        self.assertEqual(break_even_point, actual_break_even_point)

    def test_simple_calc_multiple_values(self):
        '''

        '''

        # Arrange
        actual_break_even_point: float = 10.46
        SBE = SimpleBreakEven.SimpleBreakEven(
            fixed1=TEST_DATA["process1"]["fixed"],
            variable1=TEST_DATA["process1"]["variable"],
            fixed2=TEST_DATA["process2"]["fixed"],
            variable2=TEST_DATA["process2"]["variable"]
        )

        # Act
        break_even_point: float = SBE.calc_simple_be()
        
        # Assert
        self.assertEqual(break_even_point, actual_break_even_point)

if __name__ == "__main__":
    unittest.main() 