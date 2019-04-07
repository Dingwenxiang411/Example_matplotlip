import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

x = range(11, 31)
y_1 = [1, 0, 1, 1, 2, 4, 3, 2, 3, 4, 4, 5, 6, 5, 4, 3, 3, 1, 1, 1]
y_2 = [1, 0, 3, 1, 2, 2, 3, 3, 2, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1]
plt.figure(figsize=(10, 8), dpi=100)
# 生成网格，根据x,y轴的刻度绘制的
# alpha设置的是透明度，越小越透明，0的时候完全透明
plt.grid(alpha=0.4)
font_ticks = FontProperties(fname=r"C:\windows\fonts\simsun.ttc", size=14)
font_label = FontProperties(fname=r"C:\windows\fonts\simsun.ttc", size=16)
font_title = FontProperties(fname=r"C:\windows\fonts\simsun.ttc", size=20)
plt.xticks(x)
plt.plot(x, y_1, label="自己")
plt.plot(x, y_2, label="同桌")
plt.xlabel("年龄（岁）", fontproperties=font_label)
plt.ylabel("数量（个）", fontproperties=font_label)
plt.title("11岁到30岁每年交朋友的数量变化情况", fontproperties=font_title)
# PS:只有在图例中调用中文的时候是用的prop,记得前面label的内容
plt.legend(prop=font_ticks)
# TODO 添加水印

plt.show()
