lst=["war", "peace", "Tolstoy", "world", "mama", "cat"]

def filter_long_words(l,n): #returns how many words from list:l are longer than int:n
	num=0
	for _ in l:
		if len (_) > n:
			num +=1
	return num

print (filter_long_words (lst,4))