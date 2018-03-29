
#a list of strings and a string containing a single character, and prints a new list of all the strings containing that character.

word_list = ["hello","world","my","name","is","Anna"]
newword=[]
for x in word_list:
	for i in x:
		if i=='o':
			newword.append(x)
print newword

