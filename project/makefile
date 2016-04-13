all : binary

binary :
	rm -rf bin 
	mkdir -p bin
	cp src/assemblygen.py bin/assemblygen.py
	cp src/globalvars.py bin/globalvars.py
	cp src/instruction.py bin/instruction.py
	cp src/regallocfn.py bin/regallocfn.py
	cp src/tran.py bin/tran.py
	cp src/lexer.py bin/lexer.py
	cp src/parser.py bin/parser.py
	cp src/SymbolTable.py bin/SymbolTable.py
	cp src/ThreeAddressCode.py bin/ThreeAddressCode.py
	cp src/compile.sh bin/compile.sh
	chmod +x bin/compile.sh

clean:
	rm -r bin
	rm *.o *.s *.out

assembly:
	as --32 --gstabs out.s -o out.o
	ld -m elf_i386 out.o -lc -dynamic-linker /lib/ld-linux.so.2
