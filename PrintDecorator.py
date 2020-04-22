import sys

def decorator(f):
    def wrapper(*args, **kwargs):
        s = sys.argv[0]
        if s[:2] == "./":
            s = s[2:]

        return f("["+s+"]", *args, **kwargs)
    return wrapper
