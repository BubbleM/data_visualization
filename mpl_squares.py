# 模块pyplot包含了很多用于生成图表的函数
import matplotlib.pyplot as plt

input_values = [1,2,3,4,5] 
squares = [1,4,9,16,25]
# plot()函数尝试根据这些数字绘制出有意义的图形
# @param linewidth 绘制的线条的粗细
plt.plot(input_values,squares,linewidth=5)

# 设置图表标题，并给坐标轴加上标签
# @param fontsize 图表中文字的大小
plt.title("Square Numbers",fontsize=24)
plt.xlabel("Value",fontsize=14)
plt.ylabel("Square of Value",fontsize=14)

# 设置刻度标记的大小
# @param axis="both" 将影响x轴和y轴上的刻度
# @param labelsize 将刻度标记的字号设置为14
plt.tick_params(axis="both",labelsize=14)

plt.show() # 打开matplotlib查看器,并显示会只的图形

