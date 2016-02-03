all:
	python tran.py newin.txt
	cat out.s

clean:
	rm out.s

compile:
	as -32 --gstabs out.s -o out.o
	ld -m elf_i386 out.o
