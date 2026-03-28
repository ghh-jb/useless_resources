DBG_BUILD = 0
def debug(*args, **kwargs):
	if (DBG_BUILD): print(*args, **kwargs)

n = 0
m = []

if (DBG_BUILD):
	n = 5
	m = [[0, 0, 1, 0, 0], [0, 0, 1, 0, 1], [1, 1, 0, 0, 0], [0, 0, 0, 0, 0], [0, 1, 0, 0, 0]]
else:
	n = int(input())
	for i in range(n):
		m.append(list(map(int, input().split())))

debug(m, sep = "\n")
visited = set()


for i in range(len(m)):
	for j in range(len(m[i])):
		if m[i][j] == 1: # edge is present
			if ((i+1, j+1) in visited or (j+1, i+1) in visited): # comment one of the checks to make it directed
				continue
			visited.add((i+1, j+1))
			print(i+1, j+1)
