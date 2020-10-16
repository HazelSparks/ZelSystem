import zl_environment as zlenv
import zl_primitives as zlprim
import zl_runtime as zlrt

init_string = "Initializing..."
mainfunc_string = "Entering main loop..."

def init():
    # Import and process configs, setup namespace in environment.
    print(init_string)
    zlprim.init()
    zlenv.init()
    zlrt.init()
    
def main():
    # Hand over execution to the environment and the runtime
    print(mainfunc_string)
    
if __name__ == "__main__":
    init()
    main()

