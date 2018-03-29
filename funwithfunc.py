#print the number of the iteration and specify whether it's an odd or even number.

def odd_even():
	for x in range(1,2001):
		if x%2!=0:
			print "Number is {}".format(x),".This is an odd number"
		else:
			print"Number is {}".format(x),".This is an even number"
odd_even()

#returns a list where each value has been multiplied by any given value.

def multiply(arr,val):
	for x in range(len(arr)):
		arr[x]*=val
	return arr

b=multiply([1,2,3],3)
print b

#new function returns multiplied list as a two-dimensional list. Each internal list contains the 1's times the number in the original list.



def layered_multiples(arr):
	new_array=[]
	for i in range(len(arr)):
		arr[i]*=[1]
		new_array.append(arr[i])
	return new_array
  
x = layered_multiples(multiply([2,4,5],3))
print x

#combined
def myfunc(arr,val):
	for x in range(len(arr)):
		arr[x]*=val
		arr[x]*=[1]
	return arr
y=myfunc([1,2,3,4],3)
print y