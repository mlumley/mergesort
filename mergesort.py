#!/usr/bin/env python3
import random

def topDownMergeSort(a):
    if len(a) == 1:
        return a

    width = len(a) // 2

    left = topDownMergeSort(a[:width])
    right = topDownMergeSort(a[width:])
    
    return merge(left, right)

def botUpMergeSort(a):
    result = a
    width = 1 
    start = 0
    end = len(result)

    while width < end:
        while start < end:
            left = result[start:start+width]
            right = result[start+width:start+2*width]
            temp = merge(left, right)

            # Copy from temp array to result array
            for i in range(0, len(temp)):
                result[i+start] = temp[i]

            start = start + 2 * width
        width *= 2
        start = 0
    return result

def merge(left, right):
    combined = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            combined.append(left[i])
            i += 1
        else:
            combined.append(right[j])
            j += 1

    # Add any remaining elements if there are any
    while i < len(left):
        combined.append(left[i])
        i += 1
    
    while j < len(right):
        combined.append(right[j])
        j += 1

    return combined

# Test code
ranList = [random.randint(-20, 20) for i in range(0, 10)]
print("Random List")
print(ranList)

print("Sorted List")
print(sorted(ranList))

print("TopDown")
print(topDownMergeSort(ranList))

print("BottomUp")
print(botUpMergeSort(ranList))