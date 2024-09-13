# Generator expression filter will product each element one by one,
# if needed, and will not store the entire list in memory

# The function will return a list of elements
# that are true for the function_to_apply

# The function_to_apply will be passed as an argument to the function
# The list_of_inputs will be passed as an argument to the function


# def ft_filter(function_to_apply, list_of_inputs):

# 	# If the function_to_apply is None, return the list of inputs that are true
# 	if function_to_apply is None:
# 		return (item for item in list_of_inputs if item)
# 	else:
# 		# Return the list of inputs that are true for the function_to_apply
# 		return (item for item in list_of_inputs if function_to_apply(item))

# Comprehension list will product the entire list at once,
# and will store the entire list in memory

def ft_filter(function_to_apply, list_of_inputs):

    """
    Ft_filter:
    Filter the list of inputs based on the function_to_apply.
    It use a comprehension list to filter the list of inputs.
    Args:
        - function_to_apply: The function to apply to the list of inputs.
        - list_of_inputs (list): The list of inputs to filter.
    Returns: list: The list of inputs that are true for the function_to_apply
    """

    # If the function_to_apply is None, return the list of inputs that are true
    if function_to_apply is None:
        return [item for item in list_of_inputs if item]
    else:
        # Return the list of inputs that are true for the function_to_apply
        return [item for item in list_of_inputs if function_to_apply(item)]


# def main():
#     function_to_apply = None
#     list_of_inputs = [0, 1, True, 7, False]

#     """
#     Main function to test ft_filter.
#     """

#     # Print the list of inputs
#     print(f"List of inputs: {list_of_inputs}")

#     # Filter the list of inputs
#     filtered_list = ft_filter(function_to_apply, list_of_inputs)
#     filter2 = filter(function_to_apply, list_of_inputs)

#     # Print the filtered list
#     print(f"Filtered list: {filtered_list}")
#     print(f"Filtered list: {list(filter2)}")


# if __name__ == "__main__":
#     main()
