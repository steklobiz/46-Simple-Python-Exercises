a=[3,64,73,45,3]
def max_in_list (x):
	max=x[0]
	for _ in x[1::]:
		if _>max:
			max=_
	return max

print (max_in_list(a))