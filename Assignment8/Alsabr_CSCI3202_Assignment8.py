# Yousef Alsabr
# 102056080
# Assigment 8
# CSCI 3202

import sys

letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','_']

states = [] # Hold all of the s's
observations = [] # Hold all of the o's


# Read file and split the colums into two,
# Store each as States and observations
def readFile(filename):
	f = open(filename)
	for c in f:
		splits = c.split()
		if len(splits) > 1:
			states.append(splits[0])
			observations.append(splits[1])
		

# Calculate Emission by looping throw the letters one by one
# Then count how many times they show up
# Smooth things over using Laplace-smoothed
# Return the Emission probability 
def calculateEmission(xt, et):
	
	count_xt = []
	count_et = []
	smoother_num = 1.0
	smoother_den = 27.0
	
	
# -- Failed attempt only worked with calculateMarginal
# -- Couldn't figure out how to make the list stop before the end
#	for s in states:
#		if xt == s:
#			count_xt.append(s)
#			if et == s:
#				count_et.append(s)
	
	for i in range(0, (len(states)-1)):
		if states[i] == xt:
			count_xt.append(states[i])
			if observations[i] == et:
				count_et.append(states[i])
	
	smoother_num += len(count_et)
	smoother_den += len(count_xt)
	
	return (smoother_num / smoother_den)

# Calculate Transition by looping throw the letters one by one
# Then count how many times the start equals the next
# Smooth things over using Laplace-smoothed
# Return the Transition probability 
def calculateTransition(xt_0, xt_1):
	
	count_xt_0 = []
	count_xt_1 = []
	smoother_num = 1.0
	smoother_den = 27.0
	
	
	for i in range(0, (len(states)-2)): # since we are checking the next state
		if states[i] == xt_0:
			count_xt_0.append(states[i])
			if states[i+1] == xt_1:
				count_xt_1.append(states[i+1])
	
	smoother_num += len(count_xt_1)
	smoother_den += len(count_xt_0)
	
	return (smoother_num / smoother_den)			

# Calculate Marginal / starter state by looping throw the letters one by one
# Then count how many times they appear then dividing by the total
# Smooth things over using Laplace-smoothed
# Return the Transition probability 
def calculateMarginal(xt):
	count_xt = []
	smoother_num = 1.0
	smoother_den = 27.0
	
	for s in states:
		if xt == s:
			count_xt.append(s)
	
	smoother_num += len(count_xt)
	smoother_den += len(states)
	
	return (smoother_num / smoother_den)


def printEmission():
	print "------------Emission------------\n"
	print "------------P(Et | Xt)------------\n"
	for i in range(27):
		for j in range(27):
			print "P(",letters[j],"|",letters[i],") = ", calculateEmission(letters[i], letters[j])


def printTransition():
	print "------------Transition------------\n"
	print "------------P(Xt+1 | Xt)------------\n"
	for i in range(27):
		for j in range(27):
			print "P(",letters[j],"|",letters[i],") = ", calculateTransition(letters[i], letters[j])
			
def printMarginal():
	print "------------Marginal------------\n"
	print "------------P(Xt)------------\n"
	for i in range(27):
		print "P(",letters[i],") = ", calculateMarginal(letters[i])
	

def main():
	
	readFile(sys.argv[1])
	printEmission()
	print "------------End------------\n\n\n"
	printTransition()
	print "------------End------------\n\n\n"
	printMarginal()
	print "------------End------------\n\n\n"

if __name__ == '__main__':
	main()

