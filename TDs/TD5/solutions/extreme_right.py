def extreme_right(tree):
    node = tree.root

    if node is None:
        return

    return extreme_right_aux(node)

def extreme_right_aux(node):
    if node.right is None:
        return node.value
    return extreme_right_aux(node.right)