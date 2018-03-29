
#A function that simulates tossing a coin 5,000 times,function prints how many times the head/tail appears.




def coinToss():
	headcount=0
	tailcount=0
	for x in range(1,50):
		import random
		x=round(random.random())
		if x==1:
			result="Its a head"
			headcount+=1
		elif x==0:
			result="Its a tail"
			tailcount+=1
		print"Throwing a coin...{}... Got {} head(s) so far and {} tails(s) so far".format(result,headcount,tailcount)

coinToss()

