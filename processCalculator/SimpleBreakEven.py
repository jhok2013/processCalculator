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

    def __init__(self, fixed1=0, fixed2=0, variable1=[0], variable2=[0]):
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

        self.variable1 = variable1        
        self.variable2 = variable2
        self.fixed1 = fixed1
        self.fixed2 = fixed2

    def set_fixed1(self, new_fixed1):
        '''
        Description
        -----------
        Set the value of the fixed1 attribute to the fixed1 parameter. 

        Parameters
        ----------
        new_fixed1: float, optional
            First process fixed cost. Default is 0.00.
        '''

        self.fixed1 = new_fixed1

    def set_fixed2(self, new_fixed2):
        '''
        Description
        -----------
        Set the value of the fixed2 attribute to the new_fixed2 parameter.

        Parameters
        ----------
        new_fixed2: float, optional
            Second process fixed cost.
        '''

        self.fixed2 = new_fixed2

    def set_variable1(self, new_variable1):
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

        self.variable1 = new_variable1

    def set_variable2(self, new_variable2):
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
        
        self.variable2 = new_variable2
        
    def calc_simple_be(self, decimals=2):
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
        
        result = round((self.fixed1 - self.fixed2)/(variable2- variable1), decimals)

        return result