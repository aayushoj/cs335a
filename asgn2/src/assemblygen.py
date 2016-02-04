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
        Instr="subl "
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
    elif(mode[0]=='P'):
        spec=mode[1]
        if(spec=="U"):
            Instr="pushl "
            Output=Instr+str1
        elif(spec=="O"):
            Instr="popl "
            Output=Instr+str1
    elif(mode[:2]=="CA"):
        Instr="call "
        Output=Instr+str1
    elif(mode[0]=="R"):
        Output="ret"
    elif(mode=="int"):
        Instr="int "
        Output=Instr+str1
    else:
        raise ValueError("INVALID MODE:- Don't You know I m Idiot?")
    print('\t'+Output)

def SaveContext():
    # print("SaveContext")
    if(getVar("%eax")!="NULL"):
        out('M',"%eax",getVar("%eax"))
    if(getVar("%ebx")!="NULL"):
        out('M',"%ebx",getVar("%ebx"))
    if(getVar("%ecx")!="NULL"):
        out('M',"%ecx",getVar("%ecx"))
    if(getVar("%edx")!="NULL"):
        out('M',"%edx",getVar("%edx"))
    if(getVar("%esi")!="NULL"):
        out('M',"%esi",getVar("%esi"))
    if(getVar("%edi")!="NULL"):
        out('M',"%edi",getVar("%edi"))
    for i in range(0,6):
        g.regalloc[i]='-1'


def createdatasection():
    print(".section .data")
    strIO="format_input:\n\t.ascii \"%d\\0\"\nformat_output:\n \t.ascii \"%d\\n\\0\"\nL_INPUT:\n\t.long 0"
    print(strIO)
    for i in g.variables :
        if (isInt(i)):
            continue
        print(str(i)+":")
        print("\t.long 0")
    # print("returnval:")
    # print("\t.long 0")
    # print("returnaddr:")
    # print("\t.long 0")
    print(".section .data")
    print(" ")
    print(".section .text")
    print(" ")
    print(".global _start")
    print_functions()
    print("\n _start:")



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
                g.regalloc[isregassigned(g.splitins[i].dst)]='-1'
                g.regalloc[4]=g.splitins[i].dst
            else:
                if(a!='%eax'):
                    tmp=g.regalloc[4]
                    tmp2 = isregassigned(g.splitins[i].dst)
                    out("X",a,"%eax")
                    g.regalloc[tmp2]=tmp
                    g.regalloc[4]=g.splitins[i].dst
            a='%eax'
            out("M",g.splitins[i].src1,a)
            emptyreg(i,5)
            out("M",0,"%edx")
            tmp = regs(i,"$"+str(g.splitins[i].src2))
            out("M",g.splitins[i].src2,tmp)
            out("CD")
            out("D",tmp)
            g.regalloc[isregassigned("$"+str(g.splitins[i].src2))]='-1'
            g.regalloc[5]='-1'
        elif(isInt(g.splitins[i].src1) and (g.splitins[i].src2!=g.splitins[i].dst)):
            a=regs(i,g.splitins[i].dst)
            if(g.regalloc[4]=='-1'):
                out("M",a,"%eax")
                g.regalloc[isregassigned(g.splitins[i].dst)]='-1'
                g.regalloc[4]=g.splitins[i].dst
            else:
                if(a!='%eax'):
                    tmp=g.regalloc[4]
                    tmp2 = isregassigned(g.splitins[i].dst)
                    out("X",a,"%eax")
                    g.regalloc[tmp2]=tmp
                    g.regalloc[4]=g.splitins[i].dst
            a='%eax'
            out("M",g.splitins[i].src1,a)
            emptyreg(i,5)
            out("M",0,"%edx")
            b=regs(i,g.splitins[i].src2)
            out("CD")
            out("D",b)
            g.regalloc[5]='-1'
        elif(isInt(g.splitins[i].src1) and (g.splitins[i].src2==g.splitins[i].dst)):
            a=regs(i,g.splitins[i].dst)
            if(g.regalloc[4]=='-1'):
                out("M",a,"%eax")
                g.regalloc[isregassigned(g.splitins[i].dst)]='-1'
                g.regalloc[4]=g.splitins[i].dst
            else:
                if(a!='%eax'):
                    tmp=g.regalloc[4]
                    tmp2 = isregassigned(g.splitins[i].dst)
                    out("X",a,"%eax")
                    g.regalloc[tmp2]=tmp
                    g.regalloc[4]=g.splitins[i].dst
            a='%eax'
            emptyreg(i,5)
            out("M",0,"%edx")
            c=regs(i,'xcpp')
            out("M",a,c)
            out("M",g.splitins[i].src1,a)
            out("CD")
            out("D",c)
            g.regalloc[isregassigned('xcpp')]='-1'
            g.regalloc[5]='-1'
        else:
            a=regs(i,g.splitins[i].dst)
            if(g.regalloc[4]=='-1'):
                out("M",a,"%eax")
                g.regalloc[isregassigned(g.splitins[i].dst)]='-1'
                g.regalloc[4]=g.splitins[i].dst
            else:
                if(a!='%eax'):
                    tmp=g.regalloc[4]
                    tmp2 = isregassigned(g.splitins[i].dst)
                    out("X",a,"%eax")
                    g.regalloc[tmp2]=tmp
                    g.regalloc[4]=g.splitins[i].dst
            a='%eax'
            emptyreg(i,5)
            out("M",0,"%edx")
            b=regs(i,g.splitins[i].src1)
            g.debug(str(g.splitins[i].src2))
            g.debug(str(g.splitins[i].src1))
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
                g.regalloc[isregassigned(g.splitins[i].dst)]='-1'
                g.regalloc[4]=g.splitins[i].dst
            else:
                if(a!='%eax'):
                    tmp=g.regalloc[4]
                    tmp2 = isregassigned(g.splitins[i].dst)
                    out("X",a,"%eax")
                    g.regalloc[tmp2]=tmp
                    g.regalloc[4]=g.splitins[i].dst
            a='%eax'
            emptyreg(i,5)
            out("M",0,"%edx")
            b=regs(i,g.splitins[i].src1)
            c=regs(i,g.splitins[i].src2)
            out("M",b,a)
            out("CD")
            out("D",c)
            g.regalloc[5]='-1'
        elif(g.splitins[i].dst ==g.splitins[i].src1 and g.splitins[i].dst !=g.splitins[i].src2):
            a=regs(i,g.splitins[i].dst)
            if(g.regalloc[4]=='-1'):
                out("M",a,"%eax")
                g.regalloc[isregassigned(g.splitins[i].dst)]='-1'
                g.regalloc[4]=g.splitins[i].dst
            else:
                if(a!='%eax'):
                    tmp=g.regalloc[4]
                    tmp2 = isregassigned(g.splitins[i].dst)
                    out("X",a,"%eax")
                    g.regalloc[tmp2]=tmp
                    g.regalloc[4]=g.splitins[i].dst
            a='%eax'
            emptyreg(i,5)
            out("M",0,"%edx")
            c=regs(i,g.splitins[i].src2)
            out("CD")
            out("D",c)
            g.regalloc[5]='-1'
        elif(g.splitins[i].dst !=g.splitins[i].src1 and g.splitins[i].dst ==g.splitins[i].src2):
            a=regs(i,g.splitins[i].dst)
            if(g.regalloc[4]=='-1'):
                out("M",a,"%eax")
                g.regalloc[isregassigned(g.splitins[i].dst)]='-1'
                g.regalloc[4]=g.splitins[i].dst
            else:
                if(a!='%eax'):
                    tmp=g.regalloc[4]
                    tmp2 = isregassigned(g.splitins[i].dst)
                    out("X",a,"%eax")
                    g.regalloc[tmp2]=tmp
                    g.regalloc[4]=g.splitins[i].dst
            a='%eax'
            emptyreg(i,5)
            out("M",0,"%edx")
            b=regs(i,g.splitins[i].src1)
            c=regs(i,'xcpp')
            out("M",a,c)
            out("M",b,a)
            out("CD")
            out("D",c)
            g.regalloc[isregassigned('xcpp')]='-1'
            g.regalloc[5]='-1'
        elif(g.splitins[i].dst ==g.splitins[i].src1 and g.splitins[i].dst ==g.splitins[i].src2):
            a=regs(i,g.splitins[i].dst)
            if(g.regalloc[4]=='-1'):
                out("M",a,"%eax")
                g.regalloc[isregassigned(g.splitins[i].dst)]='-1'
                g.regalloc[4]=g.splitins[i].dst
            else:
                if(a!='%eax'):
                    tmp=g.regalloc[4]
                    tmp2 = isregassigned(g.splitins[i].dst)
                    out("X",a,"%eax")
                    g.regalloc[tmp2]=tmp
                    g.regalloc[4]=g.splitins[i].dst
            a='%eax'
            emptyreg(i,5)
            out("M",0,"%edx")
            out("CD")
            out("D",a)
            g.regalloc[5]='-1'

def MOD(line):
    i=line
    if(isInt(g.splitins[i].src1) or isInt(g.splitins[i].src2)):
        if(isInt(g.splitins[i].src1) and isInt(g.splitins[i].src2)):
            a=regs(i,g.splitins[i].dst)
            if(g.regalloc[4]=='-1'):
                out("M",a,"%eax")
                g.regalloc[isregassigned(g.splitins[i].dst)]='-1'
                g.regalloc[4]=g.splitins[i].dst
            else:
                if(a!='%eax'):
                    tmp=g.regalloc[4]
                    tmp2 = isregassigned(g.splitins[i].dst)
                    out("X",a,"%eax")
                    g.regalloc[tmp2]=tmp
                    g.regalloc[4]=g.splitins[i].dst
            a='%eax'
            out("M",g.splitins[i].src1,a)
            emptyreg(i,5)
            out("M",0,"%edx")
            tmp = regs(i,"$"+str(g.splitins[i].src2))
            out("M",g.splitins[i].src2,tmp)
            out("CD")
            out("D",tmp)
            out("M","%edx",a)
            g.regalloc[isregassigned("$"+str(g.splitins[i].src2))]='-1'
            g.regalloc[5]='-1'
        elif(isInt(g.splitins[i].src1) and (g.splitins[i].src2!=g.splitins[i].dst)):
            a=regs(i,g.splitins[i].dst)
            if(g.regalloc[4]=='-1'):
                out("M",a,"%eax")
                g.regalloc[isregassigned(g.splitins[i].dst)]='-1'
                g.regalloc[4]=g.splitins[i].dst
            else:
                if(a!='%eax'):
                    tmp=g.regalloc[4]
                    tmp2 = isregassigned(g.splitins[i].dst)
                    out("X",a,"%eax")
                    g.regalloc[tmp2]=tmp
                    g.regalloc[4]=g.splitins[i].dst
            a='%eax'
            out("M",g.splitins[i].src1,a)
            emptyreg(i,5)
            out("M",0,"%edx")
            b=regs(i,g.splitins[i].src2)
            out("CD")
            out("D",b)
            out("M","%edx",a)
            g.regalloc[5]='-1'
        elif(isInt(g.splitins[i].src1) and (g.splitins[i].src2==g.splitins[i].dst)):
            a=regs(i,g.splitins[i].dst)
            if(g.regalloc[4]=='-1'):
                out("M",a,"%eax")
                g.regalloc[isregassigned(g.splitins[i].dst)]='-1'
                g.regalloc[4]=g.splitins[i].dst
            else:
                if(a!='%eax'):
                    tmp=g.regalloc[4]
                    tmp2 = isregassigned(g.splitins[i].dst)
                    out("X",a,"%eax")
                    g.regalloc[tmp2]=tmp
                    g.regalloc[4]=g.splitins[i].dst
            a='%eax'
            emptyreg(i,5)
            out("M",0,"%edx")
            c=regs(i,'xcpp')
            out("M",a,c)
            out("M",g.splitins[i].src1,a)
            out("CD")
            out("D",c)
            out("M","%edx",a)
            g.regalloc[isregassigned('xcpp')]='-1'
            g.regalloc[5]='-1'
        else:
            a=regs(i,g.splitins[i].dst)
            if(g.regalloc[4]=='-1'):
                out("M",a,"%eax")
                g.regalloc[isregassigned(g.splitins[i].dst)]='-1'
                g.regalloc[4]=g.splitins[i].dst
            else:
                if(a!='%eax'):
                    tmp=g.regalloc[4]
                    tmp2 = isregassigned(g.splitins[i].dst)
                    out("X",a,"%eax")
                    g.regalloc[tmp2]=tmp
                    g.regalloc[4]=g.splitins[i].dst
            a='%eax'
            emptyreg(i,5)
            out("M",0,"%edx")
            b=regs(i,g.splitins[i].src1)
            g.debug(str(g.splitins[i].src2))
            g.debug(str(g.splitins[i].src1))
            tmp = regs(i,"$"+str(g.splitins[i].src2))
            out("M",b,a)
            out("M",g.splitins[i].src2,tmp)
            out("CD")
            out("D",tmp)
            out("M","%edx",a)
            g.regalloc[isregassigned("$"+str(g.splitins[i].src2))]='-1'
            g.regalloc[5]='-1'
    else:
        if(g.splitins[i].dst !=g.splitins[i].src1 and g.splitins[i].dst !=g.splitins[i].src2):
            a=regs(i,g.splitins[i].dst)
            if(g.regalloc[4]=='-1'):
                out("M",a,"%eax")
                g.regalloc[isregassigned(g.splitins[i].dst)]='-1'
                g.regalloc[4]=g.splitins[i].dst
            else:
                if(a!='%eax'):
                    tmp=g.regalloc[4]
                    tmp2 = isregassigned(g.splitins[i].dst)
                    out("X",a,"%eax")
                    g.regalloc[tmp2]=tmp
                    g.regalloc[4]=g.splitins[i].dst
            a='%eax'
            emptyreg(i,5)
            a='%eax'
            # print("a..... =" + str(a))
            out("M",0,"%edx")
            b=regs(i,g.splitins[i].src1)
            c=regs(i,g.splitins[i].src2)
            out("M",b,a)
            out("CD")
            out("D",c)
            out("M","%edx",a)
            g.regalloc[5]='-1'
        elif(g.splitins[i].dst ==g.splitins[i].src1 and g.splitins[i].dst !=g.splitins[i].src2):
            a=regs(i,g.splitins[i].dst)
            if(g.regalloc[4]=='-1'):
                out("M",a,"%eax")
                g.regalloc[isregassigned(g.splitins[i].dst)]='-1'
                g.regalloc[4]=g.splitins[i].dst
            else:
                if(a!='%eax'):
                    tmp=g.regalloc[4]
                    tmp2 = isregassigned(g.splitins[i].dst)
                    out("X",a,"%eax")
                    g.regalloc[tmp2]=tmp
                    g.regalloc[4]=g.splitins[i].dst
            a='%eax'
            emptyreg(i,5)
            out("M",0,"%edx")
            c=regs(i,g.splitins[i].src2)
            out("CD")
            out("D",c)
            out("M","%edx",a)
            g.regalloc[5]='-1'
        elif(g.splitins[i].dst !=g.splitins[i].src1 and g.splitins[i].dst ==g.splitins[i].src2):
            a=regs(i,g.splitins[i].dst)
            if(g.regalloc[4]=='-1'):
                out("M",a,"%eax")
                g.regalloc[isregassigned(g.splitins[i].dst)]='-1'
                g.regalloc[4]=g.splitins[i].dst
            else:
                if(a!='%eax'):
                    tmp=g.regalloc[4]
                    tmp2 = isregassigned(g.splitins[i].dst)
                    out("X",a,"%eax")
                    g.regalloc[tmp2]=tmp
                    g.regalloc[4]=g.splitins[i].dst
            a='%eax'
            emptyreg(i,5)
            out("M",0,"%edx")
            b=regs(i,g.splitins[i].src1)
            c=regs(i,'xcpp')
            out("M",a,c)
            out("M",b,a)
            out("CD")
            out("D",c)
            out("M","%edx",a)
            g.regalloc[isregassigned('xcpp')]='-1'
            g.regalloc[5]='-1'
        elif(g.splitins[i].dst ==g.splitins[i].src1 and g.splitins[i].dst ==g.splitins[i].src2):
            a=regs(i,g.splitins[i].dst)
            if(g.regalloc[4]=='-1'):
                out("M",a,"%eax")
                g.regalloc[isregassigned(g.splitins[i].dst)]='-1'
                g.regalloc[4]=g.splitins[i].dst
            else:
                if(a!='%eax'):
                    tmp=g.regalloc[4]
                    tmp2 = isregassigned(g.splitins[i].dst)
                    out("X",a,"%eax")
                    g.regalloc[tmp2]=tmp
                    g.regalloc[4]=g.splitins[i].dst
            a='%eax'
            emptyreg(i,5)
            out("M",0,"%edx")
            out("CD")
            out("D",a)
            out("M","%edx",a)
            g.regalloc[5]='-1'

def SUB(line):
    i=line
    if(isInt(g.splitins[i].src1) or isInt(g.splitins[i].src2)):
        if(isInt(g.splitins[i].src1) and isInt(g.splitins[i].src2)):
            a=regs(i,g.splitins[i].dst)
            out("M",g.splitins[i].src1,a)
            out("S",g.splitins[i].src2,a)
        elif(isInt(g.splitins[i].src1)):
            if(g.splitins[i].dst!=g.splitins[i].src1):
                b=regs(i,g.splitins[i].src2)
                a=regs(i,g.splitins[i].dst)
                out("M",0,a)
                out("S",b,a)
                out("A",g.splitins[i].src1,a)
            else:
                a=regs(i,g.splitins[i].dst)
                tmp=regs(i,"xxpp")
                out("M",a,tmp)
                out("M",g.splitins[i].src1,a)
                out("S",tmp,a)
                g.regalloc[isregassigned('xxpp')]='-1'
        else:
            g.debug("something is fishyd")
            if(g.splitins[i].dst!=g.splitins[i].src1):
                b=regs(i,g.splitins[i].src1)
                a=regs(i,g.splitins[i].dst)
                out("M",b,a)
                out("S",g.splitins[i].src2,a)
            else:
                a=regs(i,g.splitins[i].dst)
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


def revert(inst):
    inst.src1,inst.src2=inst.src2,inst.src1
    if(inst.cmpltype=='eq'):
        inst.cmpltype='eq'
    elif(inst.cmpltype=='leq'):
        inst.cmpltype='g'
    elif(inst.cmpltype=='geq'):
        inst.cmpltype='l'
    elif(inst.cmpltype=='g'):
        inst.cmpltype='leq'
    elif(inst.cmpltype=='l'):
        inst.cmpltype='geq'
    else:
        raise ValueError("INVALID COMPARISON TYPE:- Don't You know Maths?")
    return inst



def IFGOTO(line):
    for i in range(0,6):
        g.debug(i)
        if(g.regalloc[i]!='-1'):
            g.debug("i dont know why?")


    i=line
    inst=g.splitins[i]
    SaveContext()
    if(not isInt(inst.src1) and isInt(inst.src2)):
        inst=revert(inst)
        #read a
        a="$"+str(inst.src1)
        g.debug(a)
        #read b if needed
        b=regs(i,inst.src2)
        g.debug(b)
    elif(isInt(inst.src1) and isInt(inst.src2)):
        if(isInt(inst.src1)):
            a="$"+str(inst.src1)
        g.debug(a)
        b=regs(i,"$"+str(inst.src2))
        g.debug(b)
    else:
        #read a if needed
        if(isInt(inst.src1)):
            a="$"+str(inst.src1)
        else:
            a=regs(i,inst.src1)
        g.debug(a)
        #read b if needed
        if(isInt(inst.src2)):
            b="$"+str(inst.src2)
        else:
            b=regs(i,inst.src2)
        g.debug(b)

    out('C',a,b)
    if(isInt(inst.src1) and isInt(inst.src2)):
        g.regalloc[isregassigned("$"+str(inst.src2))]='-1'

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

def FUNC(line):
    i=line
    SaveContext()
    out("CA",g.splitins[i].funcname)

def RET(line):
    out("M","%ebp","%esp")
    out("PO","%ebp")
    out("R")

def INPUT(line):
    i=line
    inp=regs(i,g.splitins[i].src1)
    out("PU","$L_INPUT")
    out("PU","$format_input")
    out("CA","scanf")
    out("M","L_INPUT",inp)

def PRINT(line):
    i=line
    inp=regs(i,g.splitins[i].src1)
    out("PU",inp)
    out("PU","$format_output")
    out("CA","printf")

def print_functions():
    g.debug(g.marker)
    for i in g.marker:
        if g.splitins[i].lbl==True:
            print(".type "+g.splitins[i].lblname+" , @function\n")
# def printexit():
#     print("\tmovl $1,%eax\n\tmovl $0,%ebx\n\tint $0x80")
def updatejumpttrgt():
    for k in g.marker:
        if(g.splitins[k].lbl==False):
            # g.splitins[k-1].lbl=True
            g.debug("dekh le"+str(k))
            g.splitins[k].lblname="l_"+g.splitins[k].lineno

def printlabelname(i,flag,fgl):
    if i in g.marker:
            g.debug("i am here"+str(i))
            if(g.splitins[i].lbl==True ):
                if(flag==1):
                    print("_exit:")
                    SaveContext()
                    out("M",1,"%eax")
                    out("M",0,"%ebx")
                    out("int","$0x80")
                    fgl=1
                flag=0
                print("\n"+g.splitins[i].lblname+":")
                out("PU","%ebp")
                out("M","%esp","%ebp")
            else:
                print("\n"+str(g.splitins[i].lblname)+":")
    return flag,fgl
    
def convertassem():
    flag=1
    fgl =0
    # print g.splitins
    createdatasection()
    g.debug(g.marker)
    updatejumpttrgt()
    for i in range(len(g.splitins)):
        flag,fgl=printlabelname(i,flag,fgl)       #If any
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
        elif(g.splitins[i].op=='%'):
            MOD(i)
        elif(g.splitins[i].op=='ifgoto'):
            IFGOTO(i)
        elif(g.splitins[i].func==True):
            FUNC(i)
        elif(g.splitins[i].returnc==True):
            RET(i)
        elif(g.splitins[i].lbl==True):
            continue;
        elif(g.splitins[i].inputc==True):
            INPUT(i)
        elif(g.splitins[i].printc==True):
            PRINT(i)
        else:
            g.splitins[i].printobj()
            raise ValueError("INVALID MODE:- Don't You know I m Idiot?")
    if(fgl==0):
        print("_exit:")
        SaveContext()
        out("M",1,"%eax")
        out("M",0,"%ebx")
        out("int","$0x80")

