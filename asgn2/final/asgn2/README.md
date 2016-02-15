GROUP 30
Sourav Anand - 13709
Shubham Jain - 13683
Amit Kumar - 13094
Aayush Ojha - 13009

Building and running
run make in asgn2 folder.

Running the generated assembly file:
save the file as out.s
run the following 2 commands in the directory containing out.s

as --32 --gstabs out.s -o out.o
ld -m elf_i386 out.o -lc -dynamic-linker /lib/ld-linux.so.2

alternatevely, we can save the file as out.s in the asgn2 folder and run "make assembly". It will generate an executable a.out


TEST FILES:
test1.ir - Array output : 19,21
test2.ir - factorial    :  takes an integer input and prints its factorial
test3.ir - gcd			returns gcd of 14 and 8
test4.ir - highest power of 2  :takes an input and returns the highest power of two smaller than the input
test5.ir - live			: a random test case containing a lot of variables and operations to test spilling
test6.ir - logic		: a test case to test logical operators AND,OR,XOR,NOT
test7.ir - power		: return 5^4
test8.ir - prime		: returns the first smallest prime factor of a number



IMPLEMENTATION DETAILS:


There are four main files for this assignment:

1)tran.py: This reads the Highlevel Intermediate language. First it break each line into it's respective parameters, operations etc. For each line it calls a instruction class which returns an object after which the contents of that line is passed so that the object defines that line that is to say that it saves what operations is involves in this line, what are the parameters etc. It also takes care when a basic block has ended and repectively append the start and ending line of it. After that we build the next use table so that we can use it to allocate register during runtime as the number of registers available are very limited (6 to be precise in x86). convertassem is called after this which converts the HIR language code into x86 assembly code.  

2)instruction.py: This defines the class instruction which in which an object has attributes like src1 which stands for source, funcname which stores the function name and so on. convert is a methid for this object which take a list which contains the contents of the lines already splitted by use of ",". We check the various possibilities for the first parameter like ifgoto, operations like +,-,/ etc. , label(definition of a function), ret and so on and we assign the various attributes of the object respectively. varname check for the identity of the variables whether it is just an integer or is it just a variable or an array element. For the last two it add a prefix of "v_" to them. printobject can be used to print the various attributes of the object.


3)assemblygen.py: This file convert the whole program to assembly code. First it creates the data section by calling the createdatasection function. The function defines all the temporary variables, variables defined by the program, it also enlist all the functions by calling print_functions which iterated over the lines so find all the places where a function is defined. It then updates all the places where we have jump statements and label the respective line which are the destinations of those jumps. After this it goes over line by line and translate the lines into assembly code taking care of the various nuances that might arise. It also has input and print statements which uses the predefined scanf and printf functions. Out functions manages all type of outputs/generations in the final assembly file centrally. SaveContext is called whenever a basic block ends which save the contents of the the registers back to ther respective variables


4)regallocfn.py: This file contains the functions which are required for register allocation to the variables. This file also contains the function build_next_use to build next use table for register allocation. There are two functions getreg and emptyreg to allocate a register to a variable. getreg is used to allocate a register to the variable (var in its param). It does so by first checking for any empty register. If it finds one, it allocates this register to var else it then checks for any variable in the registers which is not having any next use. If it finds one, it first saves the variable in that register in memory and allocates this register to the variable. If this also fails then it looks for a varable having the furthest next use, spill it and move it back to the memory and allocates this register to the variable. Emptyreg also works in the similar way but it allocates a specific register to the variable (it is used by division and modulo operators).

Apart from these, there are some helper functions such as isregassigned which simply checks if the varable is assigned any register and one regname function which translates register number to registers name (we defined a map between register no and register name) and one more function which simply returns the variable stored in that variable.

5)globalvars.py: Defines the various global variables that we are using like variable list, basic block list, next use tables etc.

Brief description of our three address code:
1. +. a, b, c represents a=b+c and similarily for sub, mul, divide and modulus
2. and, a, b, c represents a= b&c and similarily for or and xor
3. not, a, b represents a=!b
4. print, a represents printf a
5. input, a represets scanf a
6. Array: At max one array element will be opearated on in one line. The parser will make sure that whenever a line has more than one operands as array elements, it will change/break the line such that there is at max one array operations and the operator is equal. It will use temp variables as a delegate for these array elements in the calculations/operations involved.

