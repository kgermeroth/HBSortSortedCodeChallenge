"""Given already-sorted lists, `a` and `b`, return sorted list of both.

You may not use sorted() or .sort().

Check edge cases of empty lists:

    >>> sort_ab([], [])
    []

    >>> sort_ab([1, 2,3], [])
    [1, 2, 3]

    >>> sort_ab([], [1, 2, 3])
    [1, 2, 3]

Check:

    >>> sort_ab([1, 3, 5, 7], [2, 6, 8, 10])
    [1, 2, 3, 5, 6, 7, 8, 10]
"""


def sort_ab(a, b):
	"""Given already-sorted lists, `a` and `b`, return sorted list of both.

	You may not use sorted() or .sort().
	"""

	new_list = []

	# If both input lists are empty, just return the new_list
	if a == [] and b == []:
		return new_list

	# if list a is blank but list b is not, add list b to new_list
	elif a == [] and b != []:
		new_list.extend(b)
		return new_list

	# if list b is blank but list a is not, add list a to new_list
	elif a != [] and b ==[]:
		new_list.extend(a)
		return new_list

	# if none of the lists are empty:
	else:
		# index counters for lists a and b
		ia = 0
		ib = 0

		# keep the loop going until both lists have been fully iterated through
		while ia < len(a) or ib < len(b):

			# if list a has been fully been fully iterated through add the next 
			# item in list b to new list and increment index for b
			if ia == len(a):
				new_list.append(b[ib])
				ib += 1
			
			# if list b has been fully been fully iterated through add the next 
			# item in list a to new list and increment index for a
			elif ib == len(b):
				new_list.append(a[ia])
				ia += 1

			# if the item in list a is less than item in list b, add to new list 
			# and increment index for a
			elif a[ia] < b[ib]:
				new_list.append(a[ia])
				ia += 1

			# if the item in both lists are equal, add them both to the new list 
			# and increment both index counters
			elif a[ia] == b[ib]:
				new_list.append(a[ia])
				new_list.append(b[ib])
				ia += 1
				ib += 1

			# if item in list b is less than item in list a, add to new list and
			# increment index for b
			else:
				new_list.append(b[ib])
				ib += 1

	return new_list

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. YOU'RE A MERGE CHAMPION!!\n")
