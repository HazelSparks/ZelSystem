import zl_environment as zlenv
import zl_primitives as zlprim
import zl_runtime as zlrt

init_string = "Initializing..."
mainfunc_string = "Entering main loop..."
string_test = "(define atom? (lambda (x) (and (not (null? x)) (not (pair? x)))))"

def init():
    # Import and process configs, setup namespace in environment.
    print(list(filter(lambda x: (x[0] != "_") and (x != 'init'), dir(zlprim))))
    print(init_string)
    zlprim.init()
    zlenv.init()
    zlrt.init()
    
def main():
    # Hand over execution to the runtime
    print(mainfunc_string)
    zlrt.main_loop()

if __name__ == "__main__":
    init()
    main()

