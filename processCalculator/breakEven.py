class breakEven():
    #Declare properties
    fixed1 = 0
    fixed2 = 0
    variable1 = 0
    variable2 = 0

    #Constuctor method
    def __init__(self, fixed1, fixed2, variable1, variable2):
        self.fixed1 = fixed1
        self.fixed2 = fixed2
        self.variable1 = variable1
        self.variable2 = variable2 

    #Setter methods
    def setFixed1(self, fixed1):
        self.fixed1 = fixed1
    def setFixed2(self, fixed2):
        self.fixed2 = fixed2
    def setVariable1(self, variable1):
        self.variable1 = variable1
    def setVariable2(self, variable2):
        self.variable2 = variable2
    
    #Getter methods
    def getFixed1(self):
        return self.fixed1
    def getFixed2(self):
        return self.fixed2
    def getVariable1(self):
        return self.variable1
    def getVariable2(self):
        return self.variable2
    
    #Calculator methods
    def calcSimpleBE(self, decimals):
        return round((self.fixed1 - self.fixed2)/(self.variable2 - self.variable1), decimals)