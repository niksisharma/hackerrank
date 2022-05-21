#!/bin/python3
#Does not pass one of the test cases

import math
import os
import random
import re
import sys

def binary_search(sequence, value):
    lo, hi = 0, len(sequence) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if sequence[mid] < value:
            lo = mid + 1
        elif value < sequence[mid]:
            hi = mid - 1
        else:
            return mid
    return -1

def icecreamParlor(m, arr):
    result = []
    SortedArr = sorted(arr)

    for i in range(len(arr)):
        complement = m - arr[i]
        complement_index = binary_search(SortedArr, complement)

        if((arr[i] + SortedArr[complement_index]) == m):
            result.append(i+1)
            j = arr.index(SortedArr[complement_index])

            if(arr[i] == SortedArr[complement_index]): j += 1

            result.append(j +1)
            break

    return (result)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        m = int(input().strip())

        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = icecreamParlor(m, arr)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
