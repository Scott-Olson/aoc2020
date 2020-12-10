input = open('in02.txt', 'r')

pws = [line.split(' ') for line in input.readlines()]

# clean up lines really slowly
for line in pws:
	temp = line[0]
	temp.split("-")
	line[0] = [int(temp[0]), int(temp[2])]

print(pws[0])