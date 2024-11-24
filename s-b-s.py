#step-by-step nums idk how is it in english (also div by 3)
# based on arythmetical progressions

# this task was really brainf*** so now it here

#5 rc-1
def counter(S):
  
  # An = A1 + d*(n - 1), d = 3
  # S = n*(A1 + An)/2 = n*(A1 + A1 + d*(n - 1))/2
  # 2*S = n*(2*A1 + d*(n - 1))
  # 2*S = 2*n*A1 + d*n*n - d*n
  # d*n*n + (2*A1 - d)*n - 2*S = 0

  d = 3
  cnt = 0
  for A1 in range(3, S//2 + 3, 3):
    a = d
    b = 2*A1 - d
    c = -2*S
    discr = b**2 - 4*a*c
    distrSqrt = discr**0.5

    n1 = (-b + distrSqrt) / 6
    n2 = (-b - distrSqrt) / 6

    if (n1 > 0 and n1%1 == 0.0) or (n2 > 0 and n2%1 == 0.0):
      # print(A1, n1, n2)
      cnt += 1

  if S%3 == 0:
    cnt += 1
    # print(S, 1)

  return cnt

# print(counter(63))
# print(counter(9))
# print(counter(72000))
# print(counter(3072))
# print(counter(1503))

print(counter(int(input())))
