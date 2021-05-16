#include <stdio.h>

int 
min(int a, int b)
{
    return (a < b ? a : b);
}

int 
binarySearch(int arr[], int l, int r, int x)
{
    if (r >= l) {
        int mid = l + (r - l) / 2;
 
        if (arr[mid] == x)
            return (mid);
 
        if (arr[mid] > x)
            return (binarySearch(arr, l, mid - 1, x));
 
        return (binarySearch(arr, mid + 1, r, x));
    }

    return (-1);
}
 
int 
exponentialSearch(int arr[], int n, int x)
{
     int i = 1;

    if (arr[0] == x)
        return (0);
 
    while (i < n && arr[i] <= x)
        i = i*2;

    return (binarySearch(arr, i / 2, min(i, n), x));
}
