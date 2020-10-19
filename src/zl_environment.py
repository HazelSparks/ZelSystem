import zl_primitives as zlprim

namespace = {}

def init():
    # Setup namespace, and import primitives
    print("Initialized ZLang environment")
    import_prims()
    import_stdlib()
    
def import_prims():
    print("Importing primitives to env...")
    try:
        prim = open("src/zl_primitives.py", "r")
    except IOError:
        print("ZLang Primitives not found")

    prim_funcs = filter(lambda x: (x[0] == "_") or (x == 'init'), dir(zlprim))
        
def import_stdlib():
    print("Processing Standard Library...")
    try:
        stdlib = open("src/zl_standard_library.zl", "r")
    except IOError:
        print("ZLang Standard Library not found")

    for line in stdlib:
        print(line[:-1]) # trim off newlines

