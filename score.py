
#function that generates ten scores between 60 and 100. Each time a score is generated,function displays what the grade is for a particular score.

def score_grade():
	for x in range(1,11):
		import random
		x=(random.randint(60,100))
		if x >60 and x<70:
			z="D"
		elif x>70 and x<80:
			z="C"
		elif x>80 and x<90:
			z="B"
		elif x>90 and x<100:
			z="A"
		print "Score:{},Your grade is {}".format(x,z)
	
score_grade()

