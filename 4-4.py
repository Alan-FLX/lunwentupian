import matplotlib.pyplot as plt
import numpy as np

# 数据
epochs = np.arange(0, 20, 1)  # 训练轮数

# Hits@1 数据
Llama_MIKGR_hits1 = [27.1, 28.5, 28.9, 29.1, 29.3, 29.3, 29.2, 29.1, 29.3, 29.3, 29.2, 29.3, 29.4, 29.3, 29.4, 29.2, 29.3, 29.3, 29.4, 29.2]
HI_MIKGR_hits1 = [26.2, 26.8, 27.7, 26.8, 27.7, 28.1, 27.5, 27.2, 27.4, 27.7, 27.8, 28.0, 27.8, 27.9, 28.0, 27.9, 27.8, 28.0, 27.8, 28.0]

# Hits@3 数据
Llama_MIKGR_hits3 = [39.1, 40.5, 41.0, 41.4, 41.9, 41.8, 42.3, 42.1, 42.2, 42.3, 42.2, 42.4, 42.5, 42.3, 42.1, 42.2, 42.2, 42.0, 42.3, 42.0]
HI_MIKGR_hits3 = [36.8, 37.7, 38.2, 38.6, 39.1, 39.6, 40.1, 39.9, 39.7, 40.1, 40.4, 39.6, 39.3, 39.4, 39.2, 39.2, 39.2, 39.0, 39.1, 39.1]

# Hits@10 数据
Llama_MIKGR_hits10 = [50.4, 51.8, 52.6, 53.0, 53.2, 53.2, 53.3, 53.1, 53.3, 53.2, 53.1, 53.2, 53.1, 53.2, 53.3, 53.2, 53.2, 53.2, 53.1, 53.2]
HI_MIKGR_hits10 = [49.1, 49.4, 49.1, 49.7, 50.0, 50.6, 51.0, 50.7, 50.8, 51.0, 50.7, 50.9, 50.7, 50.8, 50.7, 50.8, 50.9, 50.8, 50.9, 50.8]

# MRR 数据
Llama_MIKGR_MRR = [36.2, 36.8, 38.0, 38.5, 38.7, 38.7, 38.9, 38.8, 38.9, 39.0, 38.9, 38.8, 38.9, 38.8, 38.9, 39.1, 38.9, 38.9, 38.8, 38.9]
HI_MIKGR_MRR = [34.9, 35.1, 35.6, 36.3, 36.4, 37.0, 36.2, 36.0, 35.5, 35.9, 36.1, 36.7, 36.2, 36.4, 36.2, 36.4, 36.3, 36.2, 36.4, 36.5]

# 创建子图
fig, axes = plt.subplots(2, 2, figsize=(12, 8))

# 子图 (a) Hits@1
axes[0, 0].plot(epochs, Llama_MIKGR_hits1, '#9BCD9B', linestyle='-', label='Llama-MIKGR', marker='o')
axes[0, 0].plot(epochs, HI_MIKGR_hits1, '#87CEFA', linestyle='--', label='HI-MIKGR', marker='s')
axes[0, 0].set_title('Hits@1 (%)')
axes[0, 0].set_xlabel('Epochs\n(a)')
axes[0, 0].set_ylabel('Hits@1 (%)')
axes[0, 0].legend(loc='upper left')
axes[0, 0].grid(True)

# 子图 (b) Hits@3
axes[0, 1].plot(epochs, Llama_MIKGR_hits3, '#9BCD9B', linestyle='-',label='Llama-MIKGR', marker='o')
axes[0, 1].plot(epochs, HI_MIKGR_hits3, '#87CEFA', linestyle='--',label='HI-MIKGR', marker='s')
axes[0, 1].set_title('Hits@3 (%)')
axes[0, 1].set_xlabel('Epochs\n(b)')
axes[0, 1].set_ylabel('Hits@3 (%)')
axes[0, 1].legend(loc='upper left')
axes[0, 1].grid(True)

# 子图 (c) Hits@10
axes[1, 0].plot(epochs, Llama_MIKGR_hits10, '#9BCD9B',linestyle='-', label='Llama-MIKGR', marker='o')
axes[1, 0].plot(epochs, HI_MIKGR_hits10, '#87CEFA',linestyle='--', label='HI-MIKGR', marker='s')
axes[1, 0].set_title('Hits@10 (%)')
axes[1, 0].set_xlabel('Epochs\n(c)')
axes[1, 0].set_ylabel('Hits@10 (%)')
axes[1, 0].legend(loc='upper left')
axes[1, 0].grid(True)

# 子图 (d) MRR
axes[1, 1].plot(epochs, Llama_MIKGR_MRR, '#9BCD9B',linestyle='-', label='Llama-MIKGR', marker='o')
axes[1, 1].plot(epochs, HI_MIKGR_MRR, '#87CEFA', linestyle='--',label='HI-MIKGR', marker='s')
axes[1, 1].set_title('MRR (%)')
axes[1, 1].set_xlabel('Epochs\n(d)')
axes[1, 1].set_ylabel('MRR (%)')
axes[1, 1].legend(loc='upper left')
axes[1, 1].grid(True)

# 调整布局
plt.tight_layout()
plt.show()