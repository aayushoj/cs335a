Group 30 
Aayush Ojha - 13009 
Amit Kumar - 13094 
Shubham Jain - 13683 
Sourav Anand - 13709

Files: 
Ply.py: 
The lexer that converts a java file to tokens We have 6 tokens: 
	1)Keyword 
	2)Identifier 
	3)Literals 
	4)Separator 
	5)Comments 
	6)Operator

We have written the regular expression for each token and and arranged the token in a order so that maximal munching gives correct result.

As a token is read its count is incresed and it is added to the set of its token type Uncommenting the line 
 print(tok) can print every token that is calculated Illegal entry is made for variables that start with a number literals

For printing the individual token we have used set so that a token is printed twice but their occurences will increase so the occurance would be correct

Test files 
	1. test1.java : checks different identifier names 
	2. test2.java : contains the code for the factorial function 
	3. test3.java : contains various operation that are done on strings 
	4. test4.java : has the bubblesort algorithm 
	5. test5.java : tower of hanoi solution