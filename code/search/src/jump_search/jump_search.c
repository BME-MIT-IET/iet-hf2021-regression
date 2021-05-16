#include <stdio.h>
#include <math.h>
#define MAX 100

int jumpSearch(int arr[], int size, int element)
{
   int jump_step,prev=0;
   jump_step=floor(sqrt(size));

   /* Finding block in which element lies, if it is present */

   while(arr[prev]<element)
   {
       if(arr[jump_step]>element || jump_step>=size)
       {
            break;
       }
       else
       {
                prev=jump_step;
                jump_step=jump_step+floor(sqrt(size));
       }
   }

   /*Finding the element in the identified block */

   while(arr[prev]<element)
   {
        prev++;
   }

   if(arr[prev]==element)
   {
        return prev+1;
   }
   else
   {
        return -1;
   }

}
