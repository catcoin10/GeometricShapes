def gen_zero_grid(size): # generate a right triangle
	grid = [] # the grid we are generating
	for I in range(size): # use capital for 2D iteration
		line = [] # this is a geometry program, it really should be line SEGMENT
		for i in range(size):
			line.append(0) # use int, not str
		grid.append(line) # add line before resetting
	return grid

def print_grid(grid): # print the grid
	for I in grid:
		print_str = "" # the string that will be printed
		for i in I:
			print_str += str(i) # increment
		print(print_str) # print when finished
