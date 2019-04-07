import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

x_1 = range(1, 32)
x_2 = range(51, 82)
y_1 = [11, 17, 16, 11, 12, 11, 12, 6, 6, 7, 8, 9, 12, 15, 14,
       17, 18, 21, 16, 17, 20, 14, 15, 15, 15, 19, 21, 22, 22, 22, 23]
y_2 = [26, 26, 28, 19, 21, 17, 16, 19, 18, 20, 20, 19, 22, 23, 17,
       20, 21, 20, 22, 15, 11, 15, 5, 13, 17, 10, 11, 13, 12, 13, 6]
plt.figure(figsize=(10, 8), dpi=100)
font_ticks = FontProperties(fname=r"C:\windows\fonts\simsun.ttc", size=14)
font_label = FontProperties(fname=r"C:\windows\fonts\simsun.ttc", size=16)
font_title = FontProperties(fname=r"C:\windows\fonts\simsun.ttc", size=20)
plt.scatter(x_1, y_1, label="3月")
plt.scatter(x_2, y_2, label="10月")
# 调整轴的刻度，由于xlabel的第一变量只能传递一个变量，所以下面的两个向量相加至关重要
_x = list(x_1) + list(x_2)
_xtick_labels = ["3月{}日".format(i) for i in x_1]
_xtick_labels += ["10月{}日".format(i-50) for i in x_2]
plt.xticks(_x[::3], _xtick_labels[::3], rotation=45, fontproperties=font_ticks)
plt.xlabel("日期", fontproperties=font_label)
plt.ylabel("温度（℃）", fontproperties=font_label)
plt.title("3月和10月每天的温度情况", fontproperties=font_title)
plt.legend(prop=font_ticks)
plt.show()
