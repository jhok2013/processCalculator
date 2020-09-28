class SimpleBreakEven():

    def __init__(self, fixed1 = 0, fixed2 = 0, variable1 = [0], variable2 = [0]):

        self.variable1 = variable1        
        self.variable2 = variable2
        self.fixed1 = fixed1
        self.fixed2 = fixed2

    def set_fixed1(self, fixed1):
        self.fixed1 = fixed1

    def set_fixed2(self, fixed2):
        self.fixed2 = fixed2

    def set_variable1(self, variable1):
        self.variable1 = variable1

    def set_variable2(self, variable2):
        self.variable2 = variable2
        
    #Calculator methods
    def calc_simple_be(self, decimals = 2):

        if type(self.variable1) == type(1.00):
            variable1 = self.variable1
        elif type(self.variable1) == type([1.00]):
            variable1 = sum(self.variable1)
        
        if type(self.variable2) == type(1.00):
            variable2 = self.variable2
        elif type(self.variable2) == type([1.00]):
            variable2 = sum(self.variable2)

        return round((self.fixed1 - self.fixed2)/(variable2- variable1), decimals)