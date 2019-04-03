'''
  Title     : Day 2: Operators
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

# Complete the solve function below.
def solve(meal_cost, tip_percent, tax_percent):
    tip = meal_cost * (tip_percent / 100)
    tax = meal_cost * (tax_percent / 100)
    return round(meal_cost + tip + tax)

if __name__ == '__main__':
    meal_cost = float(input())
    tip_percent = int(input())
    tax_percent = int(input())
    total_cost = solve(meal_cost, tip_percent, tax_percent)
    print(total_cost)
