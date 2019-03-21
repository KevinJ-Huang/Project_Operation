import numpy as np
import matplotlib.pyplot as plt


fig = plt.figure()
plt.scatter(8.91,(22.72-22.2)/(23.4-22.2)*12,c='b')
plt.text(8.83,(22.72-22.2)/(23.4-22.2)*12+0.2,'RSGUnet')

plt.scatter(8.96,(23.29-22.2)/(23.4-22.2)*12,c='r')
plt.text(8.91,(23.29-22.2)/(23.4-22.2)*12+0.2,'HPEU')


plt.scatter(0.57,(22.71-22.2)/(23.4-22.2)*12,c='b')
plt.text(0.57,(22.71-22.2)/(23.4-22.2)*12+0.2,'FCN')

plt.scatter(1.52,(22.73-22.2)/(23.4-22.2)*12,c='b')
plt.text(1.52,(22.73-22.2)/(23.4-22.2)*12+0.2,'DPED')


ax = plt.gca()

x = np.arange(0, 11)
# plt.gcf().set_facecolor(np.ones(3))
ax.set_xticks(x)
ax.set_xticklabels(['2200','2000','1800','1600','1400', '1200','1000','800','600','400', '200' ])
# line = np.array([0.05,0.1,0.18,0.25,0.33,0.43,0.55,0.7])
line = np.array([ 0.5])

for j in range(10):
# for i in range(1):
#     plt.axvline(line[i],hold=None,color='black',linestyle="-",linewidth=0.08)

    for i in range(1):
        plt.axvline(j+line[i],hold=None,color='black',linestyle="-",linewidth=0.08)



y = np.arange(0, 13)
ax.set_yticks(y)
ax.set_yticklabels(['22.2','22.3', '22.4', '22.5','22.6','22.7', '22.8',
                    '22.9','23.0','23.1', '23.2','23.3' ,'23.4' ])

# plt.axvline(1,hold=None,color='black',linestyle="-",linewidth=0.2)
# plt.axvline(2,hold=None,color='black',linestyle="-",linewidth=0.2)
ax.grid()
plt.xlabel('Execution time(ms)')
plt.ylabel('PSNR(dB)')
plt.show()
