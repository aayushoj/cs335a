class ThreeAddressCode:

	def __init__(self):
		self.code = []
		self.quad = -1
		self.nextQuad = 0
		self.labelBase = "l"
		self.labelNo = -1

	def emit(self,dest, src1, src2, op):
		self.code.append([dest,src1,src2,op])
		self.quad += 1
		self.nextQuad += 1
	
	def printCode(self):
		for currInstr in self.code:
			print currInstr

	def patch(self, instrList, label):
		for i in instrList :
			if i < self.nextQuad  and self.code[i][0] == 'goto':
				self.code[i][1] = label

	def makeLabel(self):
		self.labelNo += 1
		return self.labelBase + str(self.labelNo)
