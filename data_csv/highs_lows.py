import csv
from matplotlib import pyplot as plt
from datetime import datetime 

filename = 'sitka_weather_07-2014.csv'
# 打开文件　并将文件对象存储在f中
with open(filename) as f:
	# 创建一个与该文件相关联的阅读器对象reader
	reader = csv.reader(f)
	# csv模块的next()调用它并将阅读器对象传递给它，返回文件的下一行
	# header_row包含与天气相关的文件头
	header_row = next(reader)
	
	# print(header_row)
	# 对列表调用了enumerate()来获取每个元素的索引及其值
	# 日期和最高气温分别存储在第０列和第１列
	# for index,column_header in enumerate(header_row):
	# 	print(index,column_header)

	dates,highs = [],[]
	# 遍历文件中除了文件头剩下的每一行
	# 阅读器对象从其停留的地方继续往下读取csv文件，每次都自动返回当前所处位置的下一行
	# 由于我们已经读取了文件头　这个循环从第二行开始
	for row in reader:
		# print(row)
		high = int(row[1]) # 将字符串转换成数字
		highs.append(high) # 提取每天的最高气温
		current_date = datetime.strptime(row[0],"%Y-%m-%d")
		dates.append(current_date)# 日期信息
	# print(highs)


# 根据数据绘制图形
fig = plt.figure(dpi=128,figsize=(10,6))
plt.plot(dates,highs,c='red')
plt.title("Daily high temperstures,July 2014",fontsize=24)
plt.xlabel('',fontsize=16)
fig.autofmt_xdate() # 将日期倾斜显示，以免彼此重叠
plt.ylabel("Temperature(F)",fontsize=16)
plt.tick_params(axis='both',which='major',labelsize=16)
plt.show()
