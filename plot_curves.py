from matplotlib import pyplot as plt
import numpy as np

plt.figure()
plt.plot()
y = np.arange(0, 11)
ax = plt.gca()
ax.set_yticks(y)
ax.set_yticklabels(['21.4','21.6', '21.8', '22.0','22.2','22.4', '22.6',
                    '22.8','23.0','23.2', '23.4' ])
x = np.arange(0, 5)
ax.set_xticks(x)
ax.set_xticklabels(['0.125','0.25','0.5','1','2'])

x_1 = np.array([0,1,2,3,4])
y_1 = np.array([21.45,21.78,22.47,22.67,22.92])
y_1 = (y_1-21.4)/(23.4-21.4)*10

plt.scatter(x_1[0],y_1[0],c='b')
plt.text(x_1[0]-0.23,y_1[0]+0.38,'124ms')
plt.scatter(x_1[1],y_1[1],c='b')
plt.text(x_1[1]-0.4,y_1[1]+0.24,'160ms')
plt.scatter(x_1[2],y_1[2],c='b')
plt.text(x_1[2]-0.2,y_1[2]+0.27,'223ms')
plt.scatter(x_1[3],y_1[3],c='b')
plt.text(x_1[3]-0.2,y_1[3]+0.34,'371ms')
plt.scatter(x_1[4],y_1[4],c='b')
plt.text(x_1[4]-0.36,y_1[4]+0.24,'743ms')

x_2 = np.array([0,1,2,3,4])
y_2 = np.array([22.45,22.71,22.75,23.29,23.24])
y_2 = (y_2-21.4)/(23.4-21.4)*10

plt.scatter(x_2[0],y_2[0],c='r')
plt.text(x_2[0]-0.23,y_2[0]+0.38,'138ms')
plt.scatter(x_1[1],y_2[1],c='r')
plt.text(x_2[1]-0.2,y_2[1]+0.24,'174ms')
plt.scatter(x_1[2],y_2[2],c='r')
plt.text(x_2[2]-0.35,y_2[2]+0.29,'241ms')
plt.scatter(x_1[3],y_2[3],c='r')
plt.text(x_2[3],y_2[3]+0.14,'408ms')
plt.scatter(x_1[4],y_2[4],c='r')
plt.text(x_2[4]-0.36,y_2[4]+0.24,'814ms')


l1, = plt.plot(x_1,y_1)
l2, = plt.plot(x_2,y_2)

plt.xlabel('The number of filters in each layer relative to the original HPEU')
plt.ylabel('PSNR')
plt.legend(handles = [l2, l1,], labels = ['HPEU', 'Baseline'], loc = 'best')
plt.savefig('1.png',dpi = 600)
plt.show()
