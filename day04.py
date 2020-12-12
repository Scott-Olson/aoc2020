input = open('in04.txt', 'r').split()
ids = [line.split(' ') for line in input.readlines()]
print(len(ids))
print(ids[0])
print(ids[1])