import sys
class instruction(object):
    def convert(self, param):
        self.lineno=param[0]
        self.op=param[1]
        if (param[1]=="ifgoto"):
            self.jmp=True
            self.cmpl=True
            self.cmpltype=param[2]
            self.src1=param[3]
            self.src2=param[4]
            self.jlno=param[5]
        elif (param[1]=="call"):
            self.func=True
            self.funcname=param[2]
        elif (param[1]=="ret"):
            self.returnc=True
        elif (param[1]=="label"):
            self.lbl=True
            self.lblname=param[2]
        elif (param[1]=="print"):
            self.printc=True
            self.src1=param[2]
        elif (param[1]=="="):
            self.dst=param[2]
            self.src1=param[3]
        else:
            self.dst=param[2]
            self.src1=param[3]
            self.src2=param[4]

    def printobj(self):
        print("line no: "+self.lineno)
        print("op: "+self.op)
        print("dst: "+str(self.dst))
        print("src1: "+str(self.src1))
        print("src2: "+str(self.src2))
        print("jmp: "+str(self.jmp))
        print("cmpl: "+str(self.cmpl))
        print("cmpltype: "+str(self.cmpltype))
        print("jlno: "+str(self.jlno))
        print("lbl: "+str(self.lbl))
        print("lblname: "+str(self.lblname))
        print("func: "+str(self.func))
        print("funcname: "+str(self.funcname))
        print("print: "+str(self.printc))
        print("input: "+str(self.inputc))
        print("return: "+str(self.returnc))
        print("\n")

    def __init__(self):
        self.lineno=0
        self.op=None             #operator
        self.dst=None            #destination
        self.src1=None           #source1
        self.src2=None           #source2
        self.jmp=False           #if jump or not
        self.cmpl=False          #if compare or not
        self.cmpltype=None
        self.jlno=0              #line number to jump to
        self.lbl=False           #label of a function
        self.lblname=None        #Name of label
        self.func=False
        self.funcname=None
        self.printc=False        #If we have to print or not(lib func)
        self.inputc=False        #If we have to take input or not(lib func)
        self.returnc=False       #If we have to return or not(lib func)



filename = sys.argv[1]
f = open(filename, 'r')
data = f.read()
lines=data.split('\n')
splitins2 = []
for i in lines:
    f=i.split(",")
    splitins2.append(f)
splitins=[]
x=[]
for l in splitins2:
    x=[]
    for i in l:
        i=i.strip(" ")
        x.append(i)
    temp=instruction()
    temp.convert(x)
    splitins.append(temp)
for i in splitins:
    i.printobj()
#print(splitins)
# for l in splitins:
#     print(l)
#     if(l[1]=='='):
#         print(l[2]+" "+ l[1]+" "+l[3])
#     elif(l[1]=='+' or l[1]== '-' or l[1]=='*' or l[1]=='/' or l[1]=='%'):
#         print(l[2]+ " = "+ l[3]+ l[1] + l[4])
#
# # print(splitins)
# # print(data)
# #w=input().split(",");
# # print(w)
