input = open('in02.txt', 'r')

pws = [line.split(' ') for line in input.readlines()]

# part 1 - clean up lines and process them
l = len(pws)
count = 0
print(pws[0])
pws[l - 1][2] = pws[l - 1][2] + "\n"
print(pws[l - 1])
print("Total: ", l)
# for line in pws:
# 	line[1] = line[1][0]
# 	line[0] = [int(i) for i in line[0].split('-')]
# 	line[2] = line[2][:-1]
# 	c_count = line[2].count(line[1])
# 	mini, maxi = line[0][0], line[0][1]
# 	print(f"Count: {c_count}  Min: {mini}  Max: {maxi}")
# 	if mini <= c_count <= maxi:
# 		print("Valid pw detected")
# 		count += 1

# print("Valid pws: ", count)
# 378 correct

# part 2 

print(f"Count before p2: {count}")
for line in pws:
	line[1] = line[1][0]
	line[0] = [int(i) for i in line[0].split('-')]
	line[2] = line[2][:-1]
	char = line[1]
	c_count = line[2].count(line[1])
	f, s = line[0][0] - 1, line[0][1] - 1

	# assign the chars to boolean vars
	p1, p2 = line[2][f] == char, line[2][s] == char
	# xor boolean vars
	if p1 != p2:
		print(f"str: {line[2]} idx1: {line[2][f]} == {char}?  idx2: {line[2][s]} == {char}?")
		count += 1

print(f"Count after: {count}")

# correct answer 280

