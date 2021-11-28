import os

parent_folder = 'my_project'
my_dirs = ['settings', 'mainapp', 'adminapp', 'authapp']
x = [os.makedirs(os.path.join(parent_folder, i))
     for i in my_dirs
     if not os.path.exists(os.path.join(parent_folder, i))]
