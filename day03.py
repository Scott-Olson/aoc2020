input = open('in03.txt', 'r')

loc = input.readlines()
clean_loc = []
for line in loc:
	clean_loc.append(line.strip())
l = len(clean_loc)
line_l = len(clean_loc[0])

print(l, line_l)
print(clean_loc[0])
print(f"len: {line_l} 0: {clean_loc[0][0]} len: {clean_loc[0][line_l - 1]}")
cur = clean_loc[0]

cur_x = 0
cur_y = 0
trees = 0

while cur_y < l:
	# print(f"x:{cur_x}, y:{cur_y}, l:{line_l}")
	if clean_loc[cur_y][cur_x] == '#':
		trees += 1
	cur_x += 3
	# print(f"after add x:{cur_x}, y:{cur_y}, l:{line_l}")
	if line_l <= cur_x:
		# print("Before mod: ", cur_x)
		cur_x = cur_x % line_l
		# print("After mod: ", cur_x)
	cur_y += 1
	# print(trees)

print("# of trees seen: ", trees)
# 207, correct

# part 2