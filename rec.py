a = [-1337] * 100000

def f(n):
	if (a[n] != -1337):
		return a[n]
	if (n == 0):
		a[n] = 1
		return 1
	if (n > 0):
		a[n] = 2 * f(1-n) + 3 * f(n-1) + 2
		return a[n]
	if (n < 0):
		a[n] = -1 * f(-1 * n)
		return a[n]




print(f(50))
	# if (n % 3 == 1 and n > 3):
	# 	return 4 + f(n//3)
	# if (n % 3 == 2 and n > 3):
	# 	return n ** 2 + f(n-2)
'''
def q(n):
	if (n == 1):
		return 1
	if (n > 1):
		return q(n-1)-2*f(n-1)
'''
