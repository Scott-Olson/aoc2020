from math import prod 
from itertools import combinations
input = open('in01.txt', 'r')
# lines = input.readlines()
lines = [int(line.strip()) for line in input.readlines()]
print(lines[0])
# part 1
l = len(lines)
# seen = {}
# for i in range(l):
# 	diff = 2020 - int(lines[i])
# 	if diff in seen:
# 		print("Found 'er ", seen[diff] * diff)
# 	else:
# 		seen[diff] = int(lines[i])


# for i in range(l):
# 	diff = 2020 - int(lines[i])
# 	if int(lines[i]) in seen:
# 		print(f"Found 'er: {lines[i]}, {diff}", seen[int(lines[i])] * int(lines[i]))

# 1938, 82, 158916

# part 2
# same as part 1 but with 3 entries rather than 2

# seen = {}
# for i in range(l):
# 	diff = 2020 - lines[i]
# 	seen[diff] = lines[i]

# for i in range(l):
# 	for j in range(i + 1, l):
# 		diff = 2020 - lines[i] - lines[j]
# 		print(diff)
# 		if diff in seen:
# 			s = seen[diff] + lines[i] + lines[j]
# 			if s == 2020:
# 				print(f"Found 'er 3: {lines[i]},{lines[j]},{diff}, {s}", seen[diff] * lines[i] * lines[j])

for c in combinations(lines, 3):
	if sum(c) == 2020:
		print("Found 'er 3: ", prod(c))



