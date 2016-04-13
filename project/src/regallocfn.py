import globalvars as g

#returns true if string x represent a integer otherwise False
def isInt(x):
    x=str(x).strip(' ')
    if(x[0]=='-'):
        x=x[1:]
        return x.isdigit()
    else:
        return x.isdigit()

#builds nextusetable for all program points
def build_nextusetable():
    #print(type(basicblock[0]))
    # for i in range(1,len(basicblock)):
    #     for j in range(basicblock[i],basicblock[i-1],-1):
    #         print(str(j))
            # continue
    for i in range(1,len(g.basicblock)):
        newdiction  = {}
        newdiction['1line'] = -1
        for j in range(g.basicblock[i],g.basicblock[i-1],-1):
            # print("j="+str(j)+"asdas"+str(len(g.splitins)))
            # print("line no = " + str(j))
            newdiction['1line'] = j
            g.nextuse.insert(g.basicblock[i-1],newdiction.copy())
            if(g.splitins[j-1].dst!=None):
                if(g.splitins[j-1].dst in newdiction.keys()):
                    del newdiction[g.splitins[j-1].dst]
            if(g.splitins[j-1].src1!= None):
                if(isInt(g.splitins[j-1].src1)==False):
                    newdiction[g.splitins[j-1].src1]=j
            if(g.splitins[j-1].src2!= None):
                if(isInt(g.splitins[j-1].src2)==False):
                    newdiction[g.splitins[j-1].src2]=j
    # newdiction={}
    # newdiction['1line'] = len(g.splitins)+1
    # g.nextuse.insert(len(g.splitins)+1,newdiction.copy())
    #             print(g.splitins[j-1].src1)

# Returns which register is assgined to var and if no variable assigned returns '-1'
def isregassigned(var):
    if(isInt(var)):
        g.error("File:regallocfn.py=> isregassinged(): Error Spotted:---" +str(var))
    for i in range(0,6):
        if(g.regalloc[i]==var):
            return i
    return "-1"

# Mapping register to some integer
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
#eptyreg(lineno,reg) empties register reg using NextUseHeurestic
#(uses lineno for next use table and to take care of not removing variables of that line)
def emptyreg(lineno,regno):
    if(g.regalloc[regno]=='-1'):
        g.regalloc[regno]='0DNA'
        return True
    varsinline=[]
    varsinline.append(g.splitins[lineno-1].src1)
    varsinline.append(g.splitins[lineno-1].src2)
    varsinline.append(g.splitins[lineno-1].dst)
    for i in g.regalloc:
        if g.regalloc[isregassigned(i)]!='0DNA' and i not in g.nextuse[lineno-1].keys() and i not in varsinline:
            if(i!='-1'):
                g.debug( "empline no: "+str(lineno)+ " movl  "+str(regname(isregassigned(i))+","+str(i)))
                print("movl  "+str(regname(isregassigned(i))+" , "+str(i)))
                g.debug("empline no: "+str(lineno)+" movl "+regname(regno)+","+str(regname(isregassigned(i))))
                print("movl "+regname(regno)+" , "+str(regname(isregassigned(i))))
                g.regalloc[isregassigned(i)]=g.regalloc[regno]
                g.regalloc[regno]='0DNA'
            else:
                g.debug("empline no: "+str(lineno)+" movl "+regname(regno)+","+str(regname(isregassigned(i))))
                print("movl "+regname(regno)+" , "+str(regname(isregassigned(i))))
                g.regalloc[isregassigned(i)]=g.regalloc[regno]
                g.regalloc[regno]='0DNA'
            # print( "line no: "+str(lineno)+ " movl  "+str(regname(isregassigned(i))+","+str(i)))
            # regtoassign=isregassigned(i)
            # regalloc[regtoassign]='0DNA'
            return True
    tempvar=None
    tempnextuse=-1
    for j in range(0,6):
        if(g.regalloc[j]!='0DNA'):
            if g.regalloc[j] in varsinline:
                continue
            i=g.regalloc[j]
            if(tempnextuse==-1):
                tempvar=i
                tempnextuse=g.nextuse[lineno-1][i]
            elif(tempnextuse<g.nextuse[lineno-1][i]):
                    tempvar=i
                    tempnextuse=g.nextuse[lineno-1][i]
    g.debug("empline no: "+str(lineno)+ "  movl "+str(regname(isregassigned(tempvar))+","+str(tempvar)))
    print("movl "+str(regname(isregassigned(tempvar))+" , "+str(tempvar)))
    g.debug("empline no: "+str(lineno)+" movl "+regname(regno)+","+str(regname(isregassigned(tempvar))))
    print("movl "+regname(regno)+" , "+str(regname(isregassigned(tempvar))))
    g.regalloc[isregassigned(tempvar)]=g.regalloc[regno]
    g.regalloc[regno]='0DNA'
    return True

# Assigns a register to variable var.(Essentially main logic behind NextUseHeuristic)
def getreg(lineno,var):
    # mode = 0
    # if(g.splitins[lineno].op=="/" or g.splitins[lineno].op=="%"):
    # print("Abcd")
    ####NOT FOR DIV
    # if var not in g.nextuse[lineno-1].keys():
    #     return var
    varsinline=[]
    # print(lineno)
    # print(len(g.splitins))
    # print(g.splitins[lineno-1].src1)
    # print(g.splitins[lineno-1].src2)
    # print(g.splitins[lineno-1].op)
    # print(g.splitins[lineno-1].dst)
    if(lineno<=len(g.splitins)):
        varsinline.append(g.splitins[lineno-1].src1)
        varsinline.append(g.splitins[lineno-1].src2)
        varsinline.append(g.splitins[lineno-1].dst)
        varsinline.append("v_"+str(g.splitins[lineno-1].src1index))
        varsinline.append("v_"+str(g.splitins[lineno-1].src2index))
        varsinline.append("v_"+str(g.splitins[lineno-1].dstindex))
    else:
        g.error("Error GOT file: regallocfn.py => getreg()")
    # if(lineno==34):
    #     g.splitins[lineno-1].printobj()
    #     g.debug(varsinline)
    #     g.debug(g.regalloc)
    for i in range(6):
        if(g.regalloc[i]=='-1'):
            # allocatedreg=i
            g.regalloc[i]=var
            if(not('tempac'in var)):
                print("\tmovl "+var+" , "+regname(i))
            return regname(i)
    for i in g.regalloc:
        if i not in g.nextuse[lineno-1].keys() and i not in varsinline:
            print("\tmovl "+str(regname(isregassigned(i))+" , "+str(i)))
            # print("heelw")
            regtoassign=isregassigned(i)
            g.regalloc[regtoassign]=var
            print("\tmovl "+var+" , "+regname(regtoassign))
            return regname(regtoassign)
    tempvar=g.regalloc[0]
    tempnextuse=g.nextuse[lineno-1][tempvar]
    for j in range(1,6):
        i=g.regalloc[j]
        if i in varsinline:
            continue
        if(tempnextuse<g.nextuse[lineno-1][i]):
            tempvar=i
            tempnextuse=g.nextuse[lineno-1][i]
    # print("reg ass " + str(isregassigned(tempvar))+ " at" + regname(isregassigned(tempvar)))
    print("\tmovl "+str(regname(isregassigned(tempvar))+" , "+str(tempvar)))
    regtoassign=isregassigned(tempvar)
    g.regalloc[regtoassign]=var
    print("\tmovl "+var+" , "+regname(regtoassign))
    return regname(regtoassign)

# Assigns a register to varisble, var, if not already assigned and returns register name
def regs(i,var):

    tmp=isregassigned(var)
    if(tmp!="-1"):
        a=regname(tmp)
    else:
        a=getreg(i+1,var)
    return a

# getVar(reg) returns variables mapped to register "reg"
def getVar(str1):
    if(str1=="%ebx"):
        x=g.regalloc[0]
    elif(str1=="%ecx"):
        x=g.regalloc[1]
    elif(str1=="%esi"):
        x=g.regalloc[2]
    elif(str1=="%edi"):
        x=g.regalloc[3]
    elif(str1=="%eax"):
        x=g.regalloc[4]
    elif(str1=="%edx"):
        x=g.regalloc[5]
    else:
        raise ValueError("INVALID MODE:- Don't You know I m Idiot?")
    if(x=="-1" or x[0]=="$"):
        x="NULL"
    return x