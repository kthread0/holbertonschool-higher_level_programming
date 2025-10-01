#!/usr/bin/python3
def max_integer(my_list=[]):
	if not my_list:
		return None
	
	max_value = my_list[0]
	for current_value in my_list[1:]:
		if current_value > max_value:
			max_value = current_value
	
	return max_value
