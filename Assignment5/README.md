# ai3202

## Yousef Alsabr 

### CSCI3202 Assignment 5 Markov Decision Processes Value Iteration

#### To run the code:

As indicated the program will run using the command line

```
$ python Alsabr_Assignment5.py World1MDP.txt epsilon

```
### Path Found:

```
[ 0 , 0 ] —> [ 1 , 0 ] —> [ 2 , 0 ] —> [ 3 , 0 ] —> [ 4 , 0 ] —>
[ 5 , 0 ] —> [ 6 , 0 ] —> [ 6 , 1 ] —> [ 6 , 2 ] —> [ 6 , 3 ] —>
[ 6 , 4 ] —> [ 7 , 4 ] —> [ 7 , 5 ] —> [ 8 , 5 ] —> [ 9 , 5 ] —>
[ 9 , 6 ]

```

#### Results:

I decided to run epsilon with low number since if it’s too high we would be setting ourself up for failure. As mention in class.

Epsilon | Path Change | total utility
---|---|---|---
0.1	|N/A	|357.450
0.5	|N/A	|357.423
2.0	|N/A	|357.371
5.0	|N/A	|357.233
9.0	|N/A	|356.882


The results indicate the higher our epsilon the more likely the total utility will be less, this indicates the more we are welling to risk the lower our total utility is.


