class ThreeAddressCode:

    def __init__(self):
        self.lName = "l"
        self.lNo = -1
        self.code = []

    def emit(self,des, src1, src2, op):
        self.code.append([des,src1,src2,op])
    
    def newLabel(self):
        self.lNo += 1
        return self.lName + str(self.lNo)

    def output(self):
        for i in self.code:
            print i
