#Makefile to build a static library

CC = gcc

SRC_DIR=./src
CODE_DIR=$(SRC_DIR)/*
OBJ_DIR=obj

_OBJ = exponential_search.o fibonacci_search.o jump_search.o ternary_search.o binary_search.o interpolation_search.o linear_search.o
OBJ = $(patsubst %,$(OBJ_DIR)/%,$(_OBJ))

#building object file of each .c file
$(OBJ_DIR)/%.o: $(CODE_DIR)/%.c
	mkdir -p $(OBJ_DIR)
	$(CC) -c -o $@ $<

liball.a: $(OBJ)
	ar rc liball.a $^
	ranlib liball.a

build: liball.a

.PHONY: clean

clean:
	rm -f $(OBJ_DIR)/*.o *~ core $(INCDIR)/*~
	rm -rf $(OBJ_DIR)
	rm -f liball.a
