class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        dic = dict()
        return self.dfs(head, dic)

    def dfs(self, head: 'Node', dic: dict) -> 'Node':
        if not head:
            return None

        if head not in dic:
            new_node = Node(head.val)
            dic[head] = new_node
            new_node.next = self.dfs(head.next, dic)
            new_node.random = self.dfs(head.random, dic)

        return dic[head]
