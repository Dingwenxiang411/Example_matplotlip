import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

a = ["猩球崛起3：终极之战", "敦刻尔克", "蜘蛛侠：英雄归来", "战狼2"]
b_16 = [15746, 312, 4497, 319]
b_15 = [12357, 156, 2045, 168]
b_14 = [2358, 399, 2358, 362]

# 要根据条形的宽度来调节间距
x_14 = list(range(len(a)))
x_15 = [i + 0.2 for i in x_14]
x_16 = [i + 0.2 for i in x_15]
# 调节大小
plt.figure(figsize=(15, 8), dpi=100)
# 调用中文字体
font_ticks = FontProperties(fname=r"C:\windows\fonts\simsun.ttc", size=10)
font_label = FontProperties(fname=r"C:\windows\fonts\simsun.ttc", size=16)
font_title = FontProperties(fname=r"C:\windows\fonts\simsun.ttc", size=20)
# 修改坐标轴和抬头
plt.xlabel("电影名称", fontproperties=font_label)
plt.ylabel("票房（万）", fontproperties=font_label)
plt.title("2017年9月14、15、16号四部电影票房对比情况", fontproperties=font_title)
# 修改坐标轴刻度
plt.xticks(x_15, a, fontproperties=font_ticks)

plt.bar(x_14, b_14, width=0.2, label="9月14日")
plt.bar(x_15, b_15, width=0.2, label="9月15日")
plt.bar(x_16, b_16, width=0.2, label="9月16日")
# 绘制图例
plt.legend(prop=font_ticks)
plt.show()
