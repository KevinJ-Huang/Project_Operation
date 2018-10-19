import os

root = 'Expert_C/'
lists = os.listdir(root)
lists.sort()
i = 0
for file in lists :
    i+=1
    if i>=5000:
        break
    if i>=100 and i<1000:
        file.split('-')
        if file[1:5]!= '0'+str(i):
            print(i)
            i+=1

    if i>=1000 and i<5000:
        file.split('-')
        if file[1:5]!= str(i):
            print(i)
            i+=1
