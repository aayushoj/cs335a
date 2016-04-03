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

	def output3AC(self):
		count =0
		for i in self.code:
			# print(i[3])
			count+=1
			if(i[0]=='ifgoto'):
				print(str(count)+", ")
			elif(i[0]=='goto'):
				print(str(count)+", goto, "+i[1])
			elif(i[0]=='label'):
				print(str(count)+", label, "+i[1])
			elif(i[0]=='func'):
				print(str(count)+", func")
			elif(i[0]=='declare'):
				print(str(count)+", ")
			elif(i[0]=='error'):
				print(str(count)+", ")
			elif(i[0]=='ret'):
				print(str(count)+", ret")
			else:
				if(i[3]=='='):
					print(str(count)+", "+i[3]+", "+i[0]+", "+i[1])
				else:
					print(str(count)+", "+i[3]+", "+i[0]+", "+i[1]+", "+i[2])
