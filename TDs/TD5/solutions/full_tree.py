def is_full(n):

    if isinstance(n, Tree):
        n = n.root

    if n is None or (n.left is None and n.right is None):
        return True
    if n.left is None or n.right is None:
        return False
    return is_full(n.left) and is_full(n.right)