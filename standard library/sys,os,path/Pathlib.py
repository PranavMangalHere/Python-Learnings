import os
from pathlib import Path

""" 
pathlib provides an object-oriented interface for filesystem paths, replacing string-based path manipulation.

Path objects are lazy — they don’t touch the filesystem until explicitly requested.

The / operator is overloaded to perform safe path joining.
"""

# Build paths inside the project like this: os.path.join(Base_Dir, 'subdir')
# Base_Dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Build paths inside the project like this : Base_Dir/ 'subdir'
# Base_Dir = Path(__file__).resolve().parent.parent

# print(Path.cwd())

# for p in Path().iterdir():
#     print(p)
""" 
os.py
Pathlib.py
sys.py"""

my_dir = Path("sys,os,path")
myfile = Path("Pathlib.py")
# print(my_dir.exists())
# print(myfile.suffix)
# print(myfile.stem)
# print(myfile.absolute().parent)  # .

# newfile = my_dir / "newfile.txt"
# newfile = my_dir.joinpath("newfile.txt")
# print(newfile.exists())

