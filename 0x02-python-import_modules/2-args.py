#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    if (len(argv) == 1):
        print("0 arguments.")
    elif (len(argv) == 2):
        print("1 argument:")
        print("1:", argv[1])
    else:
        print(len(argv) - 1, "arguments:")
        for i in range(1, len(argv)):
            print("{:d}: {}".format(i, argv[i]))
