input = open('in03.txt', 'r')
import math

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

# cur_x = 0
# cur_y = 0
# trees = 0

# while cur_y < l:
# 	if clean_loc[cur_y][cur_x] == '#':
# 		trees += 1
# 	cur_x += 3
# 	if line_l <= cur_x:
# 		cur_x = cur_x % line_l
# 	cur_y += 1

# print("# of trees seen: ", trees)
# 207, correct

# part 2

def trav(step_x, step_y):
	cur_x, cur_y, trees = 0, 0, 0
	while cur_y < l:
		if clean_loc[cur_y][cur_x] == '#':
			trees += 1
		cur_x += step_x
		if line_l <= cur_x:
			cur_x = cur_x % line_l
		cur_y += step_y
	return trees

res = [trav(1, 1),trav(3, 1), trav(5, 1), trav(7, 1), trav(1, 2)]
print("1, 1: ", res[0])
print("3, 1: ", res[1])
print("5, 1: ", res[2])
print("7, 1: ", res[3])
print("1, 2: ", res[4])
print(math.prod(res))

# 2655892800 correct answer


