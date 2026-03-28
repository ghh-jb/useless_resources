import pprint as pp
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

CFDictionaryRef = {}
for i in bridges:
	CFDictionaryRef[i[0]] = set()
	CFDictionaryRef[i[1]] = set()
for i in bridges:
	CFDictionaryRef[i[0]].add(i[1])
	# CFDictionaryRef[i[1]].add(i[0]) # it is now not directed


CFDictionaryLst = sorted(CFDictionaryRef)
# pprint.pprint(CFDictionaryRef)
IOSurface = {}

for i in  CFDictionaryLst:
	IOSurface[i] = [0,0]

for i in CFDictionaryRef:
	out = CFDictionaryRef[i]
	for node in out:
		IOSurface[node][0] += 1
	IOSurface[i][1] += len(out)
pp.pprint(CFDictionaryRef)
pp.pprint(IOSurface)

for i in IOSurface:
	print(i, IOSurface[i][0], IOSurface[i][1])



'''
8
A B
B C
B D
B E
C E
D E
E F
G D
'''

# whatever this it...

'''correct output:
A 0 1
B 1 3
C 1 1
D 2 1
E 3 1
F 1 0
G 0 1
'''
