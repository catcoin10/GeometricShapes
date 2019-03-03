# Generate a trapezoid

def backrange(y, x): # backwards range
	list = [] # I know we (probably) use a generator, but this will do a "return"
	i = y - 1 # no overflow
	while i >= x: # go in reverse
		list.append(i) # don't enjoy OOP
		i -= 1 # decrement
	return list

def gen_zero_grid(size): # generate a right triangle
	grid = [] # the grid we are generating
	for I in range(size): # use capital for 2D iteration
		line = [] # this is a geometry program, it really should be line SEGMENT
		for i in range(size):
			line.append(" ") # use int, not str
		grid.append(line) # add line before resetting
	return grid

def print_grid(grid): # print the grid
	for I in grid:
		print_str = "" # the string that will be printed
		for i in I:
			print_str += str(i) # increment
		print(print_str) # print when finished

def write_ones(lineseg, ones): # write the ones
	length_of_segment = len(lineseg)
	if ones > length_of_segment or ones <= 0: # if we have a bad number
		return False # do nothing
	else:
		for i in range(ones):
			lineseg[i] = "1"
	return lineseg


def write_ones_2(lineseg, ones): # write the ones
	length_of_segment = len(lineseg)
	if ones > length_of_segment or ones <= 0: # if we have a bad number
		return False # do nothing
	else:
		for i in range(ones):
			x = getinvpos(i, ones)
			lineseg[x] = "1"
	return lineseg


def right_triangle_1(length_of_legs): # generate a right isoceles triangle with 1 90 degree angle and 2 45 degree angle
	trigrid = gen_zero_grid(length_of_legs) # triangle_grid
	for i in range(1, length_of_legs+1):
		grid_segment = trigrid[i-1] # get i-1th grid segment
		trigrid[i-1] = write_ones(grid_segment, i)
	return trigrid


def gen_square(size): # generate a square size long and wide
	grid = [] # the grid we are generating
	for I in range(size): # use capital for 2D iteration
		line = [] # this is a geometry program, it really should be line SEGMENT
		for i in range(size):
			line.append("1") # use int, not str
		grid.append(line) # add line before resetting
	return grid

def invert(size): # invert the right triangle
	data = right_triangle_1(size)
	newdata = []
	for i in backrange(size-1, 0):
		newdata.append(data[i])
	return newdata

size = 8
print_grid(right_triangle_1(size))
print_grid(gen_square(size))
print_grid(invert(size))
