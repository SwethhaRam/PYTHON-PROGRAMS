def common_data(list1, list2):
	result = False

	#1st list
	for x in list1:

		#2nd list
		for y in list2:

			#one common
			if x == y:
				result = True
				return result
				
	return result
	
r = [2, 4, 6, 8]
s = [1, 2, 5, 7, 8]
print(common_data(r, s))

