There are four main files for this assignment:
1)tran.py: This reads the Highlevel Intermediate language. First it break each line into it's respective parameters, operations etc. For each line it calls a instruction class which returns an object after which the contents of that line is passed so that the object defines that line that is to say that it saves what operations is involves in this line, what are the parameters etc. After that we build the next use table so that we can use it to allocate register during runtime as the number of registers available are very limited (6 to be precise in x86). convertassem is called after this which converts the HIR language code into x86 assembly code.  

2)instruction.py: This defines the class instruction which in which an object has attributes like src1 which stands for source, funcname which stores the function name and so on. convert is a methid for this object which take a list which contains the contents of the lines already splitted by use of ",". We check the various possibilities for the first parameter like ifgoto, operations like +,-,/ etc. , label(definition of a function), ret and so on and we assign the various attributes of the object respectively. varname check for the identity of the variables whether it is just an integer or is it just a variable or an array element. For the last two it add a prefix of "v_" to them. printobject can be used to print the various attributes of the object.


3)assemblygen.py:


4)regallocfn.py: This 

5)globalvars.py:




getreg(lineno,var):
first check if there is any destination involved or not. Though it might not be reqd bt lets see if nt we  will remove it

second division mod or non division which is currently TODO item

if not then what it does is ki it simply allocates a register to the var specefied.
How??
first check if there is some reg which is yet to be assigned. if there is , then return that

if not then check if there is any var in reg which is not having any next use. If we find one such reg, we save it in memory and allocate this reg to var

else we then iterate through all the registers in nextuse and find the the variable currently assigned a reg having its farthest use. We then move this reg's value back in memory and then we will assign this register to the var


a lot is left to be done
