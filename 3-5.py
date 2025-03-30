import matplotlib.pyplot as plt
import numpy as np
from matplotlib import rcParams

# ================== 整体字体配置 ==================
rcParams['font.sans-serif'] = ['SimHei']  # 中文字体
rcParams['axes.unicode_minus'] = False    # 正确显示负号
plt.rcParams.update({'font.size': 20})    # 全局字体调大一号

# ================== 图像布局配置 ==================
fig, axes = plt.subplots(2, 2, figsize=(15, 10))  # 改成2x2布局
plt.subplots_adjust(hspace=0.3, wspace=0.25)      # 控制行列间距

# ================== 数据准备 ==================
path_lengths = [2, 3, 4, 5]
hits1 = [25, 40, 35, 38]  # 修改数值，路径长度3时效果最好
hits3 = [27, 45, 40, 39]
hits10 = [30, 47, 42, 40]
mrr = [28, 42, 38, 36]

# ================== 子图逻辑 ==================
def plot_subplot(ax, data, title, color, label_prefix):
    bars = ax.bar(path_lengths, data, color=color, width=0.6)
    ax.set_title(title, fontsize=22)                    # 标题字号+2
    ax.set_xlabel('路径最大长度', fontsize=18)           # X轴标签字号
    ax.set_ylabel(f'(%)', fontsize=20)               # Y轴标签字号
    ax.set_ylim(0, 50)
    ax.tick_params(axis='both', labelsize=16)           # 刻度字号
    # 添加(a)(b)标识
    ax.text(0.5, -0.22, f'({label_prefix.lower()})',    # 调整位置防止重叠
            transform=ax.transAxes,
            fontsize=20,
            ha='center')

# 顺序为：[左上, 右上, 左下, 右下]
plot_subplot(axes[0][0], hits1, 'Hits@1', '#FFE4B5', 'a')
plot_subplot(axes[0][1], hits3, 'Hits@3', '#9BCD9B', 'b')
plot_subplot(axes[1][0], hits10, 'Hits@10', '#87CEFA', 'c')
plot_subplot(axes[1][1], mrr, 'MRR', '#CD5555', 'd')


# 调整布局，缩短底部图例与图表的距离
plt.tight_layout()
plt.subplots_adjust(bottom=0.15)  # 减少底部空白区域
plt.show()