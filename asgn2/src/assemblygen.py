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
            if(isInt(g.splitins[i].src1)):
                a=regs(i,g.splitins[i].dst)
                out("M",g.splitins[i].src1,a)
                # print("movl $"+ g.splitins[i].src1 + " , " + str(a))
            else:
                a=regs(i,g.splitins[i].dst)
                b=regs(i,g.splitins[i].src1)
                # print("movl "+ str(b) + " , " + str(a))
                out("M",b,a)
        elif(g.splitins[i].op=='+'):
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

        elif(g.splitins[i].op=='-'):
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
        elif(g.splitins[i].op=='*'):
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

