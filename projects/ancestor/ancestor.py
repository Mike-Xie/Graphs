from typing import List, Tuple
Lineage = Tuple[int, int]
Ancestor_List = List[Lineage]
""" UPER

Understand: The input is a list of tuples that are one way edges between parent
child relationships. Each node in the graph is identified with their unique int

We have to write a function that takes a graph, a node, and returns the earliest
known ancestor which is the furthest node away. In case of ties, return the
one with the smallest number and return -1 if nothing is found.

Plan: The graph is a directed acyclic graph. The most straight forward thing to
do seems to be to do a DFS and for debugging purposes probably keep a list of
list of integers which will represent a lineage path. Then filter by longest
length of a lineage and then by whichever ancestor is the earliest. 

Negative one is returned when either a person with no children is the input or
a person who does not exist in the graph is input. 

    '''
       10
     /
    1   2   4  11
     \ /   / \ /
      3   5   8
       \ / \   \
        6   7   9
    '''

In our example graph which is illustrated above and in dict form below:

{3: [1, 2], 6: [3, 5], 7: [5], 5: [4], 8: [4, 11], 9: [8], 1: [10]}

10, 2, 4, 11 would return -1. They do not exist among the values of the dictionary

Actually, since this is deterministic, it might be better to 
"""
def earliest_ancestor(ancestors: Ancestor_List, starting_node: int) -> int:
	child_parent_format: Ancestor_List = [tuple(reversed(x)) for x in ancestors]
	graph = {}

	for i in child_parent_format:
		graph.setdefault(i[0], []).append(i[1])

	return(graph)    

ancestor_list = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
graph = {}

for i in ancestor_list:
	graph.setdefault(i[0], []).append(i[1])

print(graph)

print(earliest_ancestor(ancestor_list, 1))

name_list = [("Sean", 5), ("Dave", 20), ("Sean", 11)]

print(dict(name_list))