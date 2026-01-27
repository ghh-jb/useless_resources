# (^ == and)
# (impl <=???)

def f(x,y,z,w):
	return (0) # put the condition here
	# return (y and not x) or (x == z) or not w

print("x y z w")

for x in 0,1:
	for y in 0,1:
		for z in 0,1:
			for w in 0,1:
				if (f(x,y,z,w)==0):
					print(x,y,z,w)
