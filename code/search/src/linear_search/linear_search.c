#include <stdio.h>
/*
 * Part of Cosmos by OpenGenus Foundation
*/

/*
 * Input: an integer array with size in index 0, the element to be searched
 * Output: if found, returns the index of the element else -1
*/
int linearSearch(int arr[], int size, int element)
{
	int i=0;
	for (i=0; i<size; i++)
		if (arr[i] == element)
		    return i;
	return -1;
}
