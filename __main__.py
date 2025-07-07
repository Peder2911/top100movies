import sys
import init
import pick

if __name__ == "__main__":
    match sys.argv[1:]:
        case ("init", *_):
            init.init()
        case ("pick", *_):
            pick.pick()
        case _:
            print("???")
