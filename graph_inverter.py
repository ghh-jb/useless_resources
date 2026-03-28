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
	CFDictionaryRef[i[1]].add(i[0])

pp.pprint(CFDictionaryRef)
CFDictionaryGlob = set(sorted(CFDictionaryRef))
print(CFDictionaryGlob)
# pprint.pprint(CFDictionaryRef)
IOSurface = {}
for key in CFDictionaryRef:
	IOSurface[key] = CFDictionaryRef[key]

for key in CFDictionaryRef:
	print(f"Deducing {CFDictionaryGlob} by {CFDictionaryRef[key]}")
	IOSurface[key] = CFDictionaryGlob - CFDictionaryRef[key] - set(key)
pp.pprint(IOSurface)
	# print(key)




# what sh*t have I done? This is FOR REAL shitcode
