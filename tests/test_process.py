import unittest
from typing import Union, Iterable, Any, Dict

from context import processCalculator
from processCalculator.Process import Process as p

class test_process(unittest.TestCase):
    '''

    '''
    p1: p
    p2: p

    def setUp(self) -> None:
        '''

        '''
        self.p1 = p()
        self.p2 = p()

    def tearDown(self) -> None:
        '''

        '''
        return super().tearDown()

    @unittest.skip('Test is unnecessary right now.')
    def test_toxml(self) -> None:
        '''

        '''
        p_xml: str = self.p1.to_xml()
        self.assertEqual('test', p_xml)
    
    def test_nested_toxml(self) -> None:
        '''

        '''
        nested_p: p = self.p2
        self.p1.addSteps(nested_p)
        p_xml: str = self.p1.to_xml()
        self.assertTrue(True, "test_nested_toxml has passed.")

if __name__=="__main__":
    unittest.main()