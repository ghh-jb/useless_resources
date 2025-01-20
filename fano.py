#fano
l = list(map(str, input().split()))
is_backward = True

for i in range(len(l)):
    for j in range(len(l)):
        if i == j:
            continue
        # print(i, j)
        if not is_backward:
            if l[i].startswith(l[j]) or l[j].startswith(l[i]):
                print("Fail, not Fano code error at:", l[i], l[j])
                exit()
        else:
            if l[i].endswith(l[j]) or l[j].endswith(l[i]):
                print("Fail, not backword Fano code error at:", l[i], l[j])
                exit()
if not is_backward:
    print("Code ok, Fano code")
else:
    print("Code ok, backward Fano code")
