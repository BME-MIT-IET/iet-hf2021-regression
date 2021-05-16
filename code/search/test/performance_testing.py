import sys

import timeit

#path has to be changed if you would like to run the test depending on your local location of the files 
sys.path.insert(1, 'E:/Achref/IVT hw/iet-hf2021-regression/code')

#import the search library
import search.src.linear_search.linear_search as lin
import search.src.binary_search.binary_search as binr
import search.src.fibonacci_search.fibonacci_search as fib
import search.src.ternary_search.ternary_search as ter
import search.src.jump_search.jump_search as jump
import search.src.interpolation_search.interpolation_search as inter
import search.src.exponential_search.exponential_search as exp

#prepare the searching functions to be used later 
def linear_search(mylist, find):
    return lin.linear_search(mylist,find)

def binary_search_recursive(mylist, find):
    return binr.binary_search_recursive(mylist,find)

def exponential_search(mylist, find):
    return exp.exponential_search(mylist, find)

def fibonacci_search(mylist, find):
    return fib.fibonacci_search(mylist, find)

def interpolation_search(mylist, find):
    return inter.interpolation_search(mylist, find)

def jump_search(mylist, find):
    return jump.jump_search(mylist, find)

def ternary_search(mylist, find):
    return ter.ternary_search(mylist, find)


#PERFORMANCE TESTING PART 

# compute binary search time
def binary_time():
    SETUP_CODE = '''
from __main__ import binary_search_recursive
from random import randint'''
  
    TEST_CODE = '''
mylist = [x for x in range(10000)]
find = randint(0, len(mylist))
binary_search_recursive(mylist, find)'''
      
    # timeit.repeat statement : return a list of execution time because we are repeating the process 3 times
    times = timeit.repeat(setup = SETUP_CODE,
                          stmt = TEST_CODE,
                          repeat = 3,
                          number = 10000)
  
    # priniting minimum exec. time out of the list 
    print('Binary search recursive time: {}'.format(min(times)))        
  
  
# compute linear search time
def linear_time():
    SETUP_CODE = '''
from __main__ import linear_search
from random import randint'''
      
    TEST_CODE = '''
mylist = [x for x in range(10000)]
find = randint(0, len(mylist))
linear_search(mylist, find)
    '''
    # timeit.repeat statement : return a list of execution time because we are repeating the process 3 times
    times = timeit.repeat(setup = SETUP_CODE,
                          stmt = TEST_CODE,
                          repeat = 3,
                          number = 10000)
  
    # priniting minimum exec. time out of the list 
    print('Linear search time: {}'.format(min(times)))  
    
# compute exponential search time
def exponential_time():
    SETUP_CODE = '''
from __main__ import exponential_search
from random import randint'''
      
    TEST_CODE = '''
mylist = [x for x in range(10000)]
find = randint(0, len(mylist))
exponential_search(mylist, find)
    '''
    # timeit.repeat statement : return a list of execution time because we are repeating the process 3 times
    times = timeit.repeat(setup = SETUP_CODE,
                          stmt = TEST_CODE,
                          repeat = 3,
                          number = 10000)
  
    # priniting minimum exec. time out of the list 
    print('Exponential search time: {}'.format(min(times))) 
    
# compute jump search time
def jump_time():
    SETUP_CODE = '''
from __main__ import jump_search
from random import randint'''
      
    TEST_CODE = '''
mylist = [x for x in range(10000)]
find = randint(0, len(mylist))
jump_search(mylist, find)
    '''
    # timeit.repeat statement : return a list of execution time because we are repeating the process 3 times
    times = timeit.repeat(setup = SETUP_CODE,
                          stmt = TEST_CODE,
                          repeat = 3,
                          number = 10000)
  
    # priniting minimum exec. time out of the list 
    print('Jump search time: {}'.format(min(times))) 
    
# compute fibonacci search time
def fibonacci_time():
    SETUP_CODE = '''
from __main__ import fibonacci_search
from random import randint'''
      
    TEST_CODE = '''
mylist = [x for x in range(10000)]
find = randint(0, len(mylist))
fibonacci_search(mylist, find)
    '''
    # timeit.repeat statement : return a list of execution time because we are repeating the process 3 times
    times = timeit.repeat(setup = SETUP_CODE,
                          stmt = TEST_CODE,
                          repeat = 3,
                          number = 10000)
  
    # priniting minimum exec. time out of the list 
    print('Fibonacci search time: {}'.format(min(times))) 
    
# compute ternary search time
def ternary_time():
    SETUP_CODE = '''
from __main__ import ternary_search
from random import randint'''
      
    TEST_CODE = '''
mylist = [x for x in range(10000)]
find = randint(0, len(mylist))
ternary_search(mylist, find)
    '''
    # timeit.repeat statement : return a list of execution time because we are repeating the process 3 times
    times = timeit.repeat(setup = SETUP_CODE,
                          stmt = TEST_CODE,
                          repeat = 3,
                          number = 10000)
  
    # priniting minimum exec. time out of the list 
    print('Ternary search time: {}'.format(min(times))) 
    
# compute interpolation search time
def interpolation_time():
    SETUP_CODE = '''
from __main__ import interpolation_search
from random import randint'''
      
    TEST_CODE = '''
mylist = [x for x in range(10000)]
find = randint(0, len(mylist))
interpolation_search(mylist, find)
    '''
    # timeit.repeat statement : return a list of execution time because we are repeating the process 3 times
    times = timeit.repeat(setup = SETUP_CODE,
                          stmt = TEST_CODE,
                          repeat = 3,
                          number = 10000)
  
    # priniting minimum exec. time out of the list 
    print('Interpolation search time: {}'.format(min(times))) 




if __name__ == '__main__':
    linear_time()
    binary_time()
    exponential_time()
    fibonacci_time()
    jump_time()
    interpolation_time()
    ternary_time()
