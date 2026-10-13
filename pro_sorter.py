def zap(s):
	i,t,sp = s.split()
	return int(i), int(t), set(map(int, sp.split(";")))
df = [zap(s) for s in open("file")]
z = {0:(0,0)}
while len(z) <= len(df):
	sz = set(z)
	for i,t,sp in df:
		if i in z: continue
		if sp<=sz:
			ts=max([z[p][0] for p in sp])
			z[i] = (ts + t, ts)
z.pop(0)
print(sorted([(z[i], i) for i in z]))
