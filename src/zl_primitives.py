def init():
    # Define all the primitive functions of ZLang
    print("Initialized ZLang primitives")

# mZL primitives
def car(line):
    # Get the car using string slicing, mind the parenthesis
    return line.split()[0][1:] 

def cdr(line):
    # Making the cdr while maintain "list string" format
    separator = ", "
    return "(" + separator.join(line.split()[1:]).replace(separator, " ")

