# Description: Reproduce the behavior of the filter function in python
# The function will return a list of elements that are true for the function_to_apply
# The function_to_apply will be passed as an argument to the function
# The list_of_inputs will be passed as an argument to the function

# Generator expression filter will product each element one by one, if needed, and will not store the entire list in memory
# def ft_filter(function_to_apply, list_of_inputs):
	
# 	# If the function_to_apply is None, return the list of inputs that are true
# 	if function_to_apply is None:
# 		return (item for item in list_of_inputs if item)
# 	else:
# 		# Return the list of inputs that are true for the function_to_apply
# 		return (item for item in list_of_inputs if function_to_apply(item))
	
# Comprehension list will product the entire list at once, and will store the entire list in memory
def ft_filter(function_to_apply, list_of_inputs):
	
	# If the function_to_apply is None, return the list of inputs that are true
	if function_to_apply is None:
		return [item for item in list_of_inputs if item]
	else:
		# Return the list of inputs that are true for the function_to_apply
		return [item for item in list_of_inputs if function_to_apply(item)]