# ai3202

## Yousef Alsabr Assignment 3 AStarSearch

Program can be run with 

```
	$ python Alsabr_Maze.py

```

Follow the instructions shown in the program

*1 for World1.txt*
*2 for World2.txt*

*M or m for Manhattan*
*E or e for Euclidean*


## Heuristics
### Euclidean

“If your units can move at any angle (instead of grid directions), then you should probably use a straight line distance:” - http://theory.stanford.edu/~amitp/GameProgramming/Heuristics.html

I wanted to try the straight line heuristic to test the accuracy of their statement, which is Euclidean will give better results

function: 

```
	function heuristic(node) =
    		dx = abs(node.x - goal.x)
    		dy = abs(node.y - goal.y)
    		return D * sqrt(dx * dx + dy * dy)

```

### Manhattan

The standard heuristic for a square grid is the Manhattan distance. Look at your cost function and find the minimum cost D for moving from one space to an adjacent space. In the simple case, you can set D to be 1. The heuristic on a square grid where you can move in 4 directions should be D times the Manhattan distance:


function:
```
		dx = abs(n.x - self.end.x)
		dy = abs(n.y - self.end.y)
		return D * (dx + dy)
```

## Results

### World 1

#### Manhattan

```
	Cost of the path = 130
	Number of locations evaluated = 62
	Path found:
	[(0, 0), (1, 0), (2, 0), (3, 1), (3, 2), (4, 3), (5, 4), (6, 4), (7, 4), (8, 5), (9, 6), (9, 7)]
```

#### Euclidean

```
	Cost of the path = 138
	Number of locations evaluated = 48
	Path found:
	[(0, 0), (1, 1), (2, 0), (3, 1), (4, 2), (4, 3), (5, 4), (6, 4), (7, 5), (7, 6), (8, 7), (9, 7)]
```

#### Comparison 

Both got relatively close results. However, it seems Euclidean has visited less Nodes.

### World 2

#### Manhattan

```
	Cost of the path = 144
	Number of locations evaluated = 60
	Path found:
	[(0, 0), (1, 0), (2, 0), (3, 1), (3, 2), (4, 3), (5, 4), (6, 4), (7, 5), (8, 6),(9, 7)]
```

#### Euclidean

```
	Cost of the path = 152
	Number of locations evaluated = 38
	Path found:
	[(0, 0), (1, 1), (2, 0), (3, 1), (3, 2), (4, 3), (5, 4), (6, 4), (7, 5), (8, 6), (9, 7)]
```

#### Comparison 

Both got relatively close results. However, it seems Euclidean has visited less Nodes.




