a=[1,47,85,4]
def is_member(x,a):	
	print(a)
	if x in a:
		return True
	else:
		return False
def is_member2 (x,a):
	for _ in a:
		if (_ == x):
			return True
	return False

print (is_member2(2,a))
print (is_member2(4,a))