ee = [1581,1584]
L, W = set([ee[0]]), set([ee[1]])
G = set([(i,k) for i in range(1, ee[0]) for k in range(5)])
St =set([(i,0) for i in range(1, ee[0]) ])
def pi(pos) :
    p, k = pos
    a = [(p+4,1), (p+5,2), (p*2,3), (p*3,4)]
    b = set()
    for x, y in a :
        if y == k : continue
        if x < ee[0] : b.add((x,y))
        elif x % 5 == 0 : b.add(ee[1])
        else : b.add(ee[0])
    return b
def shag(t):
    if t%2 == 1 : return set([p for p in G if pi(p) & L])
    return set([p for p in G if pi(p) <= W])
for t in range(1,7):
    R = shag(t)
    if t%2 == 1 : W=W.union(R)
    if t%2 == 0 : L=L.union(R)
    G = G - R
ans = sorted(R & St)
print(f't={t} {len(ans)=} {ans[:2]}...{ans[-2:]}')
