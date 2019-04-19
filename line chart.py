import matplotlib.pyplot as plt
import numpy as np

x = np.array([0,
0.1,
0.2,
0.3,
0.4,
0.5,
0.6,
0.7,
0.8,
0.9,
1])
y_t = np.array([61.82,
61.82,
61.82,
61.82,
61.82,
61.82,
61.82,
61.82,
61.82,
61.82,
61.82])
y_s = np.array([60.91,
61.05,
61.21,
61.36,
61.5,
61.63,
61.73,
61.8,
61.87,
61.9,
61.91])
# x_date = [datestr2num(i) for i in data.index]

plt.figure(figsize=(10, 5))
plt.title("CUB 200-2011")
plt.xlabel("KL")
# plt.xticks(rotation=45)
plt.ylabel("NMI score (%)")
plt.xticks(np.arange(0,1,0.1))
plt.yticks(np.arange(60,62,0.1))
plt.plot(x, y_t, '-*', label='ResNet34', linewidth=2)
plt.plot(x, y_s, '-^', label='ResNet18', linewidth=2)
# plt.plot_date(x_date,data['close'],'-',label="收盘价")
# plt.plot_date(x_date,data['high'],'-',color='r',label="最高价")
plt.legend(loc=4)
plt.grid(axis='y',linestyle='--')
plt.gca().spines["top"].set_alpha(0.0)
plt.gca().spines["bottom"].set_alpha(1)
plt.gca().spines["right"].set_alpha(0.0)
plt.gca().spines["left"].set_alpha(1)
plt.show()