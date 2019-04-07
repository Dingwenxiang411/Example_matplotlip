# 这里的as仅仅是为了方便书写pyplot的一个代号
from matplotlib import pyplot as plt

fig = plt.figure(figsize=(10, 8), dpi=80)

x = range(2, 26, 2)
y = [15, 13, 14.5, 17, 20, 25, 26, 26, 27, 22, 18, 15]

plt.plot(x, y)
# 可以实现用x向量中的值来表示x轴的刻度
plt.xticks(x)
# 可以实现每隔1来绘制x轴的刻度
# plt.xticks(range(2, 26))
# 可以实现每隔0.5来绘制x轴的刻度，因为range的步长要求是整数
# _xtick_labels = [i/2 for i in range(4, 49)]
# plt.xticks(_xtick_labels)
plt.savefig("./图像1.svg")
plt.show()



# # matplotlib inline
# #
# import matplotlib.pyplot as plt
# import numpy as np
#
# x = np.arange(9)
# y = np.sin(x)
# z = np.cos(x)
# # marker数据点样式，linewidth线宽，linestyle线型样式，color颜色
# plt.plot(x, y, marker="*", linewidth=3, linestyle="--", color="orange")
# plt.plot(x, z)
# plt.title("matplotlib")
# plt.xlabel("height")
# plt.ylabel("width")
# # 设置图例
# plt.legend(["Y","Z"], loc="upper right")
# plt.grid(True)
# plt.show()
