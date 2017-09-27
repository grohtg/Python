id = input("What is your ID?")
print type(id)
def identify_people(f):
    """
    process id and returns name
    :param f: identifier
    :return: name of identifier
    """
    if id ==1:
        return "A"
    elif id == 2:
        return "B"
    elif id == 3:
        return "C"
    else:
        return "someone else"

print identify_people(id)
print type(identify_people)
