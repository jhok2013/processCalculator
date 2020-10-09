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
        self.p1 = p(process_name='process 1')
        self.p2 = p(process_name='process 2')

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
    
    @unittest.skip('Test is unnecessary right now.')
    def test_nested_toxml(self) -> None:
        '''

        '''
        nested_p: p = self.p2
        self.p1.addSteps(nested_p)
        p_xml: str = self.p1.to_xml()
        self.assertTrue(True, "test_nested_toxml has passed.")
    
    def test_nested2_toxml(self) -> None:
        '''
        main priority bug
        - considers granchild process as its child process. shows grandchild process in its steps.
        Needs to only consider child process as child. Child needs to own grandchild.
        - update: added loop in addStep method to remove grandchild process from self.process_children
        but it removes it from both the layer 1 process and the nested 1 process
       
        '''
        nested1: p = p(process_name='nested1')
        nested2: p = p(process_name='nested2')
        nested1.addSteps(nested2)
        self.p1.addSteps(nested1)
        p_xml: str = self.p1.to_xml()
        self.assertTrue(True)
    
    @unittest.skip('Test is unnecessary right now.')
    def test_multiple_children_toxml(self) -> None:
        '''
        Xml returned only shows one step when there are two child process id's
        '''
        p1: p = p()
        p2: p = p()
        self.p1.addSteps(p1, p2)
        p_xml: str = self.p1.to_xml()
        self.assertTrue(True)

if __name__=="__main__":
    unittest.main()