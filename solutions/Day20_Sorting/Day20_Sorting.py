'''
  Title     : Day 20: Sorting
  Domain    : Tutorials
  Author    : Ahmedur Rahman Shovon
  Created   : 03 April 2019
'''
#!/bin/python3

import sys

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
# Write Your Code Here
total_swap = 0
for i in range(len(a) - 1):
    swap = 0
    for j in range(i+1, len(a)):
        if a[i] > a[j]:
            temp = a[i]
            a[i] = a[j]
            a[j] = temp
            swap += 1
    total_swap += swap
print("Array is sorted in {} swaps.".format(total_swap))
print("First Element: {}".format(a[0]))
print("Last Element: {}".format(a[len(a) - 1]))
