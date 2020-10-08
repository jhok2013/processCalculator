from typing import Union, MutableSequence, Optional 
from typing import Iterable, Deque, Any, Dict, List

from collections import deque

class Process(object):
    '''

    '''
    _process_id: str
    process_name: str
    inputs: List = []
    duration: Union[float, int]
    steps: Iterable[Any] = []
    parent_process_ids: Iterable[str] = []
    cycle_time: Union[float, int] = 0
    status: str

    def __init__(self, process_name: str = "default process", inputs: List = [],
                       duration: Union[float, int] = 0, steps: Iterable[Any] = [],
                       process_xml: Any = None, process_json: Any = None):
        '''

        '''
        self.process_name = process_name
        self.inputs = inputs
        self.duration = duration
        self.steps = steps
        self._process_id = self.__get_hash(self.process_name, self.duration)
        self.status = "READY"
    
    def __get_hash(self, process_name: str, duration: Union[float, int]) -> str:
        '''

        '''
        from hashlib import sha224
        from random import seed, randint
        seed()
        encoded: bytes = f"{process_name}{duration}-{randint(1, 10000)}".encode('utf-8')
        hash: str = sha224(encoded).hexdigest()
        return hash

    def to_xml(self) -> str:
        '''

        '''
        xml_packet: str = ''
        xml_deque: Iterable[Any] = deque()
        xml_tags: Dict[str, str] = {
            "process_tag":("<process>", "</process>"),
            "_process_id":("<_process_id>", "</_process_id>"),
            "process_name":("<process_name>", "</process_name>"),
            "inputs":("<inputs>", "</inputs>"),
            "input":("<input>", "</input>"),
            "duration":("<duration>", "</duration>"),
            "steps":("<steps>", "</steps>"),
            "step":("<step>", "</step>"),
            "parent_process_ids":("<parent_process_ids>", "</parent_process_ids>"),
            "parent_process_id":("<parent_process_id>", "</parent_process_id>"),
            "cycle_time":("<cycle_time>","</cycle_time>"),
            "status":("<status>", "</status>")
        }
        xml_deque.append(xml_tags["process_tag"][0])
        xml_deque.append(xml_tags["_process_id"][0])
        xml_deque.append(self._process_id)
        xml_deque.append(xml_tags["_process_id"][1])
        xml_deque.append(xml_tags["process_name"][0])
        xml_deque.append(self.process_name)
        xml_deque.append(xml_tags["process_name"][1])
        xml_deque.append(xml_tags["inputs"][0])
        xml_deque.append(xml_tags["input"][0])
        for input in self.inputs:
            xml_deque.append(str(input))
        xml_deque.append(xml_tags["input"][1])
        xml_deque.append(xml_tags["inputs"][1])
        xml_deque.append(xml_tags["duration"][0])
        xml_deque.append(str(self.duration))
        xml_deque.append(xml_tags["duration"][1])
        xml_deque.append(xml_tags["steps"][0])
        for step in self.steps:
            xml_deque.append(xml_tags["step"][0])
            
            xml_deque.append(xml_tags["step"][1])
        xml_deque.append(xml_tags["steps"][1])
        xml_deque.append(xml_tags["process_tag"][1])
        
        return xml_packet

    def to_json(self) -> str:
        '''

        '''
        json_packet: str = ''
        return json_packet