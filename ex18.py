def is_paragram(x):
	x=x.lower()#???		
	for _ in range (ord("a"),ord("z")):
		if x.find(chr(_))>=0:
			print (chr(_))
		else:
			return False
	return True


print (is_paragram("The quick brown fox jumps over the lazy dog"))