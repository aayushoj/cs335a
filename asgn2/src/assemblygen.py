#
#TODO: RETURN 
#
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
        Output=Instr+str1
    elif(mode=='X'):
        Instr="xchg "
        Output=Instr+str1+" , "+str2
    elif(mode=='CD'):
        Instr='cdq '
        Output=Instr
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
    if(g.regalloc[4]!="-1"):
        out('M',"%eax",getVar("%eax"))
    if(g.regalloc[0]!="-1"):
        out('M',"%ebx",getVar("%ebx"))
    if(g.regalloc[1]!="-1"):
        out('M',"%ecx",getVar("%ecx"))
    if(g.regalloc[5]!="-1"):
        out('M',"%edx",getVar("%edx"))
    if(g.regalloc[2]!="-1"):
        out('M',"%esi",getVar("%esi"))
    if(g.regalloc[3]!="-1"):
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
    i=line
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

def DIVIDE(line):
    i=line
    if(isInt(g.splitins[i].src1) or isInt(g.splitins[i].src2)):
        if(isInt(g.splitins[i].src1) and isInt(g.splitins[i].src2)):
            a=regs(i,g.splitins[i].dst)
            if(g.regalloc[4]=='-1'):
                out("M",a,"%eax")
                g.regalloc[isregassigned(g.splitins[i].dst)]=-1
                g.regalloc[4]=g.splitins[i].dst
            else:
                if(a!='%eax'):
                    tmp=regalloc[4]
                    tmp2 = isregassigned(g.splitins[i].dst)
                    out("X",a,"%eax")
                    g.regalloc[tmp2]=tmp
                    g.regalloc[4]=g.splitins[i].dst
            out("M",g.splitins[i].src1,a)
            emptyreg(i,5)
            out("M",0,"%edx")
            tmp = regs(i,"$"+str(g.splitins[i].src2))
            out("M",g.splitins[i].src2,tmp)
            out("CD")
            out("D",tmp)
            g.regalloc[isregassigned("$"+str(g.splitins[i].src2))]='-1'
            g.regalloc[5]='-1'
        elif(isInt(g.splitins[i].src1)):
            a=regs(i,g.splitins[i].dst)
            if(g.regalloc[4]=='-1'):
                out("M",a,"%eax")
                g.regalloc[isregassigned(g.splitins[i].dst)]=-1
                g.regalloc[4]=g.splitins[i].dst
            else:
                if(a!='%eax'):
                    tmp=regalloc[4]
                    tmp2 = isregassigned(g.splitins[i].dst)
                    out("X",a,"%eax")
                    g.regalloc[tmp2]=tmp
                    g.regalloc[4]=g.splitins[i].dst
            out("M",g.splitins[i].src1,a)
            emptyreg(i,5)
            out("M",0,"%edx")
            b=regs(i,g.splitins[i].src2)
            out("CD")
            out("D",b)
            g.regalloc[5]='-1'
        else:
            a=regs(i,g.splitins[i].dst)
            if(g.regalloc[4]=='-1'):
                out("M",a,"%eax")
                g.regalloc[isregassigned(g.splitins[i].dst)]=-1
                g.regalloc[4]=g.splitins[i].dst
            else:
                if(a!='%eax'):
                    tmp=regalloc[4]
                    tmp2 = isregassigned(g.splitins[i].dst)
                    out("X",a,"%eax")
                    g.regalloc[tmp2]=tmp
                    g.regalloc[4]=g.splitins[i].dst
            emptyreg(i,5)
            out("M",0,"%edx")
            b=regs(i,g.splitins[i].src1)
            print(str(g.splitins[i].src2))
            print(str(g.splitins[i].src1))
            tmp = regs(i,"$"+str(g.splitins[i].src2))
            out("M",b,a)
            out("M",g.splitins[i].src2,tmp)
            out("CD")
            out("D",tmp)
            g.regalloc[isregassigned("$"+str(g.splitins[i].src2))]='-1'
            g.regalloc[5]='-1'
    else:
        if(g.splitins[i].dst !=g.splitins[i].src1 and g.splitins[i].dst !=g.splitins[i].src2):
            a=regs(i,g.splitins[i].dst)
            if(g.regalloc[4]=='-1'):
                out("M",a,"%eax")
                g.regalloc[isregassigned(g.splitins[i].dst)]=-1
                g.regalloc[4]=g.splitins[i].dst
            else:
                if(a!='%eax'):
                    tmp=regalloc[4]
                    tmp2 = isregassigned(g.splitins[i].dst)
                    out("X",a,"%eax")
                    g.regalloc[tmp2]=tmp
                    g.regalloc[4]=g.splitins[i].dst
            emptyreg(i,5)
            out("M",0,"%edx")
            b=regs(i,g.splitins[i].src1)
            c=regs(i,g.splitins[i].src2)
            out("M",b,a)
            out("CD")
            out("D",c)
        elif(g.splitins[i].dst ==g.splitins[i].src1 and g.splitins[i].dst !=g.splitins[i].src2):
            a=regs(i,g.splitins[i].dst)
            if(g.regalloc[4]=='-1'):
                out("M",a,"%eax")
                g.regalloc[isregassigned(g.splitins[i].dst)]=-1
                g.regalloc[4]=g.splitins[i].dst
            else:
                if(a!='%eax'):
                    tmp=regalloc[4]
                    tmp2 = isregassigned(g.splitins[i].dst)
                    out("X",a,"%eax")
                    g.regalloc[tmp2]=tmp
                    g.regalloc[4]=g.splitins[i].dst
            emptyreg(i,5)
            out("M",0,"%edx")
            c=regs(i,g.splitins[i].src2)
            out("CD")
            out("D",c)
        elif(g.splitins[i].dst !=g.splitins[i].src1 and g.splitins[i].dst ==g.splitins[i].src2):
            a=regs(i,g.splitins[i].dst)
            if(g.regalloc[4]=='-1'):
                out("M",a,"%eax")
                g.regalloc[isregassigned(g.splitins[i].dst)]=-1
                g.regalloc[4]=g.splitins[i].dst
            else:
                if(a!='%eax'):
                    tmp=regalloc[4]
                    tmp2 = isregassigned(g.splitins[i].dst)
                    out("X",a,"%eax")
                    g.regalloc[tmp2]=tmp
                    g.regalloc[4]=g.splitins[i].dst
            emptyreg(i,5)
            out("M",0,"%edx")
            b=regs(i,g.splitins[i].src1)
            c=regs(i,'xcpp')
            out("M",a,c)
            out("M",b,a)
            out("CD")
            out("D",c)
            g.regalloc[isregassigned('xcpp')]='-1'
        elif(g.splitins[i].dst ==g.splitins[i].src1 and g.splitins[i].dst ==g.splitins[i].src2):
            a=regs(i,g.splitins[i].dst)
            if(g.regalloc[4]=='-1'):
                out("M",a,"%eax")
                g.regalloc[isregassigned(g.splitins[i].dst)]=-1
                g.regalloc[4]=g.splitins[i].dst
            else:
                if(a!='%eax'):
                    tmp=regalloc[4]
                    tmp2 = isregassigned(g.splitins[i].dst)
                    out("X",a,"%eax")
                    g.regalloc[tmp2]=tmp
                    g.regalloc[4]=g.splitins[i].dst
            emptyreg(i,5)
            out("M",0,"%edx")
            out("CD")
            out("D",a)

def SUB(line):
    i=line
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
    inst=g.splitins[i]
    #read a if needed
    if(isInt(inst.src1)):
        a="$"+str(inst.src1)
    else:
        a=regs(i,inst.src1)
    print(a)
    #read b if needed
    if(isInt(inst.src2)):
        b="$"+str(inst.src2)
    else:
        b=regs(i,inst.src2)
    print(b)
    SaveContext()
    out('C',a,b)
    if(isInt(inst.jlno)):
        label="l_"+str(inst.jlno)
    else:
        label="u_"+str(inst.jlno)
    #cmpltype #remove it
    if(inst.cmpltype=='eq'):
        out("JE",label)
    elif(inst.cmpltype=='leq'):
        out("JLE",label)
    elif(inst.cmpltype=='geq'):
        out("JGE",label)
    elif(inst.cmpltype=='g'):
        out("JG",label)
    elif(inst.cmpltype=='l'):
        out("JL",label)
    else:
        raise ValueError("INVALID LABEL:-  IFGOTO() in file assemblygen.py")

def convertassem():
    # print g.splitins
    for k in g.marker:
        g.splitins[k-1].lbl=True
        g.splitins[k-1].lblname="l_"+str(k)
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
        elif(g.splitins[i].op=='/'):
            DIVIDE(i)
        elif(g.splitins[i].op=='ifgoto'):
            IFGOTO(i)
        else:
            raise ValueError("INVALID MODE:- Don't You know I m Idiot?")
