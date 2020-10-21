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

    prim_funcs = filter(lambda x: (x[0] == "_"), dir(zlprim))
