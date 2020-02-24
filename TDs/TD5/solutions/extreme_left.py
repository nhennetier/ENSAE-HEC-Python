def extreme_left(tree):
    node = tree.root

    if node is None:
        return

    while node.left is not None:
        node = node.left
    return node.value