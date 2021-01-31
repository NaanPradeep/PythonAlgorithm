class Node:

	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None



class BinarySearchTree:

	def __init__(self):
		self.root = None


	def insert_node(self, data):

		if not self.root:
			self.root = Node(data)

		else:
			self._insert_node(data, self.root)


	def _insert_node(self, data, parent_node)

		if data > parent_node.value:
			if parent_node.right:
				insert_node(parent_node.right, data)

			else:
				parent_node.right = Node(data)
				parent_node.left.parent =  parent_node


		elif data < parent_node.value:
			if parent_node.left:
				insert_node(parent_node.left, data)

			else:
				parent_node.left = Node(data)
				parent_node.left.parent =  parent_node


		else:
			print("Node already exists")
