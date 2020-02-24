def is_perfect(tree):
    return is_perfect_aux(tree.root)[0]

def is_perfect_aux(node):

    if node is None or (node.left is None and node.right is None):
        return True, 0
    if node.left is None or node.right is None:
        return False, 0

    perfect_left, depth_left = is_perfect_aux(node.left)
    if not perfect_left:
        return False, 0
    perfect_right, depth_right = is_perfect_aux(node.right)

    return perfect_right and depth_left == depth_right, depth_left + 1