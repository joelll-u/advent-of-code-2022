class Directory:
    def __init__(self, name, parent = None):
        self.name = name
        self.sub_directories = dict()
        self.files = []
        self.size = 0
        self.parent = parent
    
    def get_size(self):
        return self.size
    
    def add_file(self, file):
        self.files.append(file)
        self.add_size(file.size)
    
    def add_directory(self, directory):
        directory.parent = self
        self.sub_directories[directory.name] = directory
        self.add_size(directory.get_size())
    
    def new_subdirectory(self, name):
        if not name in self.sub_directories:
            new_directory = Directory(name, self)
            self.sub_directories[name] = new_directory
    
    def add_size(self, size):
        self.size += size
        if self.parent:
            self.parent.add_size(size)
    
    def get_subdirectory(self, name):
        if name in self.sub_directories:
            return self.sub_directories[name]
        else:
            self.new_subdirectory(name)
            return self.get_subdirectory(name)

class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size

#part 1
import re

f = open("input.txt", "r")
lines = f.readlines()
f.close()

outer_directory = Directory("\\")
curr_directory = outer_directory

i = 1
while i < len(lines):
    cmd = re.search("\$ (\w+)\s*(\w+|\.+)?", lines[i])
    if cmd.group(1) == "cd":
        if cmd.group(2) == "..":
            curr_directory = curr_directory.parent
        else:
            curr_directory = curr_directory.get_subdirectory(cmd.group(2))
        i += 1
    elif cmd.group(1) == "ls":
        j = i + 1
        while j < len(lines) and lines[j][0] != "$":
            obj = re.search("(dir|\d+) (\w+)", lines[j])
            if obj.group(1) == "dir":
                curr_directory.new_subdirectory(obj.group(2))
            else:
                new_file = File(obj.group(2), int(obj.group(1)))
                curr_directory.add_file(new_file)
            j += 1
        i = j


def sum_small_sizes(directory):
    sum_size = 0
    if directory.get_size() < 100000:
        sum_size = directory.get_size()
    for i in directory.sub_directories.values():
        sum_size += sum_small_sizes(i)
    return sum_size

print(sum_small_sizes(outer_directory))

total_size = 70000000
size_needed = 30000000
size_used = outer_directory.get_size()
size_to_be_freed = size_needed - (total_size - size_used)

def find_dir_to_delete(directory, needed):
    if directory.get_size() < needed:
        return float('inf')
    else:
        min_size = directory.get_size()
        for i in directory.sub_directories.values():
            min_size = min(min_size, find_dir_to_delete(i, needed))
        return min_size

print(find_dir_to_delete(outer_directory, size_to_be_freed))
