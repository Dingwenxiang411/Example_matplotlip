import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
import random
x = range(0, 120)
y = [random.randint(20, 35) for i in range(120)]
plt.figure(figsize=(10, 8), dpi=100)
plt.plot(x, y)
# plt.xticks(x[::10])

# 使中文字体得以显示，注意这里的"r"不要遗漏
# 这里使用的是win自带的字体宋体，字号14.16.20
font_ticks = FontProperties(fname=r"C:\windows\fonts\simsun.ttc", size=14)
font_label = FontProperties(fname=r"C:\windows\fonts\simsun.ttc", size=16)
font_title = FontProperties(fname=r"C:\windows\fonts\simsun.ttc", size=20)
# 进一步调整x轴的刻度，把数值型数据对应到字符串数据上
_x_ticks = ["10点{}分".format(i) for i in x if i < 60]
_x_ticks += ["11点{}分".format(i-60) for i in x if i > 60]
# 列表x中的数据必须和_x_ticks上的数据意义对应，rotation让字符串旋转
plt.xticks(x[::5], _x_ticks[::5], rotation=45, fontproperties=font_ticks)
plt.xlabel("时间", fontproperties=font_label)
plt.ylabel("温度（℃）", fontproperties=font_label)
plt.title("10点到12点每分钟的温度变化情况", fontproperties=font_title)
plt.show()
