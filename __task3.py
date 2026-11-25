win = 97
start = 4

def add1(a):
	return a+1
def imul(a):
	return a*3

vtable = [add1, imul]


def step(amount_a,amount_b=0, pc = 0, lr=0):
	if (pc > lr): return False
	if (amount_a + amount_b) >= win: # CHANGEME TO <= if DIV or DEC
		return pc % 2 == 0  # 0 == Second, 1 == First

	opcodes = []
	for sub in vtable:
		opcodes.append(step(sub(amount_a) ,amount_b, pc+1, lr))
		if (amount_b != 0):
			opcodes.append(step(amount_a, sub(amount_b), pc+1, lr))


	if (pc % 2 == 0): # 1 = First
		return all(opcodes)
	return any(opcodes)


# for i in range(1, win):
# 	if not step(i, 0, 0, 2) and step(i, 0, 0, 4):
# 		print(i)

for i in range(1, win):
	if not step(start, i, 0, 2) and step(start, i, 0, 4):
		print(i)
