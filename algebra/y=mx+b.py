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

def write_one(grid, x, y): # write a one to the graph
    grid[x][y] = 1 # write a one
    return grid

def y_equals_mx_plus_0(size, m): # generate an image with a slope of -1 (the name is base32 for y=mx+0
        grid = gen_zero_grid(size) # get the grid and save the data
        for i in range(0, int(size/2)): # I hate python3 having generators and no "print 'Hi's"
                grid = write_one(grid, i*m, i)
        return grid

print_grid(y_equals_mx_plus_0(10, 2))
