class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    def serialize(self, root):
        if not root:
            return ""

        s = str(root.val) + "/"
        q = [root]
        while q:
            node = q.pop(0)
            if node.left:
                s += str(node.left.val) + "/"
                q.append(node.left)
            else:
                s += "#/"

            if node.right:
                s += str(node.right.val) + "/"
                q.append(node.right)
            else:
                s += "#/"

        return s

    def deserialize(self, data):
        if len(data) == 0:
            return None

        i = data.find('/')
        root = TreeNode(int(data[0:i]))
        data = data[i + 1:]
        q = [root]
        while q:
            if i == len(data):
                break

            node = q.pop(0)
            i = data.find('/')
            if data[0] != "#":
                node.left = TreeNode(int(data[0:i]))
                q.append(node.left)

            data = data[i + 1:]
            i = data.find('/')
            if data[0] != "#":
                node.right = TreeNode(int(data[0:i]))
                q.append(node.right)

            data = data[i + 1:]
        return root
