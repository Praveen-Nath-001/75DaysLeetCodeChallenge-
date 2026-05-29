"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        copy_map = {}
        return recursive(node, copy_map)



def recursive(cur_node, copy_map):
    if cur_node in copy_map:
        return copy_map[cur_node]

    copied = Node(cur_node.val)
    copy_map[cur_node] = copied

    for n in cur_node.neighbors: 
        copied.neighbors.append(recursive(n, copy_map))
    
    return copied
