a=[14,63,75,34,8]
b=[35,33,88,75]
def overlapping (x,y):
	for i in x:
		for j in y:
			if i==j:
				return True
	return False

print (overlapping (a,b))