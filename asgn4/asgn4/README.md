Execution:
	cd asgn4
	make
	bin/irgen test/test1.java

The above steps will print the three address code and symbol table in the console


Features and Limitations:

1}Simple arithmetic expressions ( a= b op c  and a op= b) including bitwise operation. Shift operation is not handled at the moment.

2}Nested If else is handled.

3} for loop, while loop are implemented with break and continue. Enhanced for loop in java is not handled.

4}Non parameterised functions are handled( function which do not return any value).

5}Scope check is handled.

6} 1D arrays are handled. Assignments of this form ( a[] = {1,2,4}) is not handled. for assigning we use a[0]=1 and so on.

7} Only Integer data type is handled.

8} Input(in a special form) and print is handled.


Important Files :

1) ThreeAddressCode.py : It creates label, used for appending the quad and print the final ir code.
2) SymbolTable.py : It handles the scope and store variable for later checking. It also create temporary variables and scope names.
3)Parser.py : It checks the syntax error and some semantic errors. All semantic actions are implemented in this file.