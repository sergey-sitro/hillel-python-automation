from os import path, getcwd
# https://docs.python.org/3/library/os.path.html


dir_path = getcwd()

print(f"path.exists(dir_path) - {path.exists(dir_path)}")
print("---"*20)
print(f"path.basename(dir_path) - {path.basename(dir_path)}")
print("---"*20)
file = path.join(dir_path, "standard_library", "example_os.py")
print(f"path.join(dir_path, \"standard_library\", \"example_os.py\") - {file}")
print("---"*20)
print(f"path.isdir(dir_path) - {path.isdir(dir_path)}")
print("---"*20)
print(f"path.isfile(file) - {path.isfile(file)}")
print("---"*20)
