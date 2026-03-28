DBG_BUILD = 0
def debug(*args, **kwargs):
	if (DBG_BUILD): print(*args, **kwargs)

n = 0
matrix = []
bridges = []

if (DBG_BUILD):
	n = 5
	# m = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
	# bridges = [[5, 3], [1, 3], [2, 3], [2, 5]]
else:
	n, m = map(int, input().split())
	for i in range(m):
		bridges.append(list(map(int, input().split())))
	for i in range(n):
		matrix.append([0]*n)


def parse_bridges(localbridges):
	a = []
	for i in localbridges:
		i[0] -= 1
		i[1] -= 1
		a.append([i[1], i[0]])
	# for i in a:
	# 	localbridges.append(i) # uncommenting this will make it undirected
	return localbridges

bridges = parse_bridges(bridges)
debug(m, bridges)

for i in range(n):
	for j in range(n):
		if [i, j] in bridges:
			matrix[i][j] = 1
			# m[j+1][i+1] = 1
for i in matrix:
	print(*i)
