def pre_order(tree):
    pre_order_node(tree.root)
    print()

def pre_order_node(node):
    if node is None:
        return
    print(node.value, end=' ')
    pre_order_node(node.left)
    pre_order_node(node.right)
    
def post_order(tree):
    post_order_node(tree.root)
    print()

def post_order_node(node):
    if node is None:
        return
    post_order_node(node.left)
    post_order_node(node.right)
    print(node.value, end=' ')