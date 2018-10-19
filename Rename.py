import os

path = 'output/'
lists = os.listdir(path)
lists.sort()
i = 0
for file in lists :
    file = file
    os.rename(os.path.join(path, file), os.path.join(path, file[0:5] + ".jpg"))
