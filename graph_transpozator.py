from pprint import pprint
digraph = eval(input())

new_digraph = {}

for key in digraph:
	new_digraph[key] = set()

for key in digraph:
	Ω = digraph[key]
	# print(Ω)
	for µ in Ω:
	# 	print(µ)
		new_digraph[µ].add(key)

pprint(new_digraph)
