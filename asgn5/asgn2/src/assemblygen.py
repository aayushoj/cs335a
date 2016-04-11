
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

# Use to print instructions in assembly
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
    elif(mode=='AN'):
        Instr="and "
        Output=Instr+str1+" , "+str2
    elif(mode=='OR'):
        Instr="or "
        Output= Instr + str1+" , "+ str2
    elif(mode=='XO'):
        Instr="xor "
        Output= Instr + str1+" , "+ str2
    elif(mode=='NO'):
        Instr="not "
        Output= Instr + str1
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

# Saves Context before going to next basic block called before jumps. 
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
    # Reset the mapping of register to variables
    for i in range(0,6):
        g.regalloc[i]='-1'

# Creates the data secction for assembly code
def createdatasection():
    tempvar=['tempac1','tempac2','tempac3','tempac4','tempac5','tempac6','tempretaddr']
    print(".section .data")
    # strIO="format_input:\n\t.ascii \"%d\\0\"\nformat_output:\n \t.ascii \"%d\\n\\0\"\nL_INPUT:\n\t.long 0"
    # print(strIO)
    for i in g.printstrings:
        # g.debug("data"+i[0])
        print(i[0]+":\n\t.ascii "+i[1]+"\n")
    print("format_input:\n\t.ascii \"%d\\0\"\n"+"L_INPUT:\n\t.long 0\n")
    # print("array_block:")
    # print("\t.fill 100")
    for i in g.variables :
        if (isInt(i)):
            continue
        print(str(i[0])+":")
        if(i[1]==0):
            print("\t.long 0")
        else:
            print("\t.fill "+str(i[1]))
    for i in tempvar :
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
    # print("\n _start:")

#handles all cases of addition
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

#handles all cases of Multiplication
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

#handles all cases of division
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
            c=regs(i,'tempac1')
            out("M",a,c)
            out("M",g.splitins[i].src1,a)
            out("CD")
            out("D",c)
            g.regalloc[isregassigned('tempac1')]='-1'
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
            c=regs(i,'tempac2')
            out("M",a,c)
            out("M",b,a)
            out("CD")
            out("D",c)
            g.regalloc[isregassigned('tempac2')]='-1'
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

#handles all cases of modulus operation
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
            c=regs(i,'tempac3')
            out("M",a,c)
            out("M",g.splitins[i].src1,a)
            out("CD")
            out("D",c)
            out("M","%edx",a)
            g.regalloc[isregassigned('tempac3')]='-1'
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
            c=regs(i,'tempac4')
            out("M",a,c)
            out("M",b,a)
            out("CD")
            out("D",c)
            out("M","%edx",a)
            g.regalloc[isregassigned('tempac4')]='-1'
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

#handles all cases of substraction
def SUB(line):
    i=line
    if(isInt(g.splitins[i].src1) or isInt(g.splitins[i].src2)):
        if(isInt(g.splitins[i].src1) and isInt(g.splitins[i].src2)):
            a=regs(i,g.splitins[i].dst)
            out("M",g.splitins[i].src1,a)
            out("S",g.splitins[i].src2,a)
        elif(isInt(g.splitins[i].src1)):
            if(g.splitins[i].dst!=g.splitins[i].src2):
                b=regs(i,g.splitins[i].src2)
                a=regs(i,g.splitins[i].dst)
                out("M",0,a)
                out("S",b,a)
                out("A",g.splitins[i].src1,a)
            else:
                a=regs(i,g.splitins[i].dst)
                tmp=regs(i,"tempac5")
                out("M",a,tmp)
                out("M",g.splitins[i].src1,a)
                out("S",tmp,a)
                g.regalloc[isregassigned('tempac5')]='-1'
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

#handles all cases of assignment
def EQUAL(line):
    i=line
    if(g.splitins[i].dstindex!=None and isInt(g.splitins[i].src1)):
        if(isInt(g.splitins[i].dstindex)):
            emptyreg(i,5)
            out("M",g.splitins[i].dstindex,"%edx")
            tmp=regs(i,"tempac6")
            # print("movl $array_block , "+tmp)
            out("M","$"+str(g.splitins[i].dst),tmp)
            # print("movl $"+g.splitins[i].src1+ " , "+ "("+tmp+",%edx,4)")
            out("M",g.splitins[i].src1,"("+tmp+",%edx,4)")
            g.regalloc[5]='-1'
        else:
            emptyreg(i,4)
            tmp = regs(i,"v_"+g.splitins[i].dstindex)
            # print("movl $array_block , %eax")
            out("M","$"+str(g.splitins[i].dst),"%eax")
            # print("movl $"+g.splitins[i].src1+ " , "+ "(%eax"+","+tmp+",4)")
            out("M",g.splitins[i].src1,"(%eax"+","+tmp+",4)")
            g.regalloc[4]='-1'
    elif(g.splitins[i].dstindex!=None and (not isInt(g.splitins[i].src1))):
        if(isInt(g.splitins[i].dstindex)):
            emptyreg(i,5)
            emptyreg(i,4)
            b= regs(i,g.splitins[i].src1)
            out("M",g.splitins[i].dstindex,"%edx")
            # print("movl $array_block , %eax")
            out("M","$"+str(g.splitins[i].dst),"%eax")
            # print("movl "+b+ " , "+ "(%eax+,%edx,4)")
            out("M",b,"(%eax,%edx,4)")
            g.regalloc[5]='-1'
            g.regalloc[4]='-1'
        else:
            emptyreg(i,4)
            tmp = regs(i,"v_"+g.splitins[i].dstindex)
            b= regs(i,g.splitins[i].src1)
            # if(tmp==b):
            #     print("error in EQUAL registers same")
            # print("movl $array_block , %eax")
            out("M","$"+str(g.splitins[i].dst),"%eax")
            # print("movl "+b+ " , "+ "(%eax"+","+tmp+",4)")
            out("M",b,"(%eax"+","+tmp+",4)")
            g.regalloc[4]='-1'

    elif(g.splitins[i].src1index!=None):
        if(isInt(g.splitins[i].src1index)):
            emptyreg(i,5)
            emptyreg(i,4)
            out("M",g.splitins[i].src1index,"%edx")
            a=regs(i,g.splitins[i].dst)
            # print("movl $array_block , %eax")
            out("M","$"+str(g.splitins[i].src1),"%eax")
            # print("movl (%eax,%edx,4) , "+a)
            out("M","(%eax,%edx,4)",a)
            g.regalloc[5]='-1'
            g.regalloc[4]='-1'
        else:
            emptyreg(i,4)
            a = regs(i,g.splitins[i].dst)
            tmp = regs(i,"v_"+g.splitins[i].src1index)
            # if(tmp==a):
            #     print("error in EQUAL registers same")
            # print("movl $array_block , %eax")
            out("M","$"+str(g.splitins[i].src1),"%eax")
            # print("movl (%eax,"+tmp+",4) , "+a)
            out("M","(%eax,"+tmp+",4)",a)
            g.regalloc[4]='-1'
    elif(isInt(g.splitins[i].src1)):
        a=regs(i,g.splitins[i].dst)
        out("M",g.splitins[i].src1,a)
        # print("movl $"+ g.splitins[i].src1 + " , " + str(a))
    else:
        a=regs(i,g.splitins[i].dst)
        b=regs(i,g.splitins[i].src1)
        # print("movl "+ str(b) + " , " + str(a))
        out("M",b,a)

#handles all cases of bitwise and
def AND(line):
    i=line
    if(isInt(g.splitins[i].src1) or isInt(g.splitins[i].src2)):
        if(isInt(g.splitins[i].src1) and isInt(g.splitins[i].src2)):
            a=regs(i,g.splitins[i].dst)
            out("M",g.splitins[i].src1,a)
            out("AN",g.splitins[i].src2,a)
        elif(isInt(g.splitins[i].src1)):
            b=regs(i,g.splitins[i].src2)
            a=regs(i,g.splitins[i].dst)
            out("M",b,a)
            out("AN",g.splitins[i].src1,a)
        else:
            b=regs(i,g.splitins[i].src1)
            a=regs(i,g.splitins[i].dst)
            out("M",b,a)
            out("AN",g.splitins[i].src2,a)
    else:
        if(g.splitins[i].dst !=g.splitins[i].src1 and g.splitins[i].dst !=g.splitins[i].src2):
            b=regs(i,g.splitins[i].src1)
            c=regs(i,g.splitins[i].src2)
            a=regs(i,g.splitins[i].dst)
            out("M",c,a)
            out("AN",b,a)
        elif(g.splitins[i].dst ==g.splitins[i].src1 and g.splitins[i].dst !=g.splitins[i].src2):
            c=regs(i,g.splitins[i].src2)
            a=regs(i,g.splitins[i].dst)
            out("AN",c,a)
        elif(g.splitins[i].dst !=g.splitins[i].src1 and g.splitins[i].dst ==g.splitins[i].src2):
            b=regs(i,g.splitins[i].src1)
            a=regs(i,g.splitins[i].dst)
            out("AN",b,a)
        elif(g.splitins[i].dst ==g.splitins[i].src1 and g.splitins[i].dst ==g.splitins[i].src2):
            a=regs(i,g.splitins[i].dst)
            out("AN",a,a)

#handles all cases of bitwise or
def OR(line):
    i=line
    if(isInt(g.splitins[i].src1) or isInt(g.splitins[i].src2)):
        if(isInt(g.splitins[i].src1) and isInt(g.splitins[i].src2)):
            a=regs(i,g.splitins[i].dst)
            out("M",g.splitins[i].src1,a)
            out("OR",g.splitins[i].src2,a)
        elif(isInt(g.splitins[i].src1)):
            b=regs(i,g.splitins[i].src2)
            a=regs(i,g.splitins[i].dst)
            out("M",b,a)
            out("OR",g.splitins[i].src1,a)
        else:
            b=regs(i,g.splitins[i].src1)
            a=regs(i,g.splitins[i].dst)
            out("M",b,a)
            out("OR",g.splitins[i].src2,a)
    else:
        if(g.splitins[i].dst !=g.splitins[i].src1 and g.splitins[i].dst !=g.splitins[i].src2):
            b=regs(i,g.splitins[i].src1)
            c=regs(i,g.splitins[i].src2)
            a=regs(i,g.splitins[i].dst)
            out("M",c,a)
            out("OR",b,a)
        elif(g.splitins[i].dst ==g.splitins[i].src1 and g.splitins[i].dst !=g.splitins[i].src2):
            c=regs(i,g.splitins[i].src2)
            a=regs(i,g.splitins[i].dst)
            out("OR",c,a)
        elif(g.splitins[i].dst !=g.splitins[i].src1 and g.splitins[i].dst ==g.splitins[i].src2):
            b=regs(i,g.splitins[i].src1)
            a=regs(i,g.splitins[i].dst)
            out("OR",b,a)
        elif(g.splitins[i].dst ==g.splitins[i].src1 and g.splitins[i].dst ==g.splitins[i].src2):
            a=regs(i,g.splitins[i].dst)
            out("OR",a,a)

#handles all cases of bitwise xor
def XOR(line):
    i=line
    if(isInt(g.splitins[i].src1) or isInt(g.splitins[i].src2)):
        if(isInt(g.splitins[i].src1) and isInt(g.splitins[i].src2)):
            a=regs(i,g.splitins[i].dst)
            out("M",g.splitins[i].src1,a)
            out("XO",g.splitins[i].src2,a)
        elif(isInt(g.splitins[i].src1)):
            b=regs(i,g.splitins[i].src2)
            a=regs(i,g.splitins[i].dst)
            out("M",b,a)
            out("XO",g.splitins[i].src1,a)
        else:
            b=regs(i,g.splitins[i].src1)
            a=regs(i,g.splitins[i].dst)
            out("M",b,a)
            out("XO",g.splitins[i].src2,a)
    else:
        if(g.splitins[i].dst !=g.splitins[i].src1 and g.splitins[i].dst !=g.splitins[i].src2):
            b=regs(i,g.splitins[i].src1)
            c=regs(i,g.splitins[i].src2)
            a=regs(i,g.splitins[i].dst)
            out("M",c,a)
            out("XO",b,a)
        elif(g.splitins[i].dst ==g.splitins[i].src1 and g.splitins[i].dst !=g.splitins[i].src2):
            c=regs(i,g.splitins[i].src2)
            a=regs(i,g.splitins[i].dst)
            out("XO",c,a)
        elif(g.splitins[i].dst !=g.splitins[i].src1 and g.splitins[i].dst ==g.splitins[i].src2):
            b=regs(i,g.splitins[i].src1)
            a=regs(i,g.splitins[i].dst)
            out("XO",b,a)
        elif(g.splitins[i].dst ==g.splitins[i].src1 and g.splitins[i].dst ==g.splitins[i].src2):
            a=regs(i,g.splitins[i].dst)
            out("XO",a,a)

#handles all cases of bitwise not
def NOT(line):
    i=line
    if(isInt(g.splitins[i].src1)):
        a=regs(i,g.splitins[i].dst)
        out("M",g.splitins[i].src1,a)
        out("NO", a)
    else:
        a=regs(i,g.splitins[i].dst)
        b=regs(i,g.splitins[i].src1)
        out("M",b,a)
        out("NO",a)

# sometimes for optimality we will revert comparisons
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

# handles all cases of ifgoto instruction
def IFGOTO(line):
    i=line
    inst=g.splitins[i]
    SaveContext()
    for i in range(0,6):
        g.debug(i)
        if(g.regalloc[i]!='-1'):
            g.debug("i dont know why?")
    i=line
    (inst.src1,inst.src2)=(inst.src2,inst.src1)
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
    g.debug("ifgoto issue " + inst.jlno)
    # if(isInt(inst.lineno)):
    #     label="l_"+str(inst.jlno)
    # else:
    label="l_"+str(inst.jlno)
    #Save Context before jump
    SaveContext()
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
        #For debugging
        raise ValueError("INVALID LABEL:-  IFGOTO() in file assemblygen.py")

# handles instruction call :
# this instruction calls a function
def FUNC(line):
    i=line
    SaveContext()
    out("CA",g.splitins[i].funcname)

# handles all cases of ret 
def RET(line):
    SaveContext()
    out("M","%ebp","%esp")
    out("PO","%ebp")
    out("PO", "tempretaddr")
    i=line
    var=isregassigned(g.splitins[i].dst)
    g.debug("func::push--var="+str(var))
    if(var!='-1'):
        out("PU",regname(var))
    else:
        out("PU",g.splitins[i].dst)
    out("PU", "tempretaddr")
    out("R")

# handles instruction:- input, a
# uses C-function scanf for this
def INPUT(line):
    i=line
    SaveContext()
    inp=regs(i,g.splitins[i].src1)
    out("PU","$L_INPUT")
    out("PU","$format_input")
    out("CA","scanf")
    out("M","L_INPUT",inp)

# handles instruction:- print, a
# uses C-function printf for this
def PRINT(line):
    i=line
    SaveContext()
    # if(not isInt(g.splitins[i].src1)):
    #     inp=regs(i,g.splitins[i].src1)
    g.debug("print line strs ::"+str(g.splitins[i].paramlist))
    for j in range(1,len(g.splitins[i].paramlist)):
        g.debug("j::"+str(j))
        g.debug("list "+str(g.splitins[i].paramlist[j]))
        k=len(g.splitins[i].paramlist)-j
        if(g.splitins[i].paramlist[k][1]==None):
            out("PU",g.splitins[i].paramlist[k][0]) #pushing in opp dir
    # out("PU",inp)
    # out("PU","$format_output")
    out("PU",g.splitins[i].paramlist[0])
    out("CA","printf")

def PUSH(line):
    i=line
    var=isregassigned(g.splitins[i].dst)
    g.debug("func::push--var="+str(var))
    if(var!='-1'):
        out("PU",regname(var))
    else:
        out("PU",g.splitins[i].dst)

def POP(line):
    i=line
    var=isregassigned(g.splitins[i].dst)
    if(var!='-1'):
        out("PO",regname(var))
    else:
        out("PO",g.splitins[i].dst)

def GOTO(line):
    i=line
    inst=g.splitins[i]
    SaveContext()
    out("JMP",inst.jlno)
# defines labels to be function in Assembly Code
def print_functions():
    g.debug(g.marker)
    for i in g.marker:
        if g.splitins[i].lbl==True and g.splitins[i].lblname!="u_main":
            print(".type "+g.splitins[i].lblname+" , @function\n")

# UNCOMMENTED
# def updatejumpttrgt():
#     for k in g.marker:
#         if(g.splitins[k].lbl==False):
#             # g.splitins[k-1].lbl=True
#             g.debug("Lets see: "+str(k))
#             g.splitins[k].lblname="l_"+g.splitins[k].lineno

#prints labels on required lines of Assembly Code
def printlabelname(i,flag,fgl):
    if i in g.marker:
            g.debug("Check It:- "+str(i))
            if(g.splitins[i].lbl==True):
                if(flag==1):
                    print("_exit:")
                    SaveContext()
                    out("M",1,"%eax")
                    out("M",0,"%ebx")
                    out("int","$0x80")
                    fgl=1
                    flag=0
                
                print("\n"+g.splitins[i].lblname+":")
                g.debug(str(g.splitins[i].paramlist[0][0]))
                out("PO","tempretaddr")
                for j in range(0,len(g.splitins[i].paramlist )):
                    k=len(g.splitins[i].paramlist)-j-1
                    out("PO",g.splitins[i].paramlist[k][0])                
                out("PU","tempretaddr")
                out("PU","%ebp")
                out("M","%esp","%ebp")
            else:
                SaveContext()
                print("\n"+str(g.splitins[i].lblname)+":")
    return flag,fgl

#Converts every instruction to corresponding assembly code
def convertassem():
    flag=0
    fgl =0
    #Create data section of Assembly Code
    createdatasection()
    g.debug(g.marker)
    # UNCOMMENTED
    # updatejumpttrgt()
    for i in range(len(g.splitins)):
        if(g.splitins[i].lblname=="u_main"):
            print "\n_start:"
            flag=1
        elif(g.splitins[i].op == 'func'):
            flag,fgl=printlabelname(i,flag,fgl)
        elif(g.splitins[i].op == 'label'):
            print("\n"+str(g.splitins[i].lblname)+":")
        elif(g.splitins[i].op == '='):
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
        elif(g.splitins[i].op=="goto"):
            GOTO(i)
        elif(g.splitins[i].op== 'and'):
            AND(i)
        elif(g.splitins[i].op== 'or'):
            OR(i)
        elif(g.splitins[i].op== 'xor'):
            XOR(i)
        elif(g.splitins[i].op== 'not'):
            NOT(i)
        elif(g.splitins[i].op=='push'):
            PUSH(i)
        elif(g.splitins[i].op=='pop'):
            POP(i)
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
        elif(g.splitins[i].op=='declare'):
            continue
        else:
            #Only for debugging
            g.splitins[i].printobj()
            raise ValueError("INVALID MODE:- Don't You know I m Idiot?")
    if(fgl==0):
        print("_exit:")
        SaveContext()
        out("M",1,"%eax")
        out("M",0,"%ebx")
        out("int","$0x80")
