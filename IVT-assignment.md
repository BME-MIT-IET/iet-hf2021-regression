our contribution consisted of 5 parts:

CI and static techniques:

- Adding a build framework by Makefile (Weheash Ashraf Ahmed Elazab Ahmed - HTAEOU)
- Running a static analysis tool and reviewing the reported problems using Codacy (Khuderchuluun Erdenechuluun-GTBHX0)
- Performing manual code review on some part of the application(Batsaikhan Khosbayar-L2N9IX)

Testing:

- Creating or extending unit tests (Weheash Ashraf Ahmed Elazab Ahmed-HTAEOU)
- Designing, executing and documenting manual tests (Achref Mekni-RMPSYJ)

we have chosen these tasks since this repository is a collection of libraries and these were
the most efficient CI & static techniques and testing tasks to apply on such repository.

Overview:

Static Analysis:

It is a method of debugging that is done by examining the code without executing the program. The process provides an understanding of the code structure and help us to review issues in the libraries. We used Codacy as static analyser. It analyzed various of issues to review and fix after analysing the libraries

Manual Code Review:

As we are doing manual code review on Search and Sort libraries, we have wrote down our review on document which can be found
in doc/manualReview.md and suggested changes are commited.

Manual Testing:

it consists of 2 parts which are Performance Testing that measures the performance(time complexity) of
several functions in the search library & Functional Testing that combines 2 libraries (search+sort)
and tests if their usage seperately and together is efficient and doesnt cause any execution problem

Build framework:

Makefile build system is used to create a static library of a collection of specified .c or .cpp files. In the current development, all files of algorithms under /search/ directories has been built together in liball.a static library which can make the functionality of the algorithms portable and reusable. 

Unit Testing:

First, a special framework for the environment had to be implemented using Cpputest to unit test .c files only. Afterwards, all tests are collected together in all_search_tests.c that covers the basic unit testing for the .c files in /search/ directory.
Conclusion:

we've learned how to contribute to different parts of an open-source project by applying certain testing,CI & static techniques.
we've created issues related to each task. we fixed some code/syntax/logical errors after seeing the results of our tests
and discovering which parts were erroneous.
