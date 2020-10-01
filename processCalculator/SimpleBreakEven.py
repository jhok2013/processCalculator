class SimpleBreakEven():
    '''
    Description
    -----------
    A class to provide simple ways to find the break even point
    of two cost processes. Only works for two processes in the 
    comparison. Multiple values can be provided for the variable 
    costs for each process.

    ...

    Attributes
    ----------
    fixed1: float, optional
        First process fixed cost. Default value is 0.00.
    variable1: list of floats, optional
        List of float values that represents variable costs for process 1.
        Default value is [0.00].
    fixed2: float, optional
        Second process fixed cost. Default value is 0.00.
    variable2: list of floats, optional
        List of float values that represents variable costs for process 2
        Default value is [0.00].
    
    Methods
    -------
    calc_simple_be(decimals=2):
        calculates the break even point using the object attributes to 
        the decimal limit used in the arguments
    '''

    fixed1: float
    fixed2: float
    variable1: list
    variable2: list

    def __init__(self, fixed1: float = 0.00,
                       fixed2: float = 0.00,
                       variable1: list = [0.00],
                       variable2: list = [0.00]):
        '''
        Description
        -----------
        Constructs all necessary attributes for the object to function.

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

        self.variable1 = self.__validate(variable1)        
        self.variable2 = self.__validate(variable2)
        self.fixed1 = self.__validate(fixed1)
        self.fixed2 = self.__validate(fixed2)

    def set_fixed1(self, new_fixed1: float):
        '''
        Description
        -----------
        Set the value of the fixed1 attribute to the fixed1 parameter. 

        Parameters
        ----------
        new_fixed1: float, optional
            First process fixed cost. Default is 0.00.
        '''

        self.fixed1 = self.__validate(new_fixed1)

    def set_fixed2(self, new_fixed2: float):
        '''
        Description
        -----------
        Set the value of the fixed2 attribute to the new_fixed2 parameter.

        Parameters
        ----------
        new_fixed2: float, optional
            Second process fixed cost.
        '''

        self.fixed2 = self.__validate(new_fixed2)

    def set_variable1(self, new_variable1: list):
        '''
        Description
        -----------
        Set the value of the variable1 attribute to the new_variable1 parameter

        Parameters
        ----------
        new_variable1: list of floats, optional
            List of float values that represents variable costs for process 1.
            Default is [0.00].
        '''

        self.variable1 = self.__validate(new_variable1)

    def set_variable2(self, new_variable2: list):
        '''
        Description
        -----------
        Set the value of the variable2 attribute to the new_variable2 parameter.

        Parameters
        ----------
        new_variable2: list of floats
            List of float values that represents variable costs for process 2   
            Default is [0.00].
        '''
        
        self.variable2 = self.__validate(new_variable2)
        
    def __valid_type(self, value: any) -> bool:
        '''
        Validate that the input is greater than zero and is a number type.

        Parameters
        ----------
        value: any
            The value to be validated. Needs to only be a number greater than 0.

        Returns
        -------
        result: bool
            Boolean value that indicates whether the input value type was valid.
        '''

        result: any
        value_type: str = str(type(value))
        type_list: list = [
            "<class 'float'>",
            "<class 'int'>"
        ]
        try:
            if value_type in type_list:
                result = True
            else:
                result = False
                raise TypeError
        except Exception:
            raise TypeError
        return result
    
    def __valid_number(self, value: any) -> bool:
        '''
        Validates that the value is greater than 0.

        Parameters
        ----------
        value: any
            The value to be tested. Can be any type but ideally should only be a numeric
            type.

        Returns
        -------
        result: bool
            Boolean value that indicates whether the input value was greater than 0.
        '''
        
        result: bool
        try:
            if value >= 0:
                result = True
            else:
                result = False
                raise ValueError
        except Exception:
            raise ValueError
        return result

    def __validate(self, value: any) -> any:
        '''
        Validates that the input types for the class attributes are valid.
        Attributes are valid if they are of a numeric type and are greater than 0.

        Parameters
        ----------
        value: any
            The value to be tested. Can be of any data type and has no default value.
        
        Returns
        -------
        result: any
            The original input value, assuming it has passed all the tests. Can be of
            any numeric type or a list. 
        '''

        list_type: str = "<class 'list'>"
        value_type: str = str(type(value))
        result: any
        try:
            if value_type == list_type:
                for x in value:
                    if self.__valid_type(x) and self.__valid_number(x):
                        result = value
            else:
                if self.__valid_type(value) and self.__valid_number(value):
                    result = value        
        except Exception:
            raise BaseException
        return result

    def calc_simple_be(self, decimals: int = 2):
        '''
        Description
        -----------
        Calculates the break even point using the object attributes to 
        the decimal limit used in the arguments.

        Parameters
        ----------
        decimals: float, optional
            Amount of decimal places to calculate the break even point.
            Default is 2.

        Returns
        -------
        result: float
            The break even point calculated from the attributes of the object
        '''

        if type(self.variable1) == type(1.00):
            variable1 = self.variable1
        elif type(self.variable1) == type([1.00]):
            variable1 = sum(self.variable1)
        
        if type(self.variable2) == type(1.00):
            variable2 = self.variable2
        elif type(self.variable2) == type([1.00]):
            variable2 = sum(self.variable2)
        
        result: float = round((self.fixed1 - self.fixed2)/(variable2- variable1), decimals)

        return result