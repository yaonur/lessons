#!/bin/bash

nasm -f elf64 hello.asm -o out/hello.o
ld -s -o out/hello out/hello.o
./out/hello
