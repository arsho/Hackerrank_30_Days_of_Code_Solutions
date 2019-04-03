'''
  Title     : Day 25: Running Time and Complexity
  Domain    : Tutorials
  Author    : Ahmedur Rahman Shovon
  Created   : 03 April 2019
'''
def is_prime(n):
    if n == 2:
        return True
    if n%2 == 0 or n < 2:
        return False
    max_limit = int(n**0.5) + 1
    for i in range(3, max_limit):
        if n % i == 0:
            return False
    return True

t = int(input())
for k in range(t):
    n = int(input())
    if is_prime(n):
        print("Prime")
    else:
        print("Not prime")
