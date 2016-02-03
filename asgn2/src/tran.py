#!/usr/bin/python

import sys
import globalvars as g
from instruction import *

def codegen(infile):
    #ebx=1 ,ecx=2, esi=3, edi=4, eax=5, edx=6
    i=0
    filename = infile
    f = open(filename, 'r')
    data = f.read()
    lines=data.split('\n')
    g.splitins2 = []
    for i in lines:
        f=i.split(",")
        g.splitins2.append(f)
    g.splitins=[]
    x=[]
    for l in g.splitins2:
        x=[]
        for i in l:
            i=i.strip(" ")
            x.append(i)
        temp=instruction()
        temp.convert(x)
        if(len(x)!=1):
            g.splitins.append(temp)
    g.basicblock.append(len(g.splitins))
    # for i in g.splitins:
    #     i.printobj()
    unique = set(g.variables)
    g.variables = list(unique)
    g.basicblock.sort()
    print(g.basicblock)
    print(g.marker)
    build_nextusetable()
    print("*********************************************************************************")
    for i in g.nextuse:
        print(i)
    print("*********************************************************************************")
    createdatasection()
    convertassem()
if __name__ == '__main__':
    codegen(sys.argv[1])
