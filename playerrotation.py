class PlayerRotationNode:
    def __init__(self, name):
        self.name = name
        self.next = None

    def __repr__(self):
        return self.data


class PlayerRotation:
    def __init__(self, nodes=None):
        self.head = None
        if nodes is not None:
            node = PlayerRotationNode(data=nodes.pop(0))
            self.head = node
            for elem in nodes:
                node.next = PlayerRotationNode(data=elem)
                node = node.next

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)
