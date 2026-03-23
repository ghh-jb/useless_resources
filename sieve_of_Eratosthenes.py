def sieve(N):
	M = [0,0,1] + [1,0] * (N//2)
	for d in range(2, int(N**0.5 + 1)):
		if M[d]:

			dd, d2 = d * d, d * 2
			M[dd:N:d2] = [0] * len(range(dd, N, d2))
	return M
# this is an attemt to make the most effective prime numbers searcher in python
