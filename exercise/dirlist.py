import os


def dir_find(path, key=None):
    dirs = [x for x in os.listdir('.') if os.path.isdir(x)]
    if(key == None):
        return dirs
    else:
        for d in dirs:
            files = [x for x in os.listdir(d) if os.path.isfile(
                x) and os.path.splitext(x).__contains__(key)]
            for f in files:
                return os.path.pardir(f)


print(dir_find("E:\Administrator\Documents\PythonProjects\LearnPython"))
print(dir_find('E:\Administrator\Documents\PythonProjects\LearnPython', 'test'))
