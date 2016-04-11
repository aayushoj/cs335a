all : binary

binary :
	mkdir -p bin
	cp src/assemblygen.py bin/assemblygen.py
	cp src/globalvars.py bin/globalvars.py
	cp src/instruction.py bin/instruction.py
	cp src/regallocfn.py bin/regallocfn.py
	cp src/tran.py bin/codegen
	chmod +x bin/codegen

clean:
	rm -r bin
	rm *.o *.s *.out

assembly:
	as --32 --gstabs out.s -o out.o
	ld -m elf_i386 out.o -lc -dynamic-linker /lib/ld-linux.so.2

assembly2:
	as --32 --gstabs out2.s -o out.o
	ld -m elf_i386 out.o -lc -dynamic-linker /lib/ld-linux.so.2