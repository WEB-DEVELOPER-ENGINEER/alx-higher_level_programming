#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    import re
    for entry in dir(hidden_4):
        if re.search('__.+', entry):
            continue
        else:
            print(entry)
