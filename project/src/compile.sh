#!/bin/bash
echo "Parsing the file and generating the IR code..."
python2 bin/parser.py $1 > Temp.ir
if [ "$?" = 0 ] 
then
    echo "done."
    echo "generating assembly file..."
    python2 bin/tran.py Temp.ir > out.s
    echo "done."
    echo "Generating binary file..."
    as --32 --gstabs out.s -o out.o
    ld -m elf_i386 out.o -lc -dynamic-linker /lib/ld-linux.so.2
    echo "done"
    case $2 in
        -o)
            mv a.out $3
    esac
    echo "Cleaning..."
    rm Temp.ir out.s out.o parsetab.py parser.out

    echo "done"
fi

