'''
  Title     : Day 5: Loops
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
    for i in range(1, 11):
        print("{} x {} = {}".format(n, i, n*i))
