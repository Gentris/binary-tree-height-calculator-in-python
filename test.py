from tree import Node, get_node_height

node_1 = Node(1)
node_2 = Node(2)
node_3 = Node(3)
node_4 = Node(4)
node_5 = Node(5, node_1, node_2) 
node_6 = Node(6, node_3, node_4)
root_node = Node(7, node_5, node_6)

print(get_node_height(root_node))
