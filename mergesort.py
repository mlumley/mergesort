#!/usr/bin/env python3
import random

def topDownMergeSort(ary):
    if len(ary) == 1:
        return ary

    width = len(ary) / 2

    left = topDownMergeSort(ary[:width])
    right = topDownMergeSort(ary[width:])
    
    return merge(left, right)

def merge(left, right):
    b = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            b.append(left[i])
            i += 1
        else:
            b.append(right[j])
            j += 1

    while i < len(left):
        b.append(left[i])
        i += 1
    
    while j < len(right):
        b.append(right[j])
        j += 1

    return b

ranList = [random.randint(-20, 20) for i in range(0, 10)]
print(ranList)
print(topDownMergeSort(ranList))