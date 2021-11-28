import os
from os.path import relpath

root_dir = 'some_data'

for root, dirs, files in os.walk(root_dir):
    for file in files:

        rel_path = relpath(os.path.join(root, file), root_dir)
        file_size = os.stat(os.path.join(root, file)).st_size
        # print(rel_path)
        print(file_size)

#
# for ext, files in sorted(my_files.items(), key=lambda x: len(x[1]), reverse=True):
#     print(f"{ext}: {len(files)}")

# print(sorted(my_files), sep='\n')

