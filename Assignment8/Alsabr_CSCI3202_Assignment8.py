# Yousef Alsabr
# 102056080
# Assigment 8
# CSCI 3202

# credit to https://en.wikipedia.org/wiki/Viterbi_algorithm for help


import sys
import math

letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','_']

states = [] # Hold all of the s's
observations = [] # Hold all of the o's
#Part 2
actual_states = [] # Hold all of the s's for part 2 
actual_observations = [] # Hold all of the o's part 2
correct_sequence = []
emissionlog = []
transitionlog = []
marginallog = []
sum_prob = []
options = [] #As big as possible to look for the min option




# Read file and split the colums into two,
# Store each as States and observations
def readFile(filename):
	f = open(filename)
	for c in f:
		splits = c.split()
		if len(splits) > 1:
			states.append(splits[0])
			observations.append(splits[1])
			
def readFile2(filename):
	f = open(filename)
	for c in f:
		splits = c.split()
		if len(splits) > 1:
			actual_states.append(splits[0])
			actual_observations.append(splits[1])
		

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
	p = (smoother_num / smoother_den)
	#Part 2
#	Emission.append(math.log(p)) #Hold the list with index log(E) and log(J)

	return p

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
	
	p = (smoother_num / smoother_den)
	#Part 2
	
#	Transition_list.append(math.log(p))
	
	return p			

# Calculate Marginal / starter state by looping throw the letters one by one
# Then count how many times they appear then dividing by the total
# Smooth things over using Laplace-smoothed
# Return the Transition probability 
def calculateMarginal(xt):
	count_xt = []
	smoother_num = 1.0
	smoother_den = 27.0
	
	for i in range(len(states)):
		if xt == states[i]:
			count_xt.append(states[i])
	
	smoother_num += len(count_xt)
	smoother_den += len(states)
	p = (smoother_num / smoother_den)
	
#	Marginal.append(math.log(p))
	return p


def printfunction():
	
	print "\n------------PART 1------------\n"
	print "------------Emission------------\n"
	print "------------P(Et | Xt)------------\n"
	for i in range(27):
		for j in range(27):
			print "P(",letters[j],"|",letters[i],") = ", calculateEmission(letters[i], letters[j])
	
	print "------------PART 1------------\n"
	print "------------End------------\n\n\n"
	print "------------Transition------------\n"
	print "------------P(Xt+1 | Xt)------------\n"
	for i2 in range(27):
		for j2 in range(27):
			print "P(",letters[j2],"|",letters[i2],") = ", calculateTransition(letters[i2], letters[j2])
			
	print "------------PART 1------------\n"
	print "------------End------------\n\n\n"
	print "------------Marginal------------\n"
	print "------------P(Xt)------------\n"
	for i3 in range(27):
		print "P(",letters[i3],") = ", calculateMarginal(letters[i3])
	
	print "------------End------------\n\n\n"

def printfunction2():

	print "------------PART 2------------\n"
	print "------------Error------------\n"
	
	print "Error Rate:", viterbi()
	
	print "------------End------------\n\n\n"	
	print "------------PART 2------------\n"
	print "------------Sequence------------\n"
	
	
	sequence = ""
	for i in correct_sequence:
		sequence += letters[i]
	
	print sequence
	

# Part 2
		
def viterbi():
	
	
	emissionlog = [ [ math.log(calculateEmission(letters[j], letters[i])) for i in range(27) ] for j in range(27) ]
	transitionlog = [ [ math.log(calculateTransition(letters[j], letters[i])) for i in range(27) ] for j in range(27) ]
	marginallog = [ math.log(calculateMarginal(letters[i])) for i in range(27) ]
	
	# Used for log addtion
	prevLog = [0.0] * 27
	currentLog = [0.0] * 27
	path = [[0 for i in range(27)] for j in range(len(actual_states))]
	
	for i in range(27):
		prevLog[i] = emissionlog[i][letters.index(actual_observations[0])] + marginallog[i]
	
	for index in range(len(actual_states)):
		for current in range(27):	
			options = [ (emissionlog[current][letters.index(actual_observations[index])] + transitionlog[previous][current] + prevLog[previous]) for previous in range(27) ]
			currentLog[current] = max(options) # get the best option
			path[index][current] = options.index(currentLog[current]) # set option to path
		
		for i in range(27): 
			prevLog[i] = currentLog[i]
			
	actual_sequence = [-1] * len(actual_states)
	bestLog = max(currentLog)
	bestlogindex = currentLog.index(bestLog)
	lastNode = bestlogindex
	for j in range(len(path)-1, -1, -1): # Back track the path
		actual_sequence[j] = lastNode
		lastNode = path[j][lastNode]

	
	
	# Calculate Error Rate 
	correctStates = 0
	for i in range(len(actual_states)):
		if actual_sequence[i] == letters.index(actual_states[i]):
			correctStates += 1

	errorRate = 1.0 - float(correctStates) / float(len(actual_states))
	
	correct_sequence = actual_sequence
	
	
	
	print "------------PART 2------------\n"
	print "------------Error------------\n"
	
	print "Error Rate:", errorRate
	
	print "------------End------------\n"	
	print "------------Sequence------------\n"
	
	sequence = ""
	for i in actual_sequence:
		sequence += letters[i]
	
	print sequence
	
	return errorRate	

def main():
	
	readFile(sys.argv[1])
	readFile2(sys.argv[2])
	viterbi()	
	printfunction()
	
#	printfunction2()
	

if __name__ == '__main__':
	main()

