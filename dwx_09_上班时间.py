# 这是一组已经经过统计的数据，是不适画直方图的,这里用条形图近似代替
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

interval = [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 60, 90]
width = [5, 5, 5, 5, 5, 5, 5, 5, 5, 15, 30, 60]
quantity = [836, 2737, 3723, 3926, 3596, 1438, 3273, 642, 824, 613, 215, 47]

# 这里的interval表示每个范围内的开始值，width表示间距
# 也就是结束值等于interval+width
plt.figure(figsize=(20, 8), dpi=80)
# 作图,width=1可以使条形图连接在一起
plt.bar(range(len(quantity)), quantity, width=1)
# 设置x轴的刻度，i-0.5是为了将图像左移，range+1是为了显示末尾刻度
_x = [i-0.5 for i in range(len(quantity)+1)]
# 插入一个列表到interval中
_xtick_labels = interval + [150]
# 这个方法就类似于前面的用字符串对应数字一样
plt.xticks(_x, _xtick_labels)
# 调用中文字体
font_ticks = FontProperties(fname=r"C:\windows\fonts\simsun.ttc", size=10)
font_label = FontProperties(fname=r"C:\windows\fonts\simsun.ttc", size=16)
font_title = FontProperties(fname=r"C:\windows\fonts\simsun.ttc", size=20)
# 修改坐标轴和抬头
plt.xlabel("到公司时长（分钟）", fontproperties=font_label)
plt.ylabel("数量（人）", fontproperties=font_label)
plt.title("美国部分人去上班所花费的时间", fontproperties=font_title)
plt.grid()
plt.show()
