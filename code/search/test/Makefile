PROJECT_DIR=~/cosmos/cosmos/code/search
SRC_DIR=$(PROJECT_DIR)/src
TEST_DIR=$(PROJECT_DIR)/test

# where the cpputest library is located
CPPUTEST_HOME=~/cosmos/cosmos/code/search/test/cpputest

INCLUDE_DIRS=$(SRC_DIR)/* $(CPPUTEST_HOME)/include
SRC_DIRS=$(SRC_DIR)/*

# specify where the test code is located
TEST_SRC_DIRS = $(TEST_DIR)

# what to call the test binary
TEST_TARGET=example

CPPUTEST_USE_GCOV=Y
CPPUTEST_ENABLE_C99=Y

# run MakefileWorker.mk with the variables defined here
include $(CPPUTEST_HOME)/build/MakefileWorker.mk

# removes some compilation flags
CPPUTEST_WARNINGFLAGS:=$(filter-out -Werror,$(CPPUTEST_WARNINGFLAGS)) 

CPPUTEST_WARNINGFLAGS:=$(filter-out -Wpedantic,$(CPPUTEST_WARNINGFLAGS))

# adds some other warnings
CPPUTEST_WARNINGFLAGS+=-Wunused-result
