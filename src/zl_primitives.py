def car(line):
    # Get the car using string slicing, mind the parenthesis
    return line.split()[0][1:]

def cdr(line):
    # Making the cdr while maintain "list string" format
    separator = ", "
    return "(" + separator.join(line.split()[1:]).replace(separator, " ")

def atomq(line):
    # Decide if the line is an atom
    return (car(line) == "ver") and (len(cdr(line).split()) == 1)

def eqq(line):
    # Decide if two atoms are equal
    return car(line) == car(cdr(line))


