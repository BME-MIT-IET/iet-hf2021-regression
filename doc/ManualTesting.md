Manual Testing:
- Performance Test (search)
- Functional Test (sort+search)

Testing Plan:

- the Performance testing is based on Python timeit() which is a method in Python library to measure the execution time taken by the given code snippet or function. 
The Python library runs the code statement 1 million times and provides the minimum time taken from the given set of code snippets. 
Python timeit() is a useful method that helps in checking the performance of the code.

  the idea is to run each searching function n times (n=10000) on randomly generated arrays and then calculate the average time. the process is repeated 3 times and 
  then i get 3 time results.i picked the minimal value out of these 3 to get an optimal value.

- the Functional Test is based on pytest library which is a testing framework that allows users to write test codes using Python programming language. 
It helps you to write simple and scalable test cases

  the idea is to combine 2 libraries from the repository and see if they work together or not.So all the test cases scenarios are the following:
  the function takes an array & x as a parameter, first it sorts the array using a sorting algorithm from the sort library then it searches for x in the sorted 
  array using a searching algorithm from the search library.Finally we need to assert & compare the result with the expected output that i already initialized.


Results:

Performance Testing:

![image](https://user-images.githubusercontent.com/61314172/118402354-e2edf900-b669-11eb-8ea4-d4d8b637ee5d.png)

from the Performance Testing we can deduce that:
->the ternary search is the most optimal performing algorithm out of the search algorithms (6.6823 s)
which is still not a great time for a user, a user would be happier to get his output immediatly 
i suggest that they review the code and figure out if there are other less consuming options/datastructures to use
instead of the ones already used 


Functional Testing:

![image](https://user-images.githubusercontent.com/61314172/118402365-eed9bb00-b669-11eb-899a-fa818fe8d17c.png)
![image](https://user-images.githubusercontent.com/61314172/118402371-f4370580-b669-11eb-9214-bd8f467af7b6.png)

i found 2 errors out of the functional testing(1 critical/1 average):
- average:
 
  bubble_sort has 2 functions named the same ( bubble_sort) while 1 is more elegant then the other one 
  so ---> i changed the name of one of them.now we have bubble_sort_elegent & bubble_sort   
  this will make a problem when calling the function from another file the function calling will be confusing.

-critical:

  found a mistake when using circle sorting, the algorithm is not working properly 
  i tested it with an array of pair & impair size and it shows a wrong result in both cases 
  i suggest that they revisit the algorithm and follow the right mathematical approach to fix the issue 
