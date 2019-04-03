'''
  Title     : Day 10: Binary Numbers
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
    n = int(input())
    b = str(bin(n))[2:]
    l = len(b)
    max_1 = 0
    i = 0
    while i < l:
        count = 0
        while i < l and b[i] == "1":
            count += 1
            i += 1
        i += 1
        max_1 = max(count, max_1)
    print(max_1)
