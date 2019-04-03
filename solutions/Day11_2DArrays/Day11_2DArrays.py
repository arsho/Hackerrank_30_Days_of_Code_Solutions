'''
  Title     : Day 11: 2D Arrays
  Domain    : Tutorials
  Author    : Ahmedur Rahman Shovon
  Created   : 03 April 2019
'''
#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
    max_sum = -999999999999
    for i in range(4):
        for j in range(4):
            first_row = arr[i]
            third_row = arr[i+2]
            first_row_sum = sum(first_row[j:j+3])
            middle_element = arr[i+1][j+1]
            third_row_sum = sum(third_row[j:j+3])
            hour_glass_sum = first_row_sum + middle_element + third_row_sum
            max_sum = max(max_sum, hour_glass_sum)
    print(max_sum)
