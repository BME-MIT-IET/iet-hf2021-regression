#include "CppUTest/TestHarness.h"
#include "binary_search.c"
#include "fibonacci_search.c"
#include "interpolation_search.c"
#include "linear_search.c"
#include "jump_search.c"
#include "ternary_search.c"


TEST_GROUP(SEARCH_TESTS)
{
	void setup() {
	}

	void teardown() {
	}
};

TEST(SEARCH_TESTS, binary_search)
{
   int arr[] = {1, 2, 3, 5, 9, 6};
   int size = sizeof(arr)/ sizeof(arr[0]);
   int find = 3;

   CHECK_EQUAL(2 ,recursiveBinarySearch(arr, 0, size-1, find));
   CHECK_EQUAL(2 ,binarySearch(arr, 0, size-1, find));

   CHECK_EQUAL(3, fibSearch(arr, size-1 ,find));
   

   int array[10] = {1, 5, 9, 12, 16, 18, 25, 56, 76, 78};
   size = sizeof(array)/sizeof(array[0]);
   int key = 25;

   CHECK_EQUAL(6, interpolationSearch(array, size, key));

   CHECK_EQUAL(7, jumpSearch(array, size, key));
   CHECK_EQUAL(6, linearSearch(array,size, key));

   int ary[] = {1, 2, 3, 5, 8, 10};
   size = sizeof(ary)/ sizeof(ary[0]);
   find = 5;

   CHECK_EQUAL(3, ternarySearch(ary, 0, size-1 ,find));
}
