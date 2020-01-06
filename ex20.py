vocab={"merry":"god", "christmas":"jul", "and":"och", "happy":"gott", "new":"nytt", "year":"ar"}

def translate (s):
	new_string=""
	for word in s.split():
		#print (word.lower())
		new_string = new_string + str(vocab.get(word.lower()))+" "


	return new_string

print (translate ("Merry christmas and happy New Year"))