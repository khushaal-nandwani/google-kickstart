from math import log2

def binary_list(m):
	# precondition
	# assert m >= 0 and isinstance(m, int)
	(divisor, sum_list, pow) = (m, [], 0)
	while divisor != 0:
		# loop invariant
		assert sum(sum_list) + (divisor * 2**pow) == m
		sum_list = [2**pow * (divisor % 2)] + sum_list
		divisor //= 2
		pow += 1
	# postcondition(s)
	assert all([x == 0 or log2(x) == int(log2(x)) for x in sum_list])
	assert sum(sum_list) == m
	return sum_list
