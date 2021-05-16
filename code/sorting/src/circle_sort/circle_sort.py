# Python program to implement circle sort
# Part of Cosmos by OpenGenus Foundation
# function to swap 2 elements of a list
def swap(a, i, j):
    temp = a[i]
    a[i] = a[j]
    a[j] = temp


# recursive function to perfrom circle sort on the given list
def circle_sort(a, lower, upper, swaps):
    # base case
    if lower == upper:
        return swaps

    low = lower
    high = upper
    mid = int((upper - lower) / 2)

    while lower < upper:
        if a[lower] > a[upper]:
            swap(a, lower, upper)
            swaps += 1
            print(a, swaps)

        lower += 1
        upper -= 1

    if lower == upper:
        if a[lower] > a[upper + 1]:
            swap(a, lower, upper + 1)
            swaps += 1
            print(a, swaps)

    circle_sort(a, low, low + mid, swaps)
    circle_sort(a, low + mid + 1, high, swaps)

    return swaps


