"""
Add up and print sum of min element in each inner array
Arrays may be nested arbitrarily deep


"""

def min_finder(arr):
	""" 
	Use recursive helper function to find sum of mins
	"""

	min_list = []

	recurser(arr, min_list)


	return sum(min_list)


def recurser(arr, min_list):
	# reset to zero each time we look for new min in a list
	mins = None 


	for i in arr:
		# recursively call to dig deeper into nested list if it is still a list
		if isinstance(i, list):
			print(i)
			recurser(i, min_list)

		else:
			if mins is None:
				mins = i 
			elif mins > i:
				mins = i
	if mins:
		min_list.append(mins)

if __name__ == "__main__":

	arr = [
  [8, [4]], 
  [[90, 91], -1, 3], 
  [9, 62], 
  [[-7, -1, [-56, [-6]]]], 
  [201], 
  [[76, 0], 18],
]

	print(min_finder(arr))