# DIFFERENT TYPES OF DATA STRUCTURES IN PYTHON : LIST, TUPLE, SET, DICT

# allow to store a collection of ordered elements
# advantage : mutable, ordered, can be access with their index
# and can contain duplicate elements
# disadvantage : slow access to the elements compare
# to the set and the dict and use more memory because the elements are mutable
ft_list = ["Hello", "tata!"]

# allow to store a collection of ordered elements but they are immuable
# advantage : immuable, fast access to the non mutable elements,
# use less memory and can be used as a key in a dict
# disvantage : because they are immuable, we can't modify the elements
# and have to create a new tuple
ft_tuple = ("Hello", "toto!")

# allow to store a collection of UNIQUE elements and
# they don't guarantee the order of the elements at each execution
# advantage : handle mathematical set operations : union, inter, diff,
# and sym diff and fast access to the elements due top the hash function
ft_set = {"Hello", "tutu!"}

# allow to store a collection of key-value pairs
# where each key is UNIQUE and associated with a value who can be of any type
# advantage : fast access to the value associated with a key
ft_dict = {"Hello": "titi!"}

# MODIFIY DATA

# Modiify list (we can modify elements)
# ft_list[1] = "World!"
ft_list.pop()
ft_list.append("World!")

# Modify tuple (we can only create a new one because tuple are immuable)
ft_tuple = ("Hello", "France!")

# Modify set (we can only add or remove elements because
# they don't guarantee the order of the elements)
ft_set.remove("tutu!")
ft_set.add("Paris!")

# Modify dict (we can change the value of a key)
ft_dict["Hello"] = "42Paris!"

# Print the result
print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)
