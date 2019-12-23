class Node():
	def __init__(self, parent=None, position=None):
		self.parent = parent
		self.position = position

		self.f = 0
		self.g = 0
		self.h = 0 # f = g+h

def check(new_node, close_list):
	for node in close_list:
		if node.position == new_node.position:
			return node
	return None

def a_star(grid, start, end):
	start_node, end_node = Node(None, start), Node(None, end)

	open_list, close_list = [], []

	open_list.append(start_node)

	while open_list:
		curr = open_list[0]
		index = 0

		for idx, node in enumerate(open_list):
			if node.f < curr.f:
				curr = node
				index = idx
		open_list.pop(index)
		close_list.append(curr)

		if curr.position == end_node.position:
			path = []
			while curr:
				path.append(curr.position)
				curr = curr.parent
			return path[::-1]

		# generate child
		children = []
		for i in ([0,1],[1,0],[-1,0],[0,-1],[-1,1],[-1,-1],[1,-1],[1,1]):
			new_pos = [curr.position[0]+i[0], curr.position[1]+i[1]]

			if new_pos[0] < 0 or new_pos[0] >= len(grid) or new_pos[1] < 0 or new_pos[1] >= len(grid[0]):
				continue
			else:
				if grid[new_pos[0]][new_pos[1]] == 1:
					continue
				else:
					new_node = Node(curr, new_pos)
					new_node.g = ((new_node.position[0] - start_node.position[0])**2) + ((new_node.position[1] - start_node.position[1])**2)
					new_node.h = ((new_node.position[0] - end_node.position[0])**2) + ((new_node.position[1] - end_node.position[1])**2)
					new_node.f = new_node.g + new_node.h
					status = check(new_node, close_list)
					if status != None:
						if status.f == new_node.f:
							if status.h > new_node.h:
								status.h = new_node.h
								status.parent = new_node.parent
						elif status.f > new_node.f:
							status.f = new_node.f
							status.parent = new_node.parent
					elif status == None:
						children.append(new_node)

		for child in children:
			flag = 0
			for node in open_list:
				if child.position == node.position:
					flag = 1
					if node.f == child.f:
						if node.h > child.h:
							node.f = child.f
							node.parent = child.parent
					elif node.f > child.f:
						node.f = child.f
						node.parent = child.parent
			if flag == 0:
				open_list.append(child)


def main():
	grid = [[0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0],
			[0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,1,0],
			[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],
			[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
			[0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],
			[0,0,1,0,0,0,1,1,1,1,1,1,0,0,0,0,0,0,0,0],
			[0,0,1,0,0,0,1,1,1,1,1,1,0,0,0,0,0,0,0,0],
			[0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0],
			[0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,1,1,1,1,0],
			[0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,1,1,1,0,0],
			[0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,1,1,0,0],
			[0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,1,0,0,0],
			[0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0],
			[0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0],
			[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],
			[0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0],
			[0,0,0,0,0,0,0,0,1,1,0,0,0,1,1,1,1,0,1,0],
			[0,0,0,0,0,0,0,0,1,1,1,0,0,1,1,1,1,0,0,0],
			[0,0,0,0,0,0,0,1,1,1,0,0,0,1,1,1,1,0,0,0],
			[0,0,0,0,0,0,0,0,1,1,0,0,0,1,1,1,1,1,0,0]]
	start = [0,0]
	end = [15,18]

	path = a_star(grid, start, end)
	print(path)

main()

