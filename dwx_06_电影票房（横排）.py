import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

# 对于一些名字过长可以预先加上换行符，以防止坐标轴错位
a = ["战狼2", "速度与激情8", "功夫瑜伽", "西游伏妖篇", "变形金刚5：最后的骑士", "摔跤吧！爸爸",
     "加勒比海盗5：死无对证", "金刚：骷髅岛", "极限特工：终极回归", "生化危机6：终章", "乘风破浪",
     "神偷奶爸3", "智取威虎山", "大闹天竺", "金刚狼3：殊死一战", "蜘蛛侠：英雄归来", "悟空传", "银河护卫队2", "情圣", "新木乃伊"]
b = [56.01, 26.94, 17.53, 16.49, 15.45, 12.96, 11.8, 11.61, 11.28, 11.12, 10.49,
     10.3, 8.75, 7.55, 7.32, 6.99, 6.88, 6.86, 6.58, 6.23]
# 调节绘图大小和分辨率，这句代码一定要在plt.bar前面，不然会出现两张图
plt.figure(figsize=(20, 15), dpi=100)
# 调用中文字体
font_ticks = FontProperties(fname=r"C:\windows\fonts\simsun.ttc", size=10)
font_label = FontProperties(fname=r"C:\windows\fonts\simsun.ttc", size=16)
font_title = FontProperties(fname=r"C:\windows\fonts\simsun.ttc", size=20)
# 修改坐标轴刻度
plt.yticks(range(len(a)), a, fontproperties=font_ticks)
plt.xticks(range(0, 60, 5))
# 修改坐标轴和抬头
plt.ylabel("电影名称", fontproperties=font_label)
plt.xlabel("票房（亿）", fontproperties=font_label)
plt.title("2017年电影票房情况", fontproperties=font_title)
# x轴数据不能直接传入字符串，所以用数字代替
# width可以调节条形的宽度
plt.barh(range(len(a)), b, height=0.3, color='r')
# 绘制网格，只显示x轴的网格
plt.grid(axis="x")
# 保存图像
plt.savefig("./电影票房（横排）.png")
# 绘图
plt.show()
