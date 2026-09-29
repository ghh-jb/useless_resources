ee = [1580] # exit condition
G = set(range(1, ee[0])) # reverse from ee[0]+1 , 1000000 if decreasing
L, W = set([ee[0]]), set()
def pi(pos):
    a = [pos+2,pos+7, pos + 13, pos*3, pos*5] # what can we do with this, actions
    b = set()
    for p in a:
        if p < ee[0]: # change if decrementing
            b.add(p)
        else:
            b.add(ee[0])
    return b

def shag(t):
    if t % 2:
        return set(p for p in G if pi(p) & L)
    else:
        return set([p for p in G if pi(p) <= W])

summ = 0
for t in range(1, 80):
    R = shag(t)
    if t % 2 != 0:
        summ += len(R) # for some tasks count summ of length
        W = W.union(R)
    else:
        L = L.union(R)
    G = G -R
    print(t, sorted(R))
print()
print(summ)

