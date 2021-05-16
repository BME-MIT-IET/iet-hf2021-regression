#FUNCTIONAL TESTING PART:

#path has to be changed if you would like to run the test depending on your local location of the files 
sys.path.insert(1, 'E:/Achref/IVT hw/iet-hf2021-regression/code')
#importing sort library
import sorting.src.insertion_sort.insertion_sort as insert
import sorting.src.heap_sort.heap_sort as heap
import sorting.src.merge_sort.merge_sort as merge
import sorting.src.circle_sort.circle_sort as circle
import sorting.src.bubble_sort.bubble_sort as bubble
#importing search library
import search.src.linear_search.linear_search as lin
import search.src.binary_search.binary_search as binr
import search.src.fibonacci_search.fibonacci_search as fib
import search.src.ternary_search.ternary_search as ter
import search.src.jump_search.jump_search as jump
import search.src.interpolation_search.interpolation_search as inter
import search.src.exponential_search.exponential_search as exp

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

insertionlist = [59,48,150,10,0,4,6,99,1547,2456,3145]
mergelist = [59,48,150,10,0,4,6,99,1547,2456,3145]
heaplist = [59,48,150,10,0,4,6,99,1547,2456,3145]
circlelist_impair = [59,48,150,10,0,4,6,99,1547,2456,3145]
circlelist_pair = [59,48,150,10,0,4,6,99,1547,2456]
sorted_result = [0, 4, 6, 10, 48, 59, 99, 150, 1547, 2456, 3145]
bubblelist = [59,48,150,10,0,4,6,99,1547,2456,3145]
find = 99

def test_sortInsertion_searchBinary ():
    testres = insert.insertion_sort(insertionlist)
    print('--testing Insertion sorting--')
    assert testres == sorted_result
    print('--testing Binary Recursive searching--')
    assert binary_search_recursive(testres, find) == 6
    
def test_sortHeap_searchExponential ():
    heap.heap_sort(heaplist)
    print('--testing Heap sorting--\n')
    assert heaplist == sorted_result
    print('--testing Exponential searching--\n')
    assert exponential_search(heaplist, find) == 6 
    
def test_sortMerge_searchJump ():
    testres = merge.merge_sort(mergelist)
    print('--testing Merge sorting--\n')
    assert testres == sorted_result
    print('--testing Jump searching--\n')
    assert jump_search(testres, find) == 6 
    
def test_sortCircle_searchFibonacci_impair ():
    circle.circle_sort(circlelist_impair, 0, len(circlelist_impair) - 1, 0)
    print('--testing Circle sorting--\n')
    assert circlelist_impair == sorted_result
    print('--testing Fibonacci searching--\n')
    assert fibonacci_search(circlelist_impair, find) == 6
    
def test_sortCircle_searchFibonacci_pair ():
    circle.circle_sort(circlelist_pair, 0, len(circlelist_pair) - 1, 0)
    print('--testing Circle sorting--\n')
    assert circlelist_pair == sorted_result
    print('--testing Fibonacci searching--\n')
    assert fibonacci_search(circlelist_pair, find) == 6 
    
def test_sortBubble_searchTernary ():
    testres = bubble.bubble_sort(bubblelist)
    print('--testing Bubble sorting--\n')
    assert testres == sorted_result
    print('--testing Ternary searching--\n')
    assert ternary_search(testres, find) == 6 
