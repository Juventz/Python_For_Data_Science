def NULL_not_found(obj: any) -> int:
    obj_type = type(obj)

    # None is the absence of a value
    if obj_type is type(None):
        print(f"Nothing: {obj} {obj_type}")

    # nan is a floating-point number that represents
    # an undefined or unrepresentable value
    # nan is not equal to any value, including itself
    elif obj_type is float and obj != obj:
        print(f"Cheese: nan {obj_type}")

    elif obj_type is int and obj == 0:
        print(f"Zero: {obj} {obj_type}")

    # Vérifier si l'objet est une chaîne vide
    elif obj_type is str and obj == '':
        print(f"Empty: {obj_type}")

    # False is a boolean value that represents the absence of a value
    elif obj_type is bool and obj is False:
        print(f"Fake: {obj} {obj_type}")

    # Unexcepted error type
    else:
        print("Type not Found")
        return 1

    return (0)
