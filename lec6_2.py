import sys
import pathlib

# pathlib --object oriented filesystem paths

p = pathlib.Path('/etc')
q = p/'ssh'
print(q)
print(q.exists())
print(q.is_dir())

# print all py files somewhere in the current dir
p = pathlib.Path.cwd() # current working directory
for f in p.glob('**/*.py'):
    print(f)


if __name__=="__main__":
    pass
    # print(sys.argv)