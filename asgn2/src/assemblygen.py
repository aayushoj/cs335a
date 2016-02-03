import globalvars as g
from regallocfn import *

# Returns whether x is integer or not
def isInt(x):
    x=str(x).strip(' ')
    if(x[0]=='-'):
        x=x[1:]
        return x.isdigit()
    else:
        return x.isdigit()

# Self documenting piece of Code
# InstrSet=["movl ","addl ", "subl ","imull ","idivl ","xchg ","jmp ","je ","jge ","jg ","jl ","jle ","cmpl "]

def out(mode='Q',str1="Default",str2="Default"):
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
        Instr="movl "
        Output=Instr+str1+" , "+str2
    elif(mode=='A'):
        Instr="addl "
        Output=Instr+str1+" , "+str2
    elif(mode=='S'):
        Instr="movl "
        Output=Instr+str1+" , "+str2
    elif(mode=='I'):
        Instr="imull "
        Output=Instr+str1+" , "+str2
    elif(mode=='D'):
        Instr="idivl "
        Output=Instr+str1+" , "+str2
    elif(mode=='X'):
        Instr="xchg "
        Output=Instr+str1+" , "+str2
    elif(mode=='C'): #Case of cmpl
        Instr="cmpl "
        Output=Instr+str1+" , "+str2
    elif(mode[0]=='J'):
        spec=mode[1:]
        if(spec=="MP"): # Case of jmp
            Instr="jmp "
            Output=Instr+str1
        elif(spec=="E"): #Case of je
            Instr="je "
            Output=Instr+str1
        elif(spec=="GE"): #Case of jge
            Instr="jge "
            Output=Instr+str1
        elif(spec=="G"): #Case of jg
            Instr="jg "
            Output=Instr+str1
        elif(spec=="L"): #Case of jl
            Instr="jl "
            Output=Instr+str1
        elif(spec=="LE"): #Case of jle
            Instr="jle "
            Output=Instr+str1
    else:
        raise ValueError("INVALID MODE:- Don't You know I m Idiot?")
    print(Output)

def SaveContext():
    out('M',"%eax",getVar("%eax"))
    out('M',"%ebx",getVar("%ebx"))
    out('M',"%ecx",getVar("%ecx"))
    out('M',"%edx",getVar("%edx"))
    out('M',"%esi",getVar("%esi"))
    out('M',"%edi",getVar("%edi"))


def createdatasection():
    print(".section .data")
    for i in g.variables :
        if (isInt(i)):
            continue
        print(str(i)+":")
        print("\t.long 0")
    print("returnval:")
    print("\t.long 0")
    print("returnaddr:")
    print("\t.long 0")
    print(".section .data")
    print(" ")
    print(".section .text")
    print(" ")
    print(".global _start")
    print("\n\n _start:")
    print("\n")



def ADD(line):
    i=line
    if(isInt(g.splitins[i].src1) or isInt(g.splitins[i].src2)):
        if(isInt(g.splitins[i].src1) and isInt(g.splitins[i].src2)):
            a=regs(i,g.splitins[i].dst)
            out("M",g.splitins[i].src1,a)
            out("A",g.splitins[i].src2,a)
        elif(isInt(g.splitins[i].src1)):
            b=regs(i,g.splitins[i].src2)
            a=regs(i,g.splitins[i].dst)
            out("M",b,a)
            out("A",g.splitins[i].src1,a)
        else:
            b=regs(i,g.splitins[i].src1)
            a=regs(i,g.splitins[i].dst)
            out("M",b,a)
            out("A",g.splitins[i].src2,a)
    else:
        if(g.splitins[i].dst !=g.splitins[i].src1 and g.splitins[i].dst !=g.splitins[i].src2):
            b=regs(i,g.splitins[i].src1)
            c=regs(i,g.splitins[i].src2)
            a=regs(i,g.splitins[i].dst)
            out("M",c,a)
            out("A",b,a)
        elif(g.splitins[i].dst ==g.splitins[i].src1 and g.splitins[i].dst !=g.splitins[i].src2):
            c=regs(i,g.splitins[i].src2)
            a=regs(i,g.splitins[i].dst)
            out("A",c,a)
        elif(g.splitins[i].dst !=g.splitins[i].src1 and g.splitins[i].dst ==g.splitins[i].src2):
            b=regs(i,g.splitins[i].src1)
            a=regs(i,g.splitins[i].dst)
            out("A",b,a)
        elif(g.splitins[i].dst ==g.splitins[i].src1 and g.splitins[i].dst ==g.splitins[i].src2):
            a=regs(i,g.splitins[i].dst)
            out("A",a,a)

def MULL(line):
    if(isInt(g.splitins[i].src1) or isInt(g.splitins[i].src2)):
        if(isInt(g.splitins[i].src1) and isInt(g.splitins[i].src2)):
            a=regs(i,g.splitins[i].dst)
            out("M",g.splitins[i].src1,a)
            out("I",g.splitins[i].src2,a)
        elif(isInt(g.splitins[i].src1)):
            b=regs(i,g.splitins[i].src2)
            a=regs(i,g.splitins[i].dst)
            out("M",b,a)
            out("I",g.splitins[i].src1,a)
        else:
            b=regs(i,g.splitins[i].src1)
            a=regs(i,g.splitins[i].dst)
            out("M",b,a)
            out("I",g.splitins[i].src2,a)
    else:
        if(g.splitins[i].dst !=g.splitins[i].src1 and g.splitins[i].dst !=g.splitins[i].src2):
            b=regs(i,g.splitins[i].src1)
            c=regs(i,g.splitins[i].src2)
            a=regs(i,g.splitins[i].dst)
            out("M",c,a)
            out("I",b,a)
        elif(g.splitins[i].dst ==g.splitins[i].src1 and g.splitins[i].dst !=g.splitins[i].src2):
            c=regs(i,g.splitins[i].src2)
            a=regs(i,g.splitins[i].dst)
            out("I",c,a)
        elif(g.splitins[i].dst !=g.splitins[i].src1 and g.splitins[i].dst ==g.splitins[i].src2):
            b=regs(i,g.splitins[i].src1)
            a=regs(i,g.splitins[i].dst)
            out("I",b,a)
        elif(g.splitins[i].dst ==g.splitins[i].src1 and g.splitins[i].dst ==g.splitins[i].src2):
            a=regs(i,g.splitins[i].dst)
            out("I",a,a)

#def DIV(line):

def SUB(line):
    if(isInt(g.splitins[i].src1) or isInt(g.splitins[i].src2)):
        if(isInt(g.splitins[i].src1) and isInt(g.splitins[i].src2)):
            a=regs(i,g.splitins[i].dst)
            out("M",g.splitins[i].src1,a)
            out("S",g.splitins[i].src2,a)
        elif(isInt(g.splitins[i].src1)):
            b=regs(i,g.splitins[i].src2)
            a=regs(i,g.splitins[i].dst)
            out("M",0,a)
            out("S",b,a)
            out("A",g.splitins[i].src1,a)
        else:
            b=regs(i,g.splitins[i].src1)
            a=regs(i,g.splitins[i].dst)
            out("M",b,a)
            out("S",g.splitins[i].src2,a)
    else:
        if(g.splitins[i].dst !=g.splitins[i].src1 and g.splitins[i].dst !=g.splitins[i].src2):
            b=regs(i,g.splitins[i].src1)
            c=regs(i,g.splitins[i].src2)
            a=regs(i,g.splitins[i].dst)
            out("M",b,a)
            out("S",c,a)
        elif(g.splitins[i].dst ==g.splitins[i].src1 and g.splitins[i].dst !=g.splitins[i].src2):
            c=regs(i,g.splitins[i].src2)
            a=regs(i,g.splitins[i].dst)
            out("S",c,a)
        elif(g.splitins[i].dst !=g.splitins[i].src1 and g.splitins[i].dst ==g.splitins[i].src2):
            b=regs(i,g.splitins[i].src1)
            a=regs(i,g.splitins[i].dst)
            out("S",a,b)
            out("A",b,a)
            out("X",a,b)
        elif(g.splitins[i].dst ==g.splitins[i].src1 and g.splitins[i].dst ==g.splitins[i].src2):
            a=regs(i,g.splitins[i].dst)
            out("S",a,a)

def EQUAL(line):
    i=line
    if(isInt(g.splitins[i].src1)):
        a=regs(i,g.splitins[i].dst)
        out("M",g.splitins[i].src1,a)
        # print("movl $"+ g.splitins[i].src1 + " , " + str(a))
    else:
        a=regs(i,g.splitins[i].dst)
        b=regs(i,g.splitins[i].src1)
        # print("movl "+ str(b) + " , " + str(a))
        out("M",b,a)

def IFGOTO(line):
    i=line
def convertassem():
    # print g.splitins
    for k in g.marker:
        g.splitins[k-1].lbl=True
        g.splitins[k-1].lblname="L_"+str(k)
    for i in range(len(g.splitins)):
        if(g.splitins[i].lbl==True):
            print("\n"+g.splitins[i].lblname+":")
        # print(g.splitins[i].lineno)
        if(g.splitins[i].op == '='):
            EQUAL(i)
        elif(g.splitins[i].op=='+'):
            ADD(i)
        elif(g.splitins[i].op=='-'):
            SUB(i)
        elif(g.splitins[i].op=='*'):
            MULL(i)
        elif(g.splitins[i].param[1]=='ifgoto'):
            IFGOTO(i)
        else:
            raise ValueError("INVALID MODE:- Don't You know I m Idiot?")
