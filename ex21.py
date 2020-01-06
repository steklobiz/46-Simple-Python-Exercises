import string
def char_freq(s):
	freq_dict={}
	for _ in s:
		freq_dict[_] = freq_dict.get(_,0) +1
	return freq_dict

print (char_freq("abbabcbdbabdbdbabababcbcbab"))