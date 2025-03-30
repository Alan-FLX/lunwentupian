import matplotlib.pyplot as plt
import numpy as np

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei']  # 使用黑体
plt.rcParams['axes.unicode_minus'] = False  # 显示负号

# 示例数据
lambda_values = np.linspace(0.1, 0.9, 9)  # X轴从0.1到0.9，生成10个值
dev_set_hits = np.array([0.375, 0.380, 0.378, 0.387, 0.384,  0.382, 0.389, 0.379, 0.376])  # Y轴数据

# 创建图表
plt.figure(figsize=(6, 4))
plt.plot(lambda_values, dev_set_hits, marker='s', color='orange', linestyle='-', markersize=7)

# 设置标题和标签
plt.xlabel(r'$\lambda$', fontsize=12)
plt.ylabel('dev set hits@3', fontsize=12)

# 显示网格
plt.grid(True)
plt.show()

