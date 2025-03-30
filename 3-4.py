import matplotlib.pyplot as plt
import numpy as np
from matplotlib import rcParams

# 设置中文字体
rcParams['font.sans-serif'] = ['SimHei']  # 使用黑体
rcParams['axes.unicode_minus'] = False  # 正确显示负号

# 数据
path_lengths = [2, 3, 4, 5]  # 路径最大长度
hits1 = [25, 30, 40, 45]    # Hits@1 数据
hits3 = [27, 36, 41, 43]    # Hits@3 数据
hits10 = [30, 47, 45, 44]   # Hits@10 数据
mrr = [28, 38, 41, 39]      # MRR 数据

# 创建子图
fig, axes = plt.subplots(1, 4, figsize=(15, 4))

# 子图 (a) Hits@1
axes[0].bar(path_lengths, hits1, color='#FFE4B5', width=0.6)
axes[0].set_title('Hits@1 (%)')
axes[0].set_xlabel('路径最大长度')
axes[0].set_ylabel('Hits@1 (%)')
axes[0].set_ylim(0, 50)
axes[0].text(0.5, -0.1, '(a)', transform=axes[0].transAxes, fontsize=12, ha='center')

# 子图 (b) Hits@3
axes[1].bar(path_lengths, hits3, color='#9BCD9B', width=0.6)
axes[1].set_title('Hits@3 (%)')
axes[1].set_xlabel('路径最大长度')
axes[1].set_ylabel('Hits@3 (%)')
axes[1].set_ylim(0, 50)
axes[1].text(0.5, -0.1, '(b)', transform=axes[1].transAxes, fontsize=12, ha='center')

# 子图 (c) Hits@10
axes[2].bar(path_lengths, hits10, color='#87CEFA', width=0.6)
axes[2].set_title('Hits@10 (%)')
axes[2].set_xlabel('路径最大长度')
axes[2].set_ylabel('Hits@10 (%)')
axes[2].set_ylim(0, 50)
axes[2].text(0.5, -0.1, '(c)', transform=axes[2].transAxes, fontsize=12, ha='center')

# 子图 (d) MRR
axes[3].bar(path_lengths, mrr, color='#CD5555', width=0.6)
axes[3].set_title('MRR (%)')
axes[3].set_xlabel('路径最大长度')
axes[3].set_ylabel('MRR (%)')
axes[3].set_ylim(0, 50)
axes[3].text(0.5, -0.1, '(d)', transform=axes[3].transAxes, fontsize=12, ha='center')

# 调整布局，增加子图之间的间距
plt.tight_layout(pad=3.0)  # 增加 pad 参数
plt.show()