'''
  Title     : Day 28: RegEx, Patterns, and Intro to Databases
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
    N = int(input())
    names = []
    for N_itr in range(N):
        firstNameEmailID = input().split()

        firstName = firstNameEmailID[0]

        emailID = firstNameEmailID[1]
        if emailID.endswith("@gmail.com"):
            names.append(firstName)
    names = sorted(names)
    for name in names:
        print(name)
