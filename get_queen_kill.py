lst = []
for i in range(8):
    lst.append(list(map(int, input().split())))

# print(lst)
is_killing = False

for i in range(8):
    x1, y1 = lst[i][0], lst[i][1]

    for j in range(i+1, 8):
        x2, y2 = lst[j][0], lst[j][1]
        if x1 == x2 or y1 == y2: # check in on one line
            print("YES")
            
            is_killing = True
            break
            
        
        elif x1 + y1 == x2 + y2:
            print("YES")
            is_killing = True
            break
            
    if is_killing == True:
        break

if is_killing == False:
    print("NO")
