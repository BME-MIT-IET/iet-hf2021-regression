## Makefile Build Framework:

* The first component of the branch work is building a Build framework for .c / .cpp files to build static libraries. The system used is the accumlation building system Makefile. Before using Makefile, it should be installed in the system (preferably Linux system). The details of the system and how it can be used can be found here: https://www.gnu.org/software/make/manual/make.html#Makefile-Arguments

* The framework works on only .c files of the search/src directory and collects the object files (.o) built collectively through the main Makefile in search/ directory, and then builds a static library. This static library makes the code portable and easily reusable.

* The output of the build is liball.a static library.

## Cpputest Framework

* The second part of the work is about building and integerating the Cpputest framework and create unit tests for all algorithms under /search/src directory. The process of creating is the following:
1. Downloading Cpputest 
2. Installing Cpputest under /search/test/   
3. Building the framework components:
    - a) AllTests.cpp file to initiate the tests
    - b) /search/test/Makefile which is the building system for the unit tests. It uses MakefileWorker.mk by setting the prerequisite variables and then calls it.
    - c) all_search_tests.cpp which is the unit tests file

4. Deleting the main() part of all .c files and moving the implementation to all_search_tests.cpp as this is the proper way of such tests.

### NOOTE:
Both the build and cpputest frameworks can be extended and further generalized for other directories and files based on the requirements.
 

