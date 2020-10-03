import unittest
from typing import Union, Iterable, Any, Dict, cast

from context import processcalculator #type: ignore
from processcalculator import SimpleBreakEven #type: ignore

# Declare test data that can be accessed from the test class

TEST_DATA: Any = {
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

class TestBreakEven(unittest.TestCase):
    '''

    '''
    def setUp(self) -> None:
        self.test_break_even = SimpleBreakEven.SimpleBreakEven()
    
    def tearDown(self) -> None:
        self.test_break_even = None

    def test_set_constructor(self):
        '''

        '''
        # Arrange
        test_fixed1: Union[float, int] = TEST_DATA["process1"]["fixed"]
        test_fixed2: Union[float, int] = TEST_DATA["process2"]["fixed"]
        test_variable1: Iterable[Union[float, int]] = TEST_DATA["process1"]["variable"]
        test_variable2: Iterable[Union[float, int]] = TEST_DATA["process2"]["variable"]

        # Act
        sbe: SimpleBreakEven = SimpleBreakEven.SimpleBreakEven(
            fixed1=test_fixed1,
            variable1=test_variable1,
            fixed2=test_fixed2,
            variable2=test_variable2
        )

        # Assert
        self.assertEqual(sbe.fixed1, test_fixed1)
        self.assertEqual(sbe.fixed2, test_fixed2)
        self.assertEqual(sbe.variable1, test_variable1)
        self.assertEqual(sbe.variable2, test_variable2)

    def test_simple_calc(self):
        '''

        '''

        # Arrange
        actual_break_even_point: Union[float, int] = 10.46
        test_fixed1: Union[float, int] = TEST_DATA["process1"]["fixed"]
        test_fixed2: Union[float, int] = TEST_DATA["process2"]["fixed"]
        test_variable1: Iterable[Union[float, int]] = TEST_DATA["process1"]["variable"]
        test_variable2: Iterable[Union[float, int]] = TEST_DATA["process2"]["variable"]

        self.test_break_even.fixed1 = test_fixed1
        self.test_break_even.variable1 = test_variable1
        self.test_break_even.fixed2 = test_fixed2
        self.test_break_even.variable2 = test_variable2

        # Act
        break_even_point: Union[float, int] = self.test_break_even.calc_simple_be()

        # Assert
        self.assertEqual(break_even_point, actual_break_even_point)

if __name__ == "__main__":
    unittest.main() 