CC := gcc
FLAGS := -std=c99 -Wall -Werror -Wextra -Wfloat-equal -Wfloat-conversion
U_FLAGS := -lcheck -lpthread -lrt -lm -lsubunit
FUNC_VLG :=

SRC_DIR := ./src
INC_DIR := ./src
OBJ_DIR := ./out

SRC := $(wildcard $(SRC_DIR)/*.c)
INC := $(wildcard $(INC_DIR)/*.h)

OBJ := $(patsubst $(SRC_DIR)/%.c, $(OBJ_DIR)/%.o, $(SRC))

INC_HD := -I$(INC_DIR)

LIB := libarr.so

$(LIB) : $(OBJ)
	$(CC) -shared $^ -o $@

$(OBJ_DIR):
	@mkdir -p $@

$(OBJ_DIR)/%.o : $(UNIT_DIR)/%.c $(INC) $(OBJ_DIR)
	$(CC) $(INC_HD) $(FLAGS) $(U_FLAGS) -c $< -o $@

$(OBJ_DIR)/%.o : $(SRC_DIR)/%.c $(INC) $(OBJ_DIR)
	$(CC) $(INC_HD) $(FLAGS) -c $< -o $@

.PHONY : clean func

clean:
	rm -rf $(OBJ_DIR) *.exe *.txt ./func_tests/*.txt *.a *.so;
 
run: $(LIB)
	@export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:.; python3 interface/main.py
