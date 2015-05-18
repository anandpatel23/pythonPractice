def shut_down(s):
    if s == "yes":
        return "Shutting down"
    elif s == "no":
        return "Shutdown aborted"
    else:
        return "Sorry"

>>> def distance_from_zero(x):
    if type(x) == int or type(x) == float:
        return abs(x)
    else:
        return "Nope"
