import globalvars as g


def isInt(x):
    x=str(x).strip(' ')
    if(x[0]=='-'):
        x=x[1:]
        return x.isdigit()
    else:
        return x.isdigit()
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
            print("j="+str(j)+"asdas"+str(len(g.splitins)))
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

    #             print(g.splitins[j-1].src1)

def isregassigned(var):
    if(isInt(var)):
        print("Error Spotted:---" +str(var))
    for i in range(0,6):
        if(g.regalloc[i]==var):
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
    if(g.regalloc[regno]=='-1'):
        g.regalloc[regno]=='0DNA'
        return True
    varsinline=[]
    varsinline.append(g.splitins[lineno].src1)
    varsinline.append(g.splitins[lineno].src2)
    varsinline.append(g.splitins[lineno].dst)
    for i in g.regalloc:
        if g.regalloc[isregassigned(i)]!='0DNA' and i not in g.nextuse[lineno-1].keys() and i not in varsinline:
            if(i!='-1'):
                print( "empline no: "+str(lineno)+ " movl  "+str(regname(isregassigned(i))+","+str(i)))
                print("empline no: "+str(lineno)+" movl "+regname(regno)+","+str(regname(isregassigned(i))))
                g.regalloc[isregassigned(i)]=g.regalloc[regno]
                g.regalloc[regno]='0DNA'
            else:
                print("empline no: "+str(lineno)+" movl "+regname(regno)+","+str(regname(isregassigned(i))))
                g.regalloc[isregassigned(i)]=g.regalloc[regno]
                g.regalloc[regno]='0DNA'
            # print( "line no: "+str(lineno)+ " movl  "+str(regname(isregassigned(i))+","+str(i)))
            # regtoassign=isregassigned(i)
            # regalloc[regtoassign]='0DNA'
            return True
    tempvar=None
    tempnextuse=-1
    for j in range(0,6) and g.regalloc[j]!='0DNA':
        if g.regalloc[j] in varsinline:
            continue
        i=g.regalloc[j]
        if(tempnextuse==-1):
            tempvar=i
            tempnextuse=g.nextuse[lineno-1][i]
        elif(tempnextuse<g.nextuse[lineno-1][i]):
                tempvar=i
                tempnextuse=g.nextuse[lineno-1][i]
    print("empline no: "+str(lineno)+ "  movl "+str(regname(isregassigned(tempvar))+","+str(tempvar)))
    print("empline no: "+str(lineno)+" movl "+regname(regno)+","+str(regname(isregassigned(tempvar))))
    g.regalloc[isregassigned(tempvar)]=g.regalloc[regno]
    g.regalloc[regno]='0DNA'
    return True



def getreg(lineno,var):
    # mode = 0
    # if(g.splitins[lineno].op=="/" or g.splitins[lineno].op=="%"):


    ####NOT FOR DIV
    for i in range(6):
        if(g.regalloc[i]=='-1'):
            # allocatedreg=i
            g.regalloc[i]=var
            return i
    for i in g.regalloc:
        if i not in g.nextuse[lineno-1].keys():
            print("movl "+str(regname(isregassigned(i))+" , "+str(i)))
            regtoassign=isregassigned(i)
            g.regalloc[regtoassign]=var
            return regtoassign
    tempvar=g.regalloc[0]
    tempnextuse=g.nextuse[lineno-1][tempvar]
    for j in range(1,6):
        i=g.regalloc[j]
        if(tempnextuse<g.nextuse[lineno-1][i]):
            tempvar=i
            tempnextuse=g.nextuse[lineno-1][i]
    # print("reg ass " + str(isregassigned(tempvar))+ " at" + regname(isregassigned(tempvar)))
    print("movl "+str(regname(isregassigned(tempvar))+" , "+str(tempvar)))
    regtoassign=isregassigned(i)
    g.regalloc[regtoassign]=var
    return regtoassign
# Amit Comments??
def regs(i,var):
    tmp=isregassigned(var)
    if(tmp!="-1"):
        a=regname(tmp)
    else:
        a=regname(getreg(i+1,var))
    return a


#Function added by Aayush
#getVar(reg) returns variables mapped to register "reg"
def getVar(str1):
    if(str1=="%ebx"):
        return regalloc[0]
    elif(str1=="%ecx"):
        return regalloc[1]
    elif(str1=="%esi"):
        return regalloc[2]
    elif(str1=="%edi"):
        return regalloc[3]
    elif(str1=="%eax"):
        return regalloc[4]
    elif(str1=="%edx"):
        return regalloc[5]
    else:
        raise ValueError("INVALID MODE:- Don't You know I m Idiot?")



# if(regno==0):
#         return '%ebx'
#     if(regno==1):
#         return '%ecx'
#     if(regno==2):
#         return "%esi"
#     if(regno==3):
#         return '%edi'
#     if(regno==4):
#         return '%eax'
#     if(regno==5):
#         return '%edx'