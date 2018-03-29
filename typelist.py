
'''
a=[1,2,"hello",9,"hi"]
total=0
for x in a:
	if isinstance(x,int):
		total+=x
'''

a=[1,2,3,"he",4,"hello","woaww"]
word=" "
num=0
for x in a:
	if isinstance(x,str):
	  	word+=x+' '
	if isinstance(x,int):
	  		num+=x
print "\"String:",word,"\""
print"\"Sum:",num,"\""



