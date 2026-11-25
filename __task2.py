win = 97
start = 4

def add1(a):
	return a+1
def imul(a):
	return a*3

vtable = [add1, imul]

def step(amount_a,amount_b=0, pc = 0):
	if (pc > 3): return False

	if (amount_a + amount_b) >= win: # CHANGEME TO <= if DIV or DEC
		if (pc == 1): return False
		return pc % 2 == 1  # 0 == Second, 1 == First

	opcodes = []
	for sub in vtable:
		opcodes.append(step(sub(amount_a) ,amount_b, pc+1))
		if (amount_b != 0):
			opcodes.append(step(amount_a, sub(amount_b), pc+1))

	if (pc % 2 == 1): # 1 = First
		return all(opcodes)
	return any(opcodes)


# for i in range(1, win):
# 	if step(i, 0, 0):
# 		print(i)

for i in range(1, win):
	if step(start, i, 0):
		print(i)
