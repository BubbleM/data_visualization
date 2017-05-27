import matplotlib.pyplot as plt


x_values = list(range(1,1001))
y_values = [x**2 for x in x_values] # 取x的平方
# scatter() 传入一对x和y坐标,在指定为只绘制一个点
# @param s 设置绘图时使用的点的尺寸
# plt.scatter(2,4,s=200)

# x_values = [1,2,3,4,5]
# y_values = [1,4,9,16,25]
# plt.scatter(x_values,y_values,s=100) # 绘制一系列点
# @param edgecolor='none' 删除数据点的轮廓  matplotlib默认点为蓝色点和黑色轮廓
# @param c 设置数据点颜色 可设置为一个元组，包含三个0～1之间的小数值，分别表红、绿、蓝的分量
# plt.scatter(x_values,y_values,c=(0,0,0.8),edgecolor='none',s=40)

# 将参数c设置为一个y值列表 并使用参数cmap告知pyplot使用哪个颜色映射 将y值较小的映射为浅蓝色，将y值较大的显示为深蓝色
plt.scatter(x_values,y_values,c=y_values,cmap=plt.cm.Blues,edgecolor='none',s=40)


# 设置图表标题并给坐标轴加上标签
plt.title("Square Numbers",fontsize=24)
plt.xlabel("Value",fontsize=14)
plt.ylabel("Square of Value",fontsize=14)

# 设置刻度标记的大小
plt.tick_params(axis="both",which='major',labelsize=14)

# 设置每个坐标轴的取值范围
plt.axis([0,1100,0,1100000])

# plt.show()

# 让程序自动将图表保存到文件中
# @param 实参1 指定要以什么样的文件名保存图表  文件将存储在当前py文件所在目录下
# @param 实参2 指定将图表多余的空白区域裁剪掉  如果要保留空白区域，可省略该参数
plt.savefig('squares_plot.png',bbox_inches='tight')