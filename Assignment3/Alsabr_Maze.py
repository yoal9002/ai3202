# Yousef Alsabr
# 102056080
# Assigment 3
# CSCI 3202

import heapq
import math
import sys

def readMaze(filename):
	maze = [[],[],[],[],[],[],[],[],[],[]]
	with open(filename) as f:
		for line in f:
			for i, j in enumerate(line.split()):
				maze[i].append(int(j))
	
	return maze

class MyNode(object):
	
	def __init__(self, x, y, sNum):
		self.x = x
		self.y = y
		self.sNum = sNum
		
		self.distanceFromStart = 0
		self.parent = None
		self.heuristic = None
		self.f = None
	
	def getAcualDistance(self, parent, specialNum, heuristic):
		# Get he cureent Node in order to calculate whether we are going
		# horizontal/vertical or diagonal
		self.parent = parent
		currentDistance = abs(parent.x-self.x) + abs(parent.y-self.y)
		
		# diagonal
		if(currentDistance == 2):
			self.distanceFromStart = parent.distanceFromStart + 14
		# horizontal/vertical
		elif(currentDistance == 1):
			self.distanceFromStart = parent.distanceFromStart + 10
		
        # Mountains adds 10 no matter what
		if(specialNum == 1):
			self.distanceFromStart += 10
		
		# Manhatten
		# Using (9,7) since we know this is the goal
		if(heuristic == 'M' or heuristic == 'm'):
			self.heuristic = abs(9-self.x)+abs(7-self.y)
		
		#euclidean distance
		# Using (9,7) since we know this is the goal
		elif(heuristic == 'E' or heuristic == 'e'):
			dx = abs(9-self.x)
			dy = abs(7-self.y)
			self.heuristic = 10 * (math.sqrt(dx * dx + dy * dy))
		
		# update f
		self.f = self.distanceFromStart + self.heuristic

	def compareDistance(self, newNode, specialNum):
		distToNewNode = abs(newNode.x-self.x)+abs(newNode.y-self.y)
		newDistance = 0
		
		if(distToNewNode == 2):
			newDistance = newNode.distanceFromStart + 14
		elif(distToNewNode == 1):
			newDistance = newNode.distanceFromStart + 10
			
		if(specialNum == 1):
			newDistance += 10
		
		if(newDistance < self.distanceFromStart):
			self.distanceFromStart = newDistance
			self.parent = newNode
			self.f = self.distanceFromStart + self.heuristic
			
	
	def compareNodes(self, otherNode):
		return(self.x == otherNode.x and self.y == otherNode.y)

# Failed attempt did not have enough time to work on it.
# Mistake found but by then already solved with another way		
def getAdjacent(current, maze, closed):
		adjNodes = []
		appenedOpen = False
		for i in range(-1, 2):
			for j in range(-1, 2):
				xPos = current.x+i
				yPos = current.y+j
				if (xPos >= 0 and xPos <= 9 and yPos >=0 and yPos <= 7):
					nextNode = MyNode(xPos, yPos, maze[xPos][7-yPos])
					appenedClosed = True
					for c in closed:
						if c.compareNodes(nextNode):
							appenedClosed = False
					if (nextNode.sNum != 2 and appenedClosed):	
						adjNodes.append(nextNode)
		return adjNodes

	
def aStarSearch(maze, heuristic):
	opened = []
	closed = [MyNode(-1,-1,-1)]
	start = MyNode(0,0,0)
	opened.append(start)
	visited = 1
	
	while(not closed[-1].compareNodes(MyNode(9,7,0)) and len(opened) > 0):
		opened.sort(key = lambda n: n.f)
		currentNode = opened[0]
		opened.remove(currentNode)
		closed.append(currentNode)
		
		for i in range(-1,2):
			for j in range(-1,2):
				xPos = currentNode.x+i
				yPos= currentNode.y+j
				if(xPos >= 0 and xPos <=9 and yPos >= 0 and yPos <= 7):
					nextNode = MyNode(xPos, yPos, maze[xPos][7-yPos])
					appenedClosed = True
					for c in closed:
						if c.compareNodes(nextNode):
							appenedClosed = False
					if(nextNode.sNum != 2 and appenedClosed):
						appeanedOpen = True
						# Check if visited
						for o in opened:
							if o.compareNodes(nextNode):
								appeanedOpen = False
						# Visit if not
						if appeanedOpen:
							opened.append(nextNode)
							visited += 1
							nextNode.getAcualDistance(currentNode, nextNode.sNum, heuristic)
						# Otherwise comepare it to current Node
						else:
							nextNode.compareDistance(currentNode, nextNode.sNum)
							
		finalNode = closed[-1]
		print("\nCost of the Path: " + `finalNode.distanceFromStart` + "\nNumber of Locations evaluated: " + `visited` + ".\n")
		final = []
		while(finalNode != None):
			final.insert(0, finalNode)
			finalNode = finalNode.parent
		print("----------Nodes Along the Path ----------")
		for i in final:
			print(i.x, i.y)	

def main():
	
	fileName = input("Please select the Maze you want \n1 for 'World1' \n2 for 'World2' \n:")
	heuristic = raw_input("Please select the Heuristic \n'M' or 'm' for Manhatten \n'E' or 'e' for Euclidean \n:")
	
	if(fileName == 1):
		fileName = "World1.txt"
	elif(fileName == 2):
		fileName = "World2.txt"

	world = readMaze(fileName)
	
	#mazeAstar = MazeAStar()
	
	aStarSearch(world, heuristic)

if __name__ == '__main__':
	main()

