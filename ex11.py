def generate_n_chars(n,c):
	return (n*c)

def generate_n_chars2(n,c):
	st=""
	for i in range(n):
		st+=c
	return st


print (generate_n_chars2(2,"-"))