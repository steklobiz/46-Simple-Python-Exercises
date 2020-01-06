empty = []
lst=["war","peace","Tolstoy"]

def find_longest_word (lst):
	if len(lst)>0:
		max =len (lst[0]) #max = first array member length
		for _ in lst[1::]:
			l=len (_)
			if l>max:
				max=l
		return max
	else:
		return None	
	print (len(lst))

print (find_longest_word(lst))
print (find_longest_word(empty))