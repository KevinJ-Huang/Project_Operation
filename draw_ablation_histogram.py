import matplotlib.pyplot as plt
import matplotlib
# 设置中文字体和负号正常显示
matplotlib.rcParams['font.sans-serif'] = ['SimHei']
matplotlib.rcParams['axes.unicode_minus'] = False

label_list = ['0.2', '0.4', '0.6', '0.8']    # 横坐标刻度显示值
num_list1 = [32.22,31.64,31.38,31.15]      # 纵坐标值1
num_list2 = [30.69,29.84,29.02,28.16]      # 纵坐标值2
num_list3 = [31.44,28.86,28.79,28.14]      # 纵坐标值2

x = range(len(num_list1))
"""
绘制条形图
left:长条形中点横坐标
height:长条形高度
width:长条形宽度，默认值0.8
label:为后面设置legend准备
"""
rects1 = plt.bar(left=x, height=num_list1, width=0.3, alpha=0.8, color='red', label="ours")
rects2 = plt.bar(left=[i + 0.3 for i in x], height=num_list2, width=0.3, color='green', label="flownet")
rects3 = plt.bar(left=[i + 0.6 for i in x], height=num_list3, width=0.3, color='blue', label="sift")

plt.ylim(25, 35)     # y轴取值范围
plt.ylabel("PSNR(dB)")
"""
设置x轴刻度显示值
参数一：中点坐标
参数二：显示值
"""
plt.xticks([index + 0.2 for index in x], label_list)
plt.xlabel("The disparity of the dataset()")
plt.title("Comparison of different methods in different disparity")
plt.legend()     # 设置题注
# 编辑文本
for rect in rects1:
    height = rect.get_height()
    plt.text(rect.get_x() + rect.get_width() / 2, height+0.5, str(height), ha="center", va="bottom",fontsize=8)
for rect in rects2:
    height = rect.get_height()
    plt.text(rect.get_x() + rect.get_width() / 2, height+0.5, str(height), ha="center", va="bottom",fontsize=8)
for rect in rects3:
    height = rect.get_height()
    plt.text(rect.get_x() + rect.get_width() / 2, height+0.5, str(height), ha="center", va="bottom",fontsize=8)
plt.show()
