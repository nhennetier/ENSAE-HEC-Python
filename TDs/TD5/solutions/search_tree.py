def is_search_tree(tree):
    return is_search_tree_aux(tree.root)[0]

def is_search_tree_aux(node):
    if node is None:
        return True, 100, 0

    is_search_tree_left, min_left, max_left = is_search_tree_aux(node.left)
    if not is_search_tree_left:
        return False, 0, 0
    is_search_tree_right, min_right, max_right = is_search_tree_aux(node.right)

    is_search_tree = is_search_tree_right and max_left <= node.value and min_right > node.value
    return is_search_tree, min(min_left, node.value) , max(node.value, max_right)