'''
  Title     : Day 6: Let's Review
  Domain    : Tutorials
  Author    : Ahmedur Rahman Shovon
  Created   : 03 April 2019
'''
# Enter your code here. Read input from STDIN. Print output to STDOUT
t = int(input())
for k in range(t):
    s = input()
    odd = ""
    even = ""
    for i in range(len(s)):
        if i%2 == 0:
            even += s[i]
        else:
            odd += s[i]
    print("{} {}".format(even, odd))
