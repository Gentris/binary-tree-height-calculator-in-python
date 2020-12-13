class Node:
	def __init__(self, data, left_node=None, right_node=None):
		self.data = data
		self.left_node = left_node
		self.right_node = right_node


def get_node_height(node: Node):
	if (node is None):
		return -1

	return max(get_node_height(node.left_node), get_node_height(node.right_node)) + 1
