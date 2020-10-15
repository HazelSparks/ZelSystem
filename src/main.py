import zl_environment
import zl_primitives
import zl_runtime

init_string = "Initializing..."
mainfunc_string = "Entering main loop..."

def init():
    # Import and process configs, setup namespace in environment.
    print(init_string)
    
def main():
    # Hand over execution to the environment and the runtime
    print(mainfunc_string)
    
if __name__ == "__main__":
    init()
    main()

