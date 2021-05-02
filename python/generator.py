def mygen(i):
    for i in range(i, 101):
        yield i
        i += 1

for item in mygen(99):
    print(item)

# generators chain
import os 

def generate_filenames():
    for dir_path, dir_names, file_names in os.walk('../'):
        for file_name in file_names:
            if file_name.endswith('.py'):
                yield open(os.path.join(dir_path, file_name))

def cat_files(files):
    for fname in files:
        for line in fname:
            yield line

def grep_lines(lines, pattern=None):
    for line in lines:
        if pattern in line:
            yield line

py_files = generate_filenames()
lines = cat_files(py_files)
grepped_lines = grep_lines(lines, 'bubble')
for line in grepped_lines:
    print(line)