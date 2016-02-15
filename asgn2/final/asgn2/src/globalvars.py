from logging import *

# Settings of debugger
# FORMAT = "[%(levelname)s:%(filename)s:%(lineno)s] %(message)s"
FORMAT = "%(message)s"
basicConfig(format=FORMAT,level=CRITICAL)

# list to store all variables
variables = []
# list to store all basicblocks
basicblock=[]
# list to store nextuse table
nextuse = []
# Append very first program point in basic block 
basicblock.append(0)
# list to store all labels
marker=[]
# mapping of reister to variables
regalloc = ['-1']*6
# list to store instructions
splitins=[]
