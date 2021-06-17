from pathlib import Path

# absolute path - starts from the root of the hard disk
# /usr/local/bin/...
# relative path -
# ./folder/filename.py

path = Path("package_example")
print(path.exists())  # True if the file path exists, False if it does not.

# make a new directory
path2 = Path("example_path2")
path2.mkdir()

# delete a directrory
path2.rmdir()

# list all python files
path4 = Path()
for file in path4.glob('*.py'):
    print(file)
