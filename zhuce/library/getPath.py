import os

def get_rootpath():
    rootpath = os.path.dirname(os.path.abspath(__file__))
    rootpath = rootpath[0:rootpath.rfind(os.path.sep)]
    return rootpath

def get_path(filename):
    rootpath = get_rootpath()
    path = os.path.join(rootpath,'data',filename)
    return path

def get_screenshot():
    rootpath = get_rootpath()
    path = os.path.join(rootpath,'screenshots')
    return path


