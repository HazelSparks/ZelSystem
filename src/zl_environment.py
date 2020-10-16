namespace = {}

def init():
    # Setup namespace, and import primitives
    print("Initialized ZLang environment")
    import_stdlib()
    

def import_stdlib():
    print("Processing Standard Library...")
    try:
        stdlib = open("src/zl_standard_library.zl", "r")
    except IOError:
        print("ZLang Standard Library not found")

    for line in stdlib:
        print(line[:-1]) # trim off newlines
