#!/bin/python3

import math
import os
import random
import re
import sys


def plusMinus(arr):
    positive = 0
    negative = 0
    zero = 0
    for num in arr:
        if num == 0:
            zero += 1
        elif num < 0:
            negative += 1
        elif num > 0:
            positive += 1
    print(round(positive/n,6)) 
    print(round(negative/n,6)) 
    print(round(zero/n,6))


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
