# Yousef Alsabr
# 102056080
# Assigment 5
# CSCI 3202

import math
import sys

def readFile(fileName):
	mazeMap = open(fileName, 'r')
	mazeMap = mazeMap.read()
	return mazeMap
	

class Node(object):
	def __init__(self, location, typeS):
		# (x,y)
		self.location = location 
		# 0 = path, 1 = mountain, 2 = wall, 3 = Snake, 4 = barn, 5 = apple
		self.type = typeS
		# set reward depending on type
		if typeS == '1':
			self.reward = -1.0
		elif typeS == '3':
			self.reward = -2.0
		elif typeS == '4':
			self.reward = 1.0
		elif typeS == '50':
			self.reward = 50
		else:
			self.reward = 0.0
		
		self.utility = 0
		self.direction = '' 
		
		self.parent = None 		
		
		self.up = None
		self.down = None
		self.right = None
		self.left = None
		
		
		
		
	def calculateUtility(self):
		# discount factor
		y = 0.9 

		# Check if terminal node
		if self.type == '50':
			self.utility = self.reward
			self.direction = 'Finished'
			return self.utility
		
		# Otherwise calculate the other utilities
		if self.up != None:
			upUtil = self.up.utility
		else:
			upUtil = self.utility
		
		if self.down != None:
			downUtil = self.down.utility
		else:
			downUtil = self.utility
		
		if self.right != None:
			rightUtil = self.right.utility
		else:
			rightUtil = self.utility
		
		if self.left != None:
			leftUtil = self.left.utility
		else:
			leftUtil = self.utility

		# Using the formela for Transition Model Calculations
		upDirection = (0.8 * upUtil) + (0.1 * rightUtil) + (0.1 * leftUtil)
		downDirection = (0.8 * downUtil) + (0.1 * rightUtil) + (0.1 * leftUtil)
		rightDirectionn = (0.8 * rightUtil) + (0.1 * upUtil) + (0.1 * downUtil)
		leftDirection= (0.8 * leftUtil) + (0.1 * upUtil) + (0.1 * downUtil)
		
		# Store in array and get max
		directions = ([upDirection, 'up', self.up], 
					  [downDirection, 'down', self.down], 
					  [rightDirectionn, 'right', self.right], 
					  [leftDirection, 'left', self.left])
					  
		bestDirections = max(directions)
		
		# Update valuse
		self.utility = self.reward + (y * bestDirections[0])
		self.direction = bestDirections[1]
		self.parent = bestDirections[2]

		return self.utility
		
		

def Graph(mazeMap):
	xPos = 0
	yPos = 7
	splits = mazeMap.split('\n')
	newRows = list()
	world = []

	for i in range(10):
			world.append([])
			for j in range(8):
				world[i].append(None)

	for row in splits:
		if row != '':
			newRows.append(row.split(' '))
	
	for c in newRows:
		xPos = 0
		for r in c:
			newNode = Node([xPos, yPos], r)
			world[xPos][yPos] = newNode
			xPos = xPos + 1
		yPos = yPos - 1

	return world
		

def adjNodes(world):
	
	wall = '2';

	for x in range(10):
		for y in range(8):
			current = world[x][y]
			if current.type != wall:
				if x + 1 < 10 and world[x+1][y].type != wall:
					current.right = world[x+1][y]
				if x - 1 >= 0 and world[x-1][y].type != wall:
					current.left = world[x-1][y]
				if y + 1 < 8 and world[x][y+1].type != wall:
					current.up = world[x][y+1]
				if y - 1 >= 0 and world[x][y-1].type != wall:
					current.down = world[x][y-1]
	return world	
		

def ValueIteration(world):
	
	epsilon = (float(sys.argv[2]) * 0.1)/0.9
	delta = epsilon + 1
	
	while delta > epsilon:
		delta = 0
		for y in range(7, -1, -1):
				for x in range(9, -1, -1):
					if world[x][y].type != '2':
						currentUtil = world[x][y].utility
						newUtil = world[x][y].calculateUtility()
						currentdelta = abs(currentUtil - newUtil)
						if currentdelta > delta:
							delta = currentdelta

	return world		
	
		
def printWorld(current, end, totalUtility):
	
	totalUtility += current.utility
	
	if current.type == '50':
		print "Final Location:", "[", current.location[0],"," ,current.location[1],"]" ,"Total Utility:", '%.3f' % totalUtility
		return
	else:
		print "Utility:", '%.2f' % current.utility, " Wtih " ,"Location:", "[", current.location[0],"," ,current.location[1],"]"
		
		return printWorld(current.parent, end, totalUtility)


def main():
	#mapFile, eVal = inputText()
	
	if len(sys.argv) != 3:
		print "Number of arguments wrong"
	elif sys.argv[1] != "World1MDP.txt":
		print "Name of file is wrong, needs to be 'World1MDP.txt'"
	
	fileName = sys.argv[1]
	#epsilonValue = sys.argv[2]

	mazeMap = readFile(fileName)
	world = Graph(mazeMap)
	world = adjNodes(world)
	world = ValueIteration(world)
	printWorld(world[0][0], None, 0)
	#printVals(world)

if __name__ == '__main__':
	main()

