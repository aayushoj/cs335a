all:
	mkdir -p bin
	cp src/lexer.py bin/lexer.py
	cp src/parser.py bin/irgen
	cp src/SymbolTable.py bin/SymbolTable.py
	cp src/ThreeAddressCode.py bin/ThreeAddressCode.py
	cp src/script.sh bin/script.sh
	chmod +x bin/irgen
	chmod +x bin/script.sh

clean:
	rm -r bin
	rm parser.out
	rm parsetab.py
