'''
  Title     : Day 8: Dictionaries and Maps
  Domain    : Tutorials
  Author    : Ahmedur Rahman Shovon
  Created   : 03 April 2019
'''
# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys


t = int(input())
d = {}
for k in range(t):
    person, value = input().split(" ")
    d[person] = value


for line in sys.stdin:
    person = line.strip()
    if person not in d:
        print("Not found")
    else:
        print("{}={}".format(person, d[person]))
