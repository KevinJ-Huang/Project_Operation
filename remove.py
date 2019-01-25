import os

path = 'iphone/'
i = 0
for file in os.listdir(path):
    if not os.path.exists('validation_data_iphone/'+file[:-3]+'png'):
        os.remove('iphone/'+file[:-3]+'jpg')
        os.remove('canon/' + file[:-3] + 'jpg')
        i+=1

print(i)
