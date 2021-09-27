class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None

        dic = dict()
        dic[node] = Node(node.val)
        q = [node]

        while q:
            cur = q.pop(0)
            for i in range(len(cur.neighbors)):
                if cur.neighbors[i] not in dic:
                    dic[cur.neighbors[i]] = Node(cur.neighbors[i].val)
                    dic[cur].neighbors.append(dic[cur.neighbors[i]])
                    q.append(cur.neighbors[i])
                else:
                    dic[cur].neighbors.append(dic[cur.neighbors[i]])

        return dic[node]
