# Yousef Alsabr
# 102056080
# Assignemnt 7

import random

# Credit for using this idea of nodes to Pradyumna Kikkeri
class Node(object):
	def __init__(self, name):
		self.name = name
		self.value = None
		self.probability = None

# initilize
cloudy = Node('Cloudy')
cloudy.value = 0.5

rainy = Node('Rainy')
rainy.probability = {True: 0.8, False: 0.2}

sprinkler = Node('Sprinkler')
sprinkler.probability = {True: 0.1, False: 0.5}

wetGrass = Node('WetGrass')
wetGrass.probability = {(True, True): 0.99, (True, False): 0.9, (False, True): 0.9, (False, False): 0.0}


# The data sample
samples = [0.82,	0.56,	0.08,	0.81,	0.34,	0.22,	0.37,	0.99,	0.55,	0.61,	0.31,	0.66,	0.28,	1.0,	0.95,	
0.71,	0.14,	0.1,	1.0,	0.71,	0.1,	0.6,	0.64,	0.73,	0.39,	0.03,	0.99,	1.0,	0.97,	0.54,	0.8,	0.97,	
0.07,	0.69,	0.43,	0.29,	0.61,	0.03,	0.13,	0.14,	0.13,	0.4,	0.94,	0.19, 0.6,	0.68,	0.36,	0.67,	
0.12,	0.38,	0.42,	0.81,	0.0,	0.2,	0.85,	0.01,	0.55,	0.3,	0.3,	0.11,	0.83,	0.96,	0.41,	0.65,	
0.29,	0.4,	0.54,	0.23,	0.74,	0.65,	0.38,	0.41,	0.82,	0.08,	0.39,	0.97,	0.95,	0.01,	0.62,	0.32,	
0.56,	0.68,	0.32,	0.27,	0.77,	0.74,	0.79,	0.11,	0.29,	0.69,	0.99,	0.79,	0.21,	0.2,	0.43,	0.81,	
0.9,	0.0,	0.91,	0.01]

prior = {"c":0.0, "r":0.0, "c|r": 0.0, "w":0.0, "s|w":0.0, "c|w":0.0, "s|c, w":0.0}
rejec = {"c":0.0, "r":0.0, "c|r": 0.0, "w":0.0, "s|w":0.0, "c|w":0.0, "s|c, w":0.0, "w|s, r": 0.0, "r,s|c": 0.0}

def priorSampling(samples):
	results = []
	for i in range(0, 100, 4):
		result = {}
		if samples[i] <= cloudy.value:
			result['clouds'] = True
		else:
			result['clouds'] = False

		c = result['clouds']

		if samples[i+1] <= sprinkler.probability[c]:
			result['sprinkle'] = True
		else:
			result['sprinkle'] = False

		if samples[i+2] <= rainy.probability[c]:
			result['rain'] = True
		else:
			result['rain'] = False
		
		s = result['sprinkle']
		r = result['rain']

		if samples[i+3] <= wetGrass.probability[s, r]:
			result['wet'] = True
		else:
			result['wet'] = False

		results.append(result)
		
		resultsleng = len(results)
		
	for sample in results:
		if sample['clouds'] == True:
			prior["c"] += 1.0
		if sample['rain'] == True:
			prior["r"] += 1.0
			if sample['clouds'] == True:
				prior["c|r"] += 1.0
		if sample['wet'] == True:
			prior["w"]+= 1
			if sample['sprinkle'] == True:
				prior["s|w"] += 1
		if sample['clouds'] == True:
			if sample['wet'] == True:
				prior["c|w"] += 1
				if sample['sprinkle'] == True:
					prior["s|c, w"] += 1
	
	print("P(c = true)", prior["c"]/float(resultsleng))
	print("P(c = true | r = true)", prior["c|r"]/prior["r"])
	print("P(s = true | w = true)", prior["s|w"]/prior["w"])
	print("P(s = true | c = true, w = true)", prior["s|c, w"]/prior["c|w"])
	
	
## Rejection

def rejectionSampling(samples):
	results = []
	for i in range(0, 100, 4):
		result = {}
		if samples[i] <= cloudy.value:
			result['clouds'] = True
		else:
			result['clouds'] = False

		c = result['clouds']

		if samples[i+1] <= sprinkler.probability[c]:
			result['sprinkle'] = True
		else:
			result['sprinkle'] = False

		if samples[i+2] <= rainy.probability[c]:
			result['rain'] = True
		else:
			result['rain'] = False
		
		s = result['sprinkle']
		r = result['rain']

		if samples[i+3] <= wetGrass.probability[s, r]:
			result['wet'] = True
		else:
			result['wet'] = False

		results.append(result)
		
		resultsleng = len(results)
		
		prob = {}
		count = []

	for sample in results:
		if sample['clouds'] == True:
			rejec["c"] += 1.0
			if sample['rain'] == True and sample['sprinkle'] == True:
				if sample['wet']:
					count.append([sample['clouds'], sample['rain'], sample['sprinkle'], sample['wet']])
					reject["w | s, r"] +=1
				else:
					count.append([sample['clouds'], sample['rain'], sample['sprinkle'], sample['wet']])
			elif sample['rain'] == False and sample['sprinkle'] == True:
				if sample['wet']:
					count.append([sample['clouds'], sample['rain'], sample['sprinkle'], sample['wet']])
				else:
					count.append([sample['clouds'], sample['rain'], sample['sprinkle'], sample['wet']])
			elif sample['rain'] == True and sample['sprinkle'] == False:
				if sample['wet']:
					count.append([sample['clouds'], sample['rain'], sample['sprinkle'], sample['wet']])
				else:
					count.append([sample['clouds'], sample['rain'], sample['sprinkle'], sample['wet']])
			elif sample['rain'] == False and sample['sprinkle'] == False:
					count.append([sample['clouds'], sample['rain'], sample['sprinkle'], False])
			
		if sample['clouds'] == False:
			rejec["c"] += 1.0
			if sample['rain'] == True and sample['sprinkle'] == True:
				if sample['wet']:
					count.append([sample['clouds'], sample['rain'], sample['sprinkle'], sample['wet']])
				else:
					count.append([sample['clouds'], sample['rain'], sample['sprinkle'], sample['wet']])
			elif sample['rain'] == False and sample['sprinkle'] == True:
				if sample['wet']:
					count.append([sample['clouds'], sample['rain'], sample['sprinkle'], sample['wet']])
				else:
					count.append([sample['clouds'], sample['rain'], sample['sprinkle'], sample['wet']])
			elif sample['rain'] == True and sample['sprinkle'] == False:
				if sample['wet']:
					count.append([sample['clouds'], sample['rain'], sample['sprinkle'], sample['wet']])
				else:
					count.append([sample['clouds'], sample['rain'], sample['sprinkle'], sample['wet']])
			elif sample['rain'] == False and sample['sprinkle'] == False:
					count.append([sample['clouds'], sample['rain'], sample['sprinkle'], False])

	#used for if statements
	c = 0
	r = 1
	s = 2
	w = 3
	#problem 3a
	i = 0.0
	j = 0.0
	for x in count:
		if x[c] == True:
			i += 1.0
		if x[c] == False:
			j += 1.0
	# P(c) = #c/(#c+#~c)
	print("P(c = true) : ",i/(i+j))

	#problem 3b
	i = 0.0
	j = 0.0
	for x in count:
		if x[c] == True and x[r] == True:
			i += 1.0
			#print(x,x[c],x[r],i)
		if x[c] == False and x[r] == True:
			j += 1.0
	# P(c|r) = #cr/(#cr + #~cr) bc we care about r being +, c could be + or -
	print("P(c = true | r = true)",i/(i+j))

	#problem 3c
	i = 0.0
	j = 0.0
	for x in count:
		if x[s] == True and x[w] == True:
			i += 1.0
		if x[s] == False and x[w] == True:
			j += 1.0
			#print(x,x[s],x[w],i)
	# P(s|w) = #sw/(#sw + #~sw) bc we care about w being +, s could be + or -
	print("P(s = true | w = true)",i/(i+j))

	#problem 3d
	i = 0.0
	j = 0.0
	for x in count:
		if x[s] == True and x[c] == True and x[w] == True:
			i += 1.0
		if x[s] == False and x[c] == True and x[w] == True:
			j += 1.0
			#print(x,x[s],x[c],x[w],i)
	# P(s|cw) = #scw/(#scw + #~scw) bc we care about c and w being +, s could be + or -
	print("P(s = true | c = true, w = true)",i/(i+j))
	

def main():
	
	priorSampling(samples)
	rejectionSampling(samples)

if __name__ == '__main__':
	main()

