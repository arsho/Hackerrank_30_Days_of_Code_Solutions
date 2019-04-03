'''
  Title     : Day 14: Scope
  Domain    : Tutorials
  Author    : Ahmedur Rahman Shovon
  Created   : 03 April 2019
'''
class Difference:
    def __init__(self, a):
        self.__elements = a

	# Add your code here
    def __init__(self, elements):
        self.elements = elements

    def computeDifference(self):
        self.maximumDifference = -1
        for i in range(len(self.elements) - 1):
            for j in range(i+1, len(self.elements)):
                difference = abs(self.elements[i] - self.elements[j])
                self.maximumDifference = max(self.maximumDifference, difference)

# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)
