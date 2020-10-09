from typing import Union, MutableSequence, Optional 
from typing import Iterable, Deque, Any, Dict, List, Tuple

from collections import deque

class Process(object):
    '''

    '''
    _process_id: str
    process_name: str
    inputs: List = []
    duration: Union[float, int]
    steps: Iterable[Any] = []
    cycle_time: Union[float, int] = 0
    status: str
    process_children: MutableSequence[Any] = deque()

    def __init__(self, process_name: str = "default process", inputs: List = [],
                       duration: Union[float, int] = 0, steps: Iterable[Any] = [],
                       process_xml: Any = None, process_json: Any = None):
        '''

        '''
        self.process_name = process_name
        self.inputs = inputs
        self.duration = duration
        self._process_id = self.__get_hash(self.process_name, self.duration)
        self.status = "READY"
        if steps:
            for step in steps:
                if str(type(step)) == "<class 'processCalculator.Process.Process'>":
                    self.process_children.append(step._process_id)
                else:
                    raise Exception('Invalid step type. Must be Process object.')
    
    def __get_hash(self, process_name: str, duration: Union[float, int]) -> str:
        '''

        '''
        from hashlib import sha224
        from random import seed, randint
        seed()
        encoded: bytes = f"{process_name}{duration}-{randint(1, 10000)}".encode('utf-8')
        hash: str = sha224(encoded).hexdigest()
        return hash

    def addSteps(self, *child_processes):
        '''

        '''
        for child_process in child_processes:
            if str(type(child_process)) == "<class 'processCalculator.Process.Process'>":
                if child_process.process_children:
                    for grandchild in child_process.process_children:
                        if grandchild in self.process_children:
                            self.process_children.remove(grandchild)
                            break
                if child_process._process_id != self._process_id:
                    self.process_children.append(child_process._process_id)
                    self.steps.append(child_process)
                else:
                    pass
            else:
                raise Exception('Invalid step type. Must be Process object.')

    def to_xml(self) -> str:
        '''

        '''
        input_str: str = ''.join(['<inputs>', str([''.join(['<input>', x, '</input>']) for x in self.inputs]).translate({ord(i): None for i in ' [],\''}), '</inputs>']) if self.inputs else ''

        child_process_str: str = ''.join([
            "<process_children>",
            str([''.join(['<process_child_id>', x, '</process_child_id>']) for x in self.process_children]).translate(
            {ord(i): None for i in ' [],\''}),
            "</process_children>"
        ]) if self.process_children and self._process_id not in self.process_children else ''

        steps_str: str = ''.join([
            '<steps>',
            str([
                ''.join([
                    '<step>',
                    x.to_xml(),
                    '</step>'
                ])
            for x in self.steps if x._process_id in self.process_children and self._process_id not in self.process_children]),
            '</steps>'
        ]).translate(
            {ord(i): None for i in ' [],\''}
        ) if self.steps and self._process_id not in self.process_children else ''

        xml_packet: str = (
            f"<process>"
            f"<process_id>{self._process_id}</process_id>"
            f"<process_name>{self.process_name}</process_name>"
            f"<duration>{self.duration}</duration>"
            f"<status>{self.status}</status>"
            f"<cycle_time>{self.cycle_time}</cycle_time>"
            f"{input_str}"
            f"{child_process_str}"
            f"{steps_str}"
            f"</process>"
        )

        return xml_packet

    def to_json(self) -> str:
        '''

        '''
        json_packet: str = ''
        return json_packet