import os
from itertools import takewhile


def platform_map():
    if os.name == "nt":
        return "win"
    if os.name == "posix":
        return "linux"
    raise RuntimeError("Could not detect Operating System")


def allnamesequal(name):
    return all(n==name[0] for n in name[1:])


def commonprefix(paths, sep='/'):
    if platform_map() == "win":
        paths = [p.lower() for p in paths]
    # strip trailing separator
    paths = [p.rstrip(sep)]
    bydirectorylevels = zip(*[p.split(sep) for p in paths])
    return sep.join(x[0] for x in takewhile(allnamesequal, bydirectorylevels))
