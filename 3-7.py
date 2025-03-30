import matplotlib.pyplot as plt
import numpy as np

# 数据
epochs = np.arange(0, 20, 1)  # 训练轮数

# Hits@1 数据
ISSS_MIKGR_hits1 = [27.1, 28.4, 28.8, 29.0, 29.2, 29.2, 29.2, 29.1, 29.2, 29.2, 29.1, 29.2, 29.3, 29.2, 29.3, 29.1, 29.2, 29.2, 29.3, 29.1]
LASS_hits1 = [26.2, 26.9, 27.8, 26.9, 27.8, 28.2, 27.6, 27.3, 27.5, 27.8, 27.9, 28.1, 27.9, 28.0, 28.1, 28.0, 27.9, 28.1, 27.9, 28.1]
Path_hits1 = [24.2, 24.6, 24.8, 25.2, 25.3, 25.7, 26.1, 26.1, 26.4, 26.5, 26.4, 26.5, 26.5, 26.6, 26.6, 26.5, 26.5, 26.5, 26.5, 26.5]

# Hits@3 数据
ISSS_MIKGR_hits3 = [39.1, 40.4, 40.9, 41.3, 41.9, 41.7, 42.2, 42.0, 42.1, 42.2, 42.1, 42.3, 42.4, 42.2, 42.0, 42.1, 42.1, 41.9, 42.2, 41.9]
LASS_hits3 = [36.8, 37.8, 38.3, 38.7, 39.2, 39.7, 40.2, 40.0, 39.8, 40.2, 40.5, 39.7, 39.4, 39.5, 39.3, 39.3, 39.3, 39.1, 39.2, 39.2]
Path_hits3 = [34.0, 35.1, 35.7, 36.4, 36.6, 36.5, 36.3, 36.6, 36.8, 36.6, 36.9, 37.0, 36.2, 36.1, 36.6, 36.9, 37.1, 37.0, 37.4, 37.4]

# Hits@10 数据
ISSS_MIKGR_hits10 = [50.4, 51.7, 52.5, 52.9, 53.1, 53.1, 53.2, 53.0, 53.2, 53.1, 53.0, 53.1, 53.0, 53.1, 53.2, 53.1, 53.1, 53.1, 53.0, 53.1]
LASS_hits10 = [48.6, 49.5, 49.2, 49.8, 50.1, 50.7, 51.1, 50.8, 50.9, 51.1, 50.8, 51.0, 50.8, 50.9, 50.8, 50.9, 51.0, 50.9, 51.0, 50.9]
Path_hits10 = [47.3, 47.8, 48.2, 49.3, 49.8, 50.3, 49.3, 49.2, 48.9, 49.1, 48.9, 49.1, 48.9, 49.1, 48.9, 49.1, 49.1, 49.1, 49.1, 49.2]

# MRR 数据
ISSS_MIKGR_MRR = [36.2, 36.9, 38.1, 38.6, 38.8, 38.8, 39.0, 38.9, 39.0, 39.1, 39.0, 38.9, 39.0, 38.9, 39.0, 39.2, 39.0, 39.0, 38.9, 39.0]
LASS_MRR = [34.2, 35.3, 35.8, 36.5, 36.6, 37.3, 36.4, 36.2, 35.6, 36.0, 36.2, 36.9, 36.4, 36.6, 36.4, 36.6, 36.5, 36.4, 36.6, 36.7]
Path_MRR = [32.1, 32.6, 34.0, 34.8, 33.6, 34.6, 34.1, 33.8, 34.6, 34.8, 34.8, 34.9, 34.8, 35.0, 34.8, 34.9, 34.8, 34.8, 34.9, 34.9]

# 创建子图
fig, axes = plt.subplots(2, 2, figsize=(12, 10))  # 调整整体大小
fontsize = 16  # 设置全局字体大小

# 子图 (a) Hits@1
axes[0, 0].plot(epochs, ISSS_MIKGR_hits1, '#9BCD9B', linestyle='-', marker='o')
axes[0, 0].plot(epochs, LASS_hits1, '#87CEFA', linestyle='--', marker='s')
axes[0, 0].plot(epochs, Path_hits1, '#FFE4B5', linestyle='-.', marker='^')
axes[0, 0].set_title('Hits@1 (%)', fontsize=fontsize)
axes[0, 0].set_xlabel('Epochs\n(a)', fontsize=fontsize)
axes[0, 0].set_ylabel('Hits@1 (%)', fontsize=fontsize)
axes[0, 0].grid(True)

# 子图 (b) Hits@3
axes[0, 1].plot(epochs, ISSS_MIKGR_hits3, '#9BCD9B', linestyle='-', marker='o')
axes[0, 1].plot(epochs, LASS_hits3, '#87CEFA', linestyle='--', marker='s')
axes[0, 1].plot(epochs, Path_hits3, '#FFE4B5', linestyle='-.', marker='^')
axes[0, 1].set_title('Hits@3 (%)', fontsize=fontsize)
axes[0, 1].set_xlabel('Epochs\n(b)', fontsize=fontsize)
axes[0, 1].set_ylabel('Hits@3 (%)', fontsize=fontsize)
axes[0, 1].grid(True)

# 子图 (c) Hits@10
axes[1, 0].plot(epochs, ISSS_MIKGR_hits10, '#9BCD9B', linestyle='-', marker='o')
axes[1, 0].plot(epochs, LASS_hits10, '#87CEFA', linestyle='--', marker='s')
axes[1, 0].plot(epochs, Path_hits10, '#FFE4B5', linestyle='-.', marker='^')
axes[1, 0].set_title('Hits@10 (%)', fontsize=fontsize)
axes[1, 0].set_xlabel('Epochs\n(c)', fontsize=fontsize)
axes[1, 0].set_ylabel('Hits@10 (%)', fontsize=fontsize)
axes[1, 0].grid(True)

# 子图 (d) MRR
axes[1, 1].plot(epochs, ISSS_MIKGR_MRR, '#9BCD9B', linestyle='-', marker='o')
axes[1, 1].plot(epochs, LASS_MRR, '#87CEFA', linestyle='--', marker='s')
axes[1, 1].plot(epochs, Path_MRR, '#FFE4B5', linestyle='-.', marker='^')
axes[1, 1].set_title('MRR (%)', fontsize=fontsize)
axes[1, 1].set_xlabel('Epochs\n(d)', fontsize=fontsize)
axes[1, 1].set_ylabel('MRR (%)', fontsize=fontsize)
axes[1, 1].grid(True)

# 统一图例放在底部
fig.legend(['HI-MIKGR', '-Hi', '-Att'], loc='lower center', ncol=3, fontsize=fontsize)

# 调整布局，缩短底部图例与图表的距离
plt.tight_layout()
plt.subplots_adjust(bottom=0.15)  # 减少底部空白区域
plt.show()