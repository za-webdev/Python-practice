
# takes a list of numbers and prints out 

def draw_stars(my_count):
	for x in range(len(my_count)):
		x = "*"*my_count[x]
		print x

draw_stars([4,6,1,3,5,7,25])


# when a string is passed instead of displaying * displays the first letter of the string as small letter


def new_stars(my_arr):
	for x in range(len(my_arr)):
		if type(my_arr[x])==int:
			print my_arr[x]*"*"
		if type(my_arr[x])==str:
			a=my_arr[x][0]7
			b= a*len(my_arr[x])
			print b.lower()


		
new_stars([1,'Hello',3,4])
