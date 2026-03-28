# import sys
# sys.setrecursionlimit(10000)
# import pprint as pp
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
	n = int(input())
	for i in range(n):
		bridges.append(list(map(str, input().split())))

cfdref = {}
visited = set()
stack = []


def find_child(node, graph):
	# for i in graph:
	global visited
	if node in visited:
		return
	
	visited.add(node)
	print(node)
	for i in sorted(list(graph[node])):
		find_child(i, graph)
	





for i in bridges:
	cfdref[i[0]] = set()
	cfdref[i[1]] = set()
for i in bridges:
	cfdref[i[0]].add(i[1])

find_child("A", cfdref)

























