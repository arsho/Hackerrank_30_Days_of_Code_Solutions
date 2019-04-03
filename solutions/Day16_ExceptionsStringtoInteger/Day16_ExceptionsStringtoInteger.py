'''
  Title     : Day 16: Exceptions - String to Integer
  Domain    : Tutorials
  Author    : Ahmedur Rahman Shovon
  Created   : 03 April 2019
'''
#!/bin/python3

import sys


s = input().strip()
try:
    n = int(s)
    print(n)
except ValueError as value_error:
    print("Bad String")
