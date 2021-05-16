#include <stdio.h>
/*
 * Part of Cosmos by OpenGenus Foundation
*/
int recursiveBinarySearch(int arr[], int l, int r, int x)
{
   if (r >= l)
   {
        int mid = l + (r - l)/2;
        if (arr[mid] == x)  
            return mid;
         if (arr[mid] > x) 
             return recursiveBinarySearch(arr, l, mid-1, x);
         return recursiveBinarySearch(arr, mid+1, r, x);
   }
   return -1;
}
int binarySearch(int arr[], int l, int r, int x)
{
  while (l <= r)
  {
    int mid = l + (r-l)/2;
    if (arr[mid] == x) 
        return mid;  
    if (arr[mid] < x) 
        l = mid + 1; 
    else
         r = mid - 1; 
  }
   return -1; 
}
