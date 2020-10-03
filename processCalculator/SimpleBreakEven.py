from typing import Union, Any, Iterable

class SimpleBreakEven():
    '''
    Description
    -----------
    A class to provide simple ways to find the break even point
    of two cost processes. Only works for two processes in the 
    comparison.

    ...

    Attributes
    ----------
    fixed1: Union[float, int], optional
        First process fixed cost. Default value is 0.00.
    variable1: Iterable[Union[float, int]], optional
        List of float values that represents variable costs for process 1.
        Default value is [0.00].
    fixed2: Union[float, int], optional
        Second process fixed cost. Default value is 0.00.
    variable2: Iterable[Union[float, int]], optional
        List of float values that represents variable costs for process 2
        Default value is [0.00].
    
    Methods
    -------
    calc_simple_be(decimals=2):
        calculates the break even point using the object attributes to 
        the decimal limit used in the arguments
    '''

    fixed1: Union[float, int]
    fixed2: Union[float, int]
    variable1: Iterable[Union[float, int]]
    variable2: Iterable[Union[float, int]]

    def __init__(self, fixed1: Union[float, int] = 0.00,
                       variable1: Iterable[Union[float, int]] = [0.00],
                       fixed2: Union[float, int] = 0.00,
                       variable2: Iterable[Union[float, int]] = [0.00]):
        '''
        Private. Constructs all necessary attributes for the object to function.

        Parameters
        ----------
        fixed1: float, optional
            First process fixed cost. Default is 0.00.
        variable1: list of floats, optional
            List of float values that represents variable costs for process 1.
            Default is [0.00].
        fixed2: float, optional
            Second process fixed cost.
        variable2: list of floats, optional
            List of float values that represents variable costs for process 2.
            Default is [0.00].
        '''
        self.variable1 = self.__validate_variable(variable1)        
        self.variable2 = self.__validate_variable(variable2)
        self.fixed1 = self.__validate_fixed(fixed1)
        self.fixed2 = self.__validate_fixed(fixed2)
    
    def __call__(self, fixed1: Union[float, int] = 0.00,
                       variable1: Iterable[Union[float, int]] = [0.00],
                       fixed2: Union[float, int] = 0.00,
                       variable2: Iterable[Union[float, int]] = [0.00]):
        '''
        Private. Allows the object to be callable.
        '''
        call_self: SimpleBreakEven = SimpleBreakEven(fixed1=fixed1, fixed2=fixed2, variable1=variable1, variable2=variable2) 
        return call_self

    
    def __validate_variable(self, value: Iterable[Union[float, int]]) -> Iterable[Union[float, int]]:
        '''
        Private. Validates all values within the variable cost list.

        Parameters
        ----------
        value: Iterable[Union[float, int]]
            The variable cost list to be used in further calculations
        
        Returns
        -------
        result: Iterable[Union[float, int]]
            The original value passed in
        '''
        result = [x for x in value if self.__valid_number(x)]
        return result

    def __valid_number(self, value: Union[float, int]) -> bool:
        '''
        Private. Validates that the value is greater than 0.
        Raises a special exception if the value is not.

        Parameters
        ----------
        value: Union[float ,int]
            The value to be tested. Can be any type but ideally should only be a numeric
            type.

        Returns
        -------
        result: bool
            Boolean value that indicates whether the input value was greater than 0.
        '''
        result: bool = True if value >= 0 else False
        if not result:
            raise Exception('Invalid number. Only positive float or ints permitted.')
        return result

    def __validate_fixed(self, value: Union[float, int]) -> Union[float, int]:
        '''
        Private. Validates that the fixed value is greater than or equal to 0.

        Parameters
        ----------
        value: Union[float, int]
            The value to be tested. Can be of any data type and has no default value.
        
        Returns
        -------
        result: Union[float, int]
            The original input value, assuming it has passed all the tests. Can be of
            any numeric type. 
        '''
        result: Union[float, int] = value if self.__valid_number(value) else 0
        return result

    def calc_simple_be(self, decimals: int = 2) -> Union[float, int]:
        '''
        Description
        -----------
        Calculates the break even point using the object attributes to 
        the decimal limit used in the arguments.

        Parameters
        ----------
        decimals: int, optional
            Amount of decimal places to calculate the break even point.
            Default is 2.

        Returns
        -------
        result: Union[float, int]
            The break even point calculated from the attributes of the object
        '''
        variable1: Union[float, int] = sum(self.variable1)
        variable2: Union[float, int] = sum(self.variable2)
        result: Union[float, int] = round((self.fixed1 - self.fixed2)/(variable2- variable1), decimals)
        return result