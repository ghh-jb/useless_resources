cnt = 0; start = 3; end = 13; block = 9
def preprocess(i, path):
	global cnt; global end
	if (i == end and block not in path):
		cnt += 1
	if (i >= end): return
	i1 = i+1; i2 = i+2;
	preprocess(i1, path + [i1])
	preprocess(i2, path + [i2])
preprocess(start, [start])
print(cnt)
