import sys

# mZL primitive functions

def car(linelist):
    return linelist[0]

def cdr(linelist):
    return linelist[-1:]

def atomq(linelist):
    return (len(linelist) == 1) and (not isinstance(linelist[0], list))

def eqq(linelist1, linelist2):
    return linelist1 == linelist2

def cons(linelist1, linelist2):
    return linelist1 + linelist2

def nullq(linelist):
    return linelist == []

def ver(linelist):
    return linelist

def zlist(*linelist):
    return [sum(i) for i in zip(*linelist)]

def cond(*linelist):
    # TODO
    return True

def warn():
    return "Non-fatal error, check your input"

def error():
    sys.exit()

# mZL primitive atoms

hasht = True

hashf = False

null = []
