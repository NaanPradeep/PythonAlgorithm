class Node:
	def __init__(self, data):
		self.data = data
		self.next = None


class LinkedList:
	insertion_error = TypeError("Insertion not possible, Previous node does not exists.")
	node_error = TypeError("Node doest not exists")
	
	def __init__(self):
		self.head = None


	def print_list(self):
		cur_node = self.head

		while cur_node:
			print(cur_node.data)
			cur_node = cur_node.next


	def append(self, data):
		new_node = Node(data)

		if not self.head:
			self.head= new_node
			return

		last_node = self.head
		while last_node.next:
			last_node = last_node.next
		last_node.next = new_node


	def prepend(self, data):
		new_node = Node(data)

		new_node.next = self.head
		self.head = new_node


	def insert_btwn_nodes(self, previous_node, data):
		new_node = Node(data)
		prev_node = self.head

		while prev_node and prev_node.data == previous_node:
			new_node.next = prev_node.next
			prev_node.next = new_node

		while prev_node and prev_node.data != previous_node:
			prev_node = prev_node.next

		if not prev_node:
			raise self.insertion_error

		new_node.next = prev_node.next
		prev_node.next = new_node


	def delete(self, key):
		cur_node = self.head

		if cur_node and cur_node.data == key:
			self.head = cur_node.next
			cur_node = None
			return

		prev_node = None
		while cur_node and cur_node.data != key:
			prev_node = cur_node
			cur_node = cur_node.next


		if cur_node is None:
			return

		prev_node.next = cur_node.next
		cur_node = None


	def list_length_iterative(self):

		node = self.head
		length = 0

		while node:
			node = node.next
			length += 1

		return length


	def list_length_recursive(self, node):

		if not node:
			return 0

		list_length = self.list_length_recursive(node.next)
		print(list_length)

		return 1 + list_length


	def node_swap(self, node_1, node_2):
		previous_node_1 = None
		first_node = self.head
		
		while first_node and first_node.data != node_1:
			previous_node_1 = first_node
			first_node = first_node.next

		previous_node_2 = None
		second_node = self.head

		while second_node and second_node.data != node_2:
			previous_node_2 = second_node
			second_node = second_node.next

		if not first_node or not second_node:
			raise self.swap_error

		if previous_node_1:
			previous_node_1.next = second_node
		else:
			self.head = second_node

		if previous_node_2:
			previous_node_2.next = first_node
		else:
			self.head = first_node

		first_node.next, second_node.next = second_node.next, first_node.next	


	def node_swap_by_index(self, node_1, node_2):

		prev_node_1 = None
		first_node = self.head

		for i in range(0, node_1):
			if not first_node:
				break
			prev_node_1 = first_node
			first_node = first_node.next

		prev_node_2 = None
		second_node = self.head

		for i in range(0, node_2):
			if not second_node:
				break
			prev_node_2 = second_node
			second_node = second_node.next

		if not first_node or not second_node:
			raise self.swap_error
		
		if prev_node_1:
			prev_node_1.next = second_node
		else:
			self.head = second_node

		if prev_node_2:
			prev_node_2.next = first_node
		else:
			self.head = first_node

		first_node.next, second_node.next = second_node.next, first_node.next

	def reverse_iterative(self):
		prev_node = None
		cur_node  = self.head

		while cur_node:
			nxt = cur_node.next
			cur_node.next = prev_node
			prev_node = cur_node
			cur_node = nxt

		self.head = prev_node

	def reverse_recursive(self):	

		def _reverse_recursive(prev_node, cur_node):

			if not cur_node:
				return prev_node

			nxt = cur_node.next
			cur_node.next = prev_node
			prev_node = cur_node
			cur_node = nxt
			return _reverse_recursive(prev_node, cur_node)

		self.head = _reverse_recursive(prev_node=None, cur_node=self.head)


	def merge_sorted(self, lst):

		p_node = self.head
		q_node = lst.head
		s_node  = None

		if not p_node:
			return q_node

		if not q_node:
			return p_node

		if p_node and q_node:
			if p_node.data <= q_node.data:
				s_node = p_node
				p_node = s_node.next

			else:
				s_node = q_node
				q_node = s_node.next

			new_head = s_node

		while p_node and q_node:
			if p_node.data <= q_node.data:
				s_node.next = p_node
				s_node = p_node
				p_node = s_node.next

			else:
				s_node.next = q_node
				s_node = q_node
				q_node = s_node.next

		if not p_node:
			s_node.next = q_node

		if not q_node:
			s_node.next = p_node

		return new_head

	def remove_duplicates(self):

		prev_node = None
		cur_node = self.head
		dup_list = []

		while cur_node:
			if cur_node.data in dup_list:
				prev_node.next = cur_node.next
				cur_node = None

			else:
				dup_list.append(cur_node.data)
				prev_node = cur_node

			cur_node = prev_node.next


	def nth_to_the_last_node(self, index):
		total_list_length = self.list_length()
		nth_index = total_list_length - index

		cur_node = self.head

		if nth_index == 0:
			return self.head.data

		if nth_index < 0:
			return

		for i in range(nth_index):
			cur_node = cur_node.next

		return cur_node.data


	def count_occurrences(self):

		cur_node = self.head
		node_frequency_list = {}

		if not cur_node:
			return

		while cur_node:
			if cur_node.data not in node_frequency_list:
				node_frequency_list[cur_node.data] = 1

			elif cur_node.data in node_frequency_list:
				node_frequency_list[cur_node.data] += 1

			cur_node = cur_node.next

		return node_frequency_list


	def rotate_lists(self, pivot):
		first_head = self.head
		cur_node = self.head

		while cur_node and cur_node.data != pivot:
			cur_node = cur_node.next

		if not cur_node:
			raise self.node_error

		self.head = cur_node.next
		cur_node.next = None

		prev_node = cur_node.next
		cur_node = self.head

		while cur_node:
			prev_node = cur_node
			cur_node = cur_node.next

		prev_node.next = first_head


	def is_polindrome(self):

		cur_node = self.head
		s = ""

		while cur_node:
			s += str(cur_node)
			cur_node = cur_node.next

		return s == s[::-1]


	def mov_tail_to_head(self):

		prev_node = None
		first_head = self.head

		cur_node = self.head

		length = self.	list_length()

		for i in range(length - 1):
			prev_node = cur_node
			cur_node = cur_node.next

		self.head = cur_node
		cur_node.next = first_head
		prev_node.next = None






lst1 = LinkedList()

lst1.append(1)
lst1.append(4)
lst1.append(1)
lst1.append(5)
lst1.append(6)
lst1.append(4)



print(lst1.list_length_recursive(lst1.head))
