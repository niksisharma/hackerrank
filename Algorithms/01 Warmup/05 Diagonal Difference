#!/bin/python3

import math
import os
import random
import re
import sys

def diagonalDifference(arr):
    leftsum = 0
    rightsum = 0
    for i in range(n):
            leftsum += arr[i][i]
            rightsum += arr[i][n-1-i]
    return abs(leftsum-rightsum)
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
