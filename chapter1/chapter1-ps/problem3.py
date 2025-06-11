import os

# Specify the directory path
directory_path = '/GitHub'  # Current directory; change this to any path you want

try:
    # List all files and directories in the given path
    contents = os.listdir(directory_path)
    
    print(f"Contents of directory '{directory_path}':")
    for item in contents:
        print(item)

except FileNotFoundError:
    print(f"The directory '{directory_path}' does not exist.")
except PermissionError:
    print(f"Permission denied to access '{directory_path}'.")
