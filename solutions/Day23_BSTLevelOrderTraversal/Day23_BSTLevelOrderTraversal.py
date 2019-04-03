'''
  Title     : Day 23: BST Level-Order Traversal
  Domain    : Tutorials
  Author    : Ahmedur Rahman Shovon
  Created   : 03 April 2019
'''
import sys

class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data
class Solution:
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root

    def levelOrder(self,root):
        #Write your code here
        nodes = []
        queue = [root]
        while queue:
            top = queue.pop(0)
            nodes.append(top.data)
            if top.left:
                queue.append(top.left)
            if top.right:
                queue.append(top.right)
        print(" ".join(map(str, nodes)))

T=int(input())
myTree=Solution()
root=None
for i in range(T):
    data=int(input())
    root=myTree.insert(root,data)
myTree.levelOrder(root)
