input = open('in01.txt', 'r')
lines = input.readlines()

print(lines[0])
l = len(lines)
seen = {}
for i in range(l):
	diff = 2020 - int(lines[i])
	if diff in seen:
		print("Found 'er ", seen[diff] * diff)
	else:
		seen[diff] = int(lines[i])


for i in range(l):
	diff = 2020 - int(lines[i])
	if int(lines[i]) in seen:
		print(f"Found 'er: {lines[i]}, {diff}", seen[int(lines[i])] * int(lines[i]))

# 1938, 82, 158916