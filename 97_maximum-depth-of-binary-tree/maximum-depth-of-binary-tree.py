# coding:utf-8
'''
@Copyright:LintCode
@Author:   cong11
@Problem:  http://www.lintcode.com/problem/maximum-depth-of-binary-tree
@Language: Python
@Datetime: 16-11-02 02:49
'''

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
#recursion
class Solution:
    """
    @param root: The root of binary tree.
    @return: An integer
    """ 
    def maxDepth(self, root):
        # write your code here
        if root is None:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1