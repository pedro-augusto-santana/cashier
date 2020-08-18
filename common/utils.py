# utils.py

# TODO
# - ADD CUSTOM ERROR PRINTS

def error (msg: str)-> None:
    print(f"\033[1;31m{msg}\033[0m")

def info (msg: str)-> None:
    print(f"\033[1m{msg}\033[0m")