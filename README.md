Mine Blast Program
==================

The mine blast program was writtin to solve the following problem:

"Assume you have a graph of points, where each point represents a mine, and
every mine has a blast radius. Create a program that finds the mine (or set of mines) that triggers the greatest number of additional mines."

Approach / Strategy
-------------------

The program goes about solving the problem above by iterating over every
point (i.e, mine) in a graph and activating any other points (i.e., mines) that fall within the blast radius. 

In particular, if given a point a0 (origin) with N points that fall within the origin radius (edge points), the program creates an array that includes origin and edge points. Each array is then mapped to a key in a python dict that represents the origin (a0).

With the data structure in place, the program recursively traverses each key / value pair, i.e., {a0: [edges]}, until all overlapping edges are correctly groupped.

```
mine_group = {
	p0: [p1, p2],
	p1: [],
	p2: [p1]
}

```

Note, for simplicity you'll see that we create a mapping such that each mine is represented by a unique number (e.g., p0 )

```
graph = [
	{x: 0.1, y: 0.1, r: 2},
	{x: 1.1, y: 0.5, r: 0.5},
	{x: 3.2, y: 2.1, r: 1.2}
]



```

Running Unit Tests
------------------
To run the python unit tests simply cd into the mineblast directory and run the following:

```
python -m unittest test
```
