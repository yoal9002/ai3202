# Yousef Alsabr
# 102056080
# Assigment 8
# CSCI 3202

# credit to https://en.wikipedia.org/wiki/Viterbi_algorithm for help


import sys
import math
sys.setrecursionlimit(300000)

letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','_']

states = [] # Hold all of the s's
observations = [] # Hold all of the o's
#Part 2
actual_states = [] # Hold all of the s's for part 2 
actual_observations = [] # Hold all of the o's part 2
actual_sequence = []
Emission = [] 
Transition_list = []
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
	Emission.append(-1*(math.log10(p))) #Hold the list with index log(E) and log(J)

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
	
	Transition_list.append(-1*(math.log10(p)))
	
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
	return p


def printfunction():
	
	print "------------Emission------------\n"
	print "------------P(Et | Xt)------------\n"
	for i in range(27):
		for j in range(27):
			print "P(",letters[j],"|",letters[i],") = ", calculateEmission(letters[i], letters[j])
	
	
	print "------------End------------\n\n\n"
	print "------------Transition------------\n"
	print "------------P(Xt+1 | Xt)------------\n"
	for i2 in range(27):
		for j2 in range(27):
			print "P(",letters[j2],"|",letters[i2],") = ", calculateTransition(letters[i2], letters[j2])
			
	
	print "------------End------------\n\n\n"
	print "------------Marginal------------\n"
	print "------------P(Xt)------------\n"
	for i3 in range(27):
		print "P(",letters[i3],") = ", calculateMarginal(letters[i3])
	
	print "------------End------------\n\n\n"

def printfunction2():
	
	print "------------PART 2------------\n"
	print "------------State sequence------------\n"
	
	for s in actual_sequence:
		print s,
	
	print "------------End------------\n\n"

	print "------------PART 2------------\n"
	print "------------Error rate: ------------\n"
	
	print calculateError()
	
	
	

# Part 2
def viterbiinitiate():
	prob = 0.0
	index1 = 0
	max_letter = ''
	
	for i in range(27):
		index1 = (27 * i) + letters.index(actual_observations[0])
		prob = -1*(math.log10(calculateMarginal(letters[i]))) + Emission[index1]
		sum_prob.append(prob)
	
	max_letter = letters[(sum_prob.index(min(sum_prob)))]
	actual_sequence.append(max_letter)
	
	return max_letter
		
def viterbirun(start_letter, index):
	options = [999999999999999999.0]*27
	
	if index < len(actual_observations):
		
		for cuurent in range(27):
			for previous in range(27):
				log_probability = Transition_list[((27 * previous) + cuurent)] + Emission[(27*letters.index(actual_observations[index])) + cuurent] + sum_prob[previous]
				if options[cuurent] > log_probability:
					 options[cuurent] = log_probability # store the best possible state
					
		for i in range(27):
			sum_prob[i] = options[i]
		
		max_letter = letters[(sum_prob.index(min(sum_prob)))]
		actual_sequence.append(max_letter)
		viterbirun(index, index+1)
	
	return actual_sequence

def calculateError():
	error = 0.0
	actual1 = 0.0
	l = (len(actual_observations))
	for i in range(l):
		if actual_sequence[i] == actual_states[i]:
			actual1+=1
	
	error = 1 - (actual1 / l)
	return error
	
	

def main():
	
	readFile(sys.argv[1])
	readFile2(sys.argv[2])
	printfunction()
	
	viterbiinitiate()
	viterbirun(actual_sequence[0], 1)
	printfunction2()
	

if __name__ == '__main__':
	main()

