# Add up and print the sum of the all of the minimum elements of each inner array:
# [[8, 4], [90, -1, 3], [9, 62], [-7, -1, -56, -6], [201], [76, 18]]
# The expected output is given by:
# 4 + -1 + 9 + -56 + 201 + 18 = 175
# You may use whatever programming language you'd like.
# Verbalize your thought process as much as possible before writing any code. 
# Run through the UPER problem solving framework while going through your thought process.

"""
Input: A list of list of integers

Output is a single integer 

For each of the input lists:
	find its minimum element and store it somewhere, probably in a list

And then return the sum of each of these minimum elements 
"""

from typing import List 

def min_sum(two_d_list: List[List[int]]) -> int:
	lowest_int_list = []

	for ls in two_d_list:

		lowest_int_list.append(min(ls))

	print(sum(lowest_int_list))
	return sum(lowest_int_list)


min_sum([[8, 4], [90, -1, 3], [9, 62], [-7, -1, -56, -6], [201], [76, 18]])