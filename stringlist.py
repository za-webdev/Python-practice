

my_str='Today is a good day!'
x=my_str.find('good')
print x

#replacing words
sent="It is a sunny day"
print sent.replace('is','was')

#finding min, max,length and sorting

numbers=[23,45,2,6,4,7,28]
print min(numbers)

print max(numbers)

print sorted(numbers)

print len(numbers)


#finding and replacing
words = "It's thanksgiving day. It's my birthday,too!"
x=words.find('day')
print x

print words.replace('day','month',1)

#finding max and min
x = [2,54,-2,7,12,98]
print 'Max is',max(x)

print 'Min is',min(x)

#finding only first and last values and creating a new list conating only first and last values

y = ["hello",2,54,-2,7,12,98,"world"]
a = y[0]
print a
b=y[-1]
print b

z=[a,b]
print z

#Sorting list first.Then, spliting list in half. Push the list created from the first half to position 0 of the list created from the second half.

x = [19,2,54,-2,7,12,98,32,10,-3,6]
A=sorted(x)
B = A[:len(A)/2]
C = A[len(A)/2:]
C.insert(0,B)
print C

