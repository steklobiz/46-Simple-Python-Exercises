def palindrome (x):
	a=""
	for i in x:
		if i.isalpha():
			a+=i.lower()
	print (a) 
	if a==a[::-1]:
		return True
	else:
		return False

print (palindrome("Go hang a salami I'm a lasagna hog."))