#!/usr/bin/python
    
import sys
class instruction(object):
    def convert(self, param):
        # print(param)
        if(len(param)==1):
            return 0
        self.lineno=param[0]
        self.op=param[1]
        if (param[1]=="ifgoto"):
            self.jmp=True
            self.cmpl=True
            self.cmpltype=param[2]
            self.src1=param[3]
            self.src2=param[4]
            self.jlno=param[5]
            basicblock.append(int(self.lineno))
            basicblock.append(int(self.jlno))
            # splitins[i].jlno
            marker.append(int(self.jlno))
        elif (param[1]=="call"):
            basicblock.append(int(self.lineno))
            basicblock.append(int(self.lineno)+1)
            self.func=True
            self.funcname=param[2]
        elif (param[1]=="ret"):
            self.returnc=True
        elif (param[1]=="label"):
            basicblock.append(int(self.lineno))
            # marker.append(int(self.lineno))
            self.lbl=True
            self.lblname="u_"+param[2]
        elif (param[1]=="print"):
            self.printc=True
            self.src1=varname(param[2])
        elif (param[1]=="="):
            self.dst=varname(param[2])
            self.src1=varname(param[3])
            variables.append(varname(param[2]))
            variables.append(varname(param[3]))
        else:
            self.dst=varname(param[2])
            self.src1=varname(param[3])
            self.src2=varname(param[4])
            variables.append(varname(param[2]))
            variables.append(varname(param[3]))
            variables.append(varname(param[4]))

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
#
def varname(var):
    if(var.isdigit()):
        return var
    else:
        return "v_"+var
def build_nextusetable():
    #print(type(basicblock[0]))
    # for i in range(1,len(basicblock)):
    #     for j in range(basicblock[i],basicblock[i-1],-1):
    #         print(str(j))
            # continue
    for i in range(1,len(basicblock)):
        newdiction  = {}
        newdiction['1line'] = -1
        for j in range(basicblock[i],basicblock[i-1],-1):
            # print("line no = " + str(j))
            newdiction['1line'] = j
            nextuse.insert(basicblock[i-1],newdiction.copy())
            if(splitins[j-1].dst!=None):
                if(splitins[j-1].dst in newdiction.keys()):
                    del newdiction[splitins[j-1].dst]
            if(splitins[j-1].src1!= None):
                if(isInt(splitins[j-1].src1)==False):
                    newdiction[splitins[j-1].src1]=j
            if(splitins[j-1].src2!= None):
                if(isInt(splitins[j-1].src2)==False):
                    newdiction[splitins[j-1].src2]=j

    #             print(splitins[j-1].src1)

def isregassigned(var):
    if(isInt(var)):
        print("Error Spotted:---" +str(var))
    for i in range(0,6):
        if(regalloc[i]==var):
            return i
    return "-1"

def regname(regno):
    #ebx=1 ,ecx=2, esi=3, edi=4, eax=5, edx=6
    if(regno==0):
        return '%ebx'
    if(regno==1):
        return '%ecx'
    if(regno==2):
        return "%esi"
    if(regno==3):
        return '%edi'
    if(regno==4):
        return '%eax'
    if(regno==5):
        return '%edx'

def emptyreg(lineno,regno):
    if(regalloc[regno]=='-1'):
        regalloc[regno]=='0DNA'
        return True
    for i in regalloc:
        if regalloc[isregassigned(i)]!='0DNA' and i not in nextuse[lineno-1].keys():
            if(i!='-1'):
                print( "empline no: "+str(lineno)+ " movl  "+str(regname(isregassigned(i))+","+str(i)))
                print("empline no: "+str(lineno)+" movl "+regname(regno)+","+str(regname(isregassigned(i))))
                regalloc[isregassigned(i)]=regalloc[regno]
                regalloc[regno]='0DNA'
            else:
                print("empline no: "+str(lineno)+" movl "+regname(regno)+","+str(regname(isregassigned(i))))
                regalloc[isregassigned(i)]=regalloc[regno]
                regalloc[regno]='0DNA'
            # print( "line no: "+str(lineno)+ " movl  "+str(regname(isregassigned(i))+","+str(i)))
            # regtoassign=isregassigned(i)
            # regalloc[regtoassign]='0DNA'
            return True
    tempvar=None
    tempnextuse=-1
    for j in range(0,6) and regalloc[j]!='0DNA':
        i=regalloc[j]
        if(tempnextuse==-1):
            tempvar=i
            tempnextuse=nextuse[lineno-1][i]
        elif(tempnextuse<nextuse[lineno-1][i]):
                tempvar=i
                tempnextuse=nextuse[lineno-1][i]
    print("empline no: "+str(lineno)+ "  movl "+str(regname(isregassigned(tempvar))+","+str(tempvar)))
    print("empline no: "+str(lineno)+" movl "+regname(regno)+","+str(regname(isregassigned(tempvar))))
    regalloc[isregassigned(tempvar)]=regalloc[regno]
    regalloc[regno]='0DNA'
    return True



def getreg(lineno,var):
    # mode = 0
    # if(splitins[lineno].op=="/" or splitins[lineno].op=="%"):


    ####NOT FOR DIV
    for i in range(6):
        if(regalloc[i]=='-1'):
            # allocatedreg=i
            regalloc[i]=var
            return i
    for i in regalloc:
        if i not in nextuse[lineno-1].keys():
            print("movl "+str(regname(isregassigned(i))+" , "+str(i)))
            regtoassign=isregassigned(i)
            regalloc[regtoassign]=var
            return regtoassign
    tempvar=regalloc[0]
    tempnextuse=nextuse[lineno-1][tempvar]
    for j in range(1,6):
        i=regalloc[j]
        if(tempnextuse<nextuse[lineno-1][i]):
            tempvar=i
            tempnextuse=nextuse[lineno-1][i]
    # print("reg ass " + str(isregassigned(tempvar))+ " at" + regname(isregassigned(tempvar)))
    print("movl "+str(regname(isregassigned(tempvar))+" , "+str(tempvar)))
    regtoassign=isregassigned(i)
    regalloc[regtoassign]=var
    return regtoassign
# Amit Comments??
def regs(i,var):
    tmp=isregassigned(var)
    if(tmp!="-1"):
        a=regname(tmp)
    else:
        a=regname(getreg(i+1,var))
    return a

# Returns whether x is integer or not
def isInt(x):
    x=str(x).strip(' ')
    if(x[0]=='-'):
        x=x[1:]
        return x.isdigit()
    else:
        return x.isdigit()

# Self documenting piece of Code 
InstrSet=["movl ","addl ", "subl ","imull ","idivl ","xchg "]

def out(mode, str1,str2):
    if(isInt(str1)):
        str1="$"+str(str1)
    else:
        str1=str(str1)
    if(isInt(str2)):
        str2="$"+str(str2)
    else:
        str2=str(str2)
    str1=str1.strip(' ')
    str2=str2.strip(' ')
    if(mode=='M'):
        Output=InstrSet[0]+str1+" , "+str2
    elif(mode=='A'):
        Output=InstrSet[1]+str1+" , "+str2
    elif(mode=='S'):
        Output=InstrSet[2]+str1+" , "+str2
    elif(mode=='I'):
        Output=InstrSet[3]+str1+" , "+str2
    elif(mode=='D'):
        Output=InstrSet[4]+str1+" , "+str2
    elif(mode=='X'):
        Output=InstrSet[5]+str1+" , "+str2
    else:
        raise ValueError("INVALID MODE:- Don't You know I m Idiot?")
    print(Output)


def createdatasection():
    print(".section .data")
    for i in variables :
        if (i.isdigit()):
            continue
        print(str(i)+":")
        print("\t.long 0")
    print(".section .data")
    print(" ")
    print(".section .text")
    print(" ")
    print(".global _start")
    print("\n")
def convertassem():
    # print splitins
    for i in range(len(splitins)):
        # print(splitins[i].lineno)
        if(splitins[i].op == '='):
            if(isInt(splitins[i].src1)):
                a=regs(i,splitins[i].dst)
                out("M",splitins[i].src1,a)
                # print("movl $"+ splitins[i].src1 + " , " + str(a))
            else:
                a=regs(i,splitins[i].dst)
                b=regs(i,splitins[i].src1)
                # print("movl "+ str(b) + " , " + str(a))
                out("M",b,a)
        elif(splitins[i].op=='+'):
            if(isInt(splitins[i].src1) or isInt(splitins[i].src2)):
                if(isInt(splitins[i].src1) and isInt(splitins[i].src2)):
                    a=regs(i,splitins[i].dst)
                    out("M",splitins[i].src1,a)
                    out("A",splitins[i].src2,a)
                elif(isInt(splitins[i].src1)):
                    b=regs(i,splitins[i].src2)
                    a=regs(i,splitins[i].dst)
                    out("M",b,a)
                    out("A",splitins[i].src1,a)
                else:
                    b=regs(i,splitins[i].src1)
                    a=regs(i,splitins[i].dst)
                    out("M",b,a)
                    out("A",splitins[i].src2,a)
            else:
                if(splitins[i].dst !=splitins[i].src1 and splitins[i].dst !=splitins[i].src2):
                    b=regs(i,splitins[i].src1)
                    c=regs(i,splitins[i].src2)
                    a=regs(i,splitins[i].dst)
                    out("M",c,a)
                    out("A",b,a)
                elif(splitins[i].dst ==splitins[i].src1 and splitins[i].dst !=splitins[i].src2):
                    c=regs(i,splitins[i].src2)
                    a=regs(i,splitins[i].dst)
                    out("A",c,a)
                elif(splitins[i].dst !=splitins[i].src1 and splitins[i].dst ==splitins[i].src2):
                    b=regs(i,splitins[i].src1)
                    a=regs(i,splitins[i].dst)
                    out("A",b,a)
                elif(splitins[i].dst ==splitins[i].src1 and splitins[i].dst ==splitins[i].src2):
                    a=regs(i,splitins[i].dst)
                    out("A",a,a)

        elif(splitins[i].op=='-'):
            if(isInt(splitins[i].src1) or isInt(splitins[i].src2)):
                if(isInt(splitins[i].src1) and isInt(splitins[i].src2)):
                    a=regs(i,splitins[i].dst)
                    out("M",splitins[i].src1,a)
                    out("S",splitins[i].src2,a)
                elif(isInt(splitins[i].src1)):
                    b=regs(i,splitins[i].src2)
                    a=regs(i,splitins[i].dst)
                    out("M",0,a)
                    out("S",b,a)
                    out("A",splitins[i].src1,a)
                else:
                    b=regs(i,splitins[i].src1)
                    a=regs(i,splitins[i].dst)
                    out("M",b,a)
                    out("S",splitins[i].src2,a)
            else:
                if(splitins[i].dst !=splitins[i].src1 and splitins[i].dst !=splitins[i].src2):
                    b=regs(i,splitins[i].src1)
                    c=regs(i,splitins[i].src2)
                    a=regs(i,splitins[i].dst)
                    out("M",b,a)
                    out("S",c,a)
                elif(splitins[i].dst ==splitins[i].src1 and splitins[i].dst !=splitins[i].src2):
                    c=regs(i,splitins[i].src2)
                    a=regs(i,splitins[i].dst)
                    out("S",c,a)
                elif(splitins[i].dst !=splitins[i].src1 and splitins[i].dst ==splitins[i].src2):
                    b=regs(i,splitins[i].src1)
                    a=regs(i,splitins[i].dst)
                    out("S",a,b)
                    out("A",b,a)
                    out("X",a,b)
                elif(splitins[i].dst ==splitins[i].src1 and splitins[i].dst ==splitins[i].src2):
                    a=regs(i,splitins[i].dst)
                    out("S",a,a)
        elif(splitins[i].op=='*'):
            if(isInt(splitins[i].src1) or isInt(splitins[i].src2)):
                if(isInt(splitins[i].src1) and isInt(splitins[i].src2)):
                    a=regs(i,splitins[i].dst)
                    out("M",splitins[i].src1,a)
                    out("I",splitins[i].src2,a)
                elif(isInt(splitins[i].src1)):
                    b=regs(i,splitins[i].src2)
                    a=regs(i,splitins[i].dst)
                    out("M",b,a)
                    out("I",splitins[i].src1,a)
                else:
                    b=regs(i,splitins[i].src1)
                    a=regs(i,splitins[i].dst)
                    out("M",b,a)
                    out("I",splitins[i].src2,a)
            else:
                if(splitins[i].dst !=splitins[i].src1 and splitins[i].dst !=splitins[i].src2):
                    b=regs(i,splitins[i].src1)
                    c=regs(i,splitins[i].src2)
                    a=regs(i,splitins[i].dst)
                    out("M",c,a)
                    out("I",b,a)
                elif(splitins[i].dst ==splitins[i].src1 and splitins[i].dst !=splitins[i].src2):
                    c=regs(i,splitins[i].src2)
                    a=regs(i,splitins[i].dst)
                    out("I",c,a)
                elif(splitins[i].dst !=splitins[i].src1 and splitins[i].dst ==splitins[i].src2):
                    b=regs(i,splitins[i].src1)
                    a=regs(i,splitins[i].dst)
                    out("I",b,a)
                elif(splitins[i].dst ==splitins[i].src1 and splitins[i].dst ==splitins[i].src2):
                    a=regs(i,splitins[i].dst)
                    out("I",a,a)


variables = []
basicblock=[]
nextuse = []
basicblock.append(0)
marker=[]
regalloc = ['-1']*6
#No Scheme for regalloc
#ebx=1 ,ecx=2, esi=3, edi=4, eax=5, edx=6
i=0
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
# print(splitins2)
for l in splitins2:
    x=[]
    for i in l:
        i=i.strip(" ")
        x.append(i)
    temp=instruction()
    temp.convert(x)
    if(len(x)!=1):
        splitins.append(temp)
basicblock.append(len(splitins))
for i in splitins:
    i.printobj()
unique = set(variables)
variables = list(unique)
basicblock.sort()
print(basicblock)
print(marker)
build_nextusetable()
print("*********************************************************************************")
for i in nextuse:
    print(i)
print("*********************************************************************************")
# for i in range(len(nextuse)):
#     for j in nextuse[i-1].keys():
#         if(j=='1line'):
#             continue
#         if(isregassigned(j)!="-1"):
#             continue
#         if(isregassigned(j)=="-1"):
#             temp=getreg(i,j)
#         print("line no: "+str(i)+"  "+j+"  ::  "+str(temp))
#         # print()

# emptyreg(13,4)
# emptyreg(13,5)
createdatasection()
convertassem()

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
