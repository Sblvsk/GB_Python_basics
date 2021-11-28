import os
from os.path import relpath

root_dir = 'some_data'
groups = [10, 100, 1000, 10000, 100000, 1000000]
result = dict.fromkeys(groups, 0)
for root, dirs, files in os.walk(root_dir):
    for file in files:
        rel_path = relpath(os.path.join(root, file), root_dir)
        file_size = os.stat(os.path.join(root, file)).st_size
        to_group = min(filter(lambda x: file_size < x, groups))
        result[to_group] += 1

print(result)