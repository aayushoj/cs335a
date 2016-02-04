from logging import *
# from Handler import *

# FORMAT = "[%(levelname)s:%(filename)s:%(lineno)s] %(message)s"
FORMAT = "%(message)s"
basicConfig(format=FORMAT,level=DEBUG)

variables = []
basicblock=[]
nextuse = []
basicblock.append(0)
marker=[]
regalloc = ['-1']*6
splitins=[]
