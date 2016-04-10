all:
	python3 tran.py newin.txt
	cat out.s

clean:
	rm *.o *.pyc *.s

%.o: %.s *.py
	as --32 --gstabs $< -o $@
	ld -m elf_i386 $@ -lc -dynamic-linker /lib/ld-linux.so.2

%.s: test/%.txt tran.py
	python3 tran.py $< > $@