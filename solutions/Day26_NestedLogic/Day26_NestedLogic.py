'''
  Title     : Day 26: Nested Logic
  Domain    : Tutorials
  Author    : Ahmedur Rahman Shovon
  Created   : 03 April 2019
'''
import datetime


returned = list(map(int, input().split()))
expected = list(map(int, input().split()))
returned_date = datetime.date(returned[2], returned[1], returned[0])
expected_date = datetime.date(expected[2], expected[1], expected[0])
difference = returned_date - expected_date


days_difference = difference.days
if days_difference <= 0:
    print(0)
else:
    if returned[2] != expected[2]:
        print(10000)
    else:
        if returned[1] != expected[1]:
            print((returned[1] - expected[1]) * 500)
        else:
            print((returned[0] - expected[0]) * 15)
