import pandas as pd
import matplotlib.pyplot as plt

# 修正数据维度（模型列表与得分数量匹配）
data = {
    'Model': [
        'DeepSeek-r1-7b', 'Qwen-7b', 'GPT-4o',
        'Llama2-7B', 'LLM+MIKG'
    ],
    # UMLS数据集三元分类准确率（参考格式：参考资料1表3）[^1]
    'Accuracy Score': [256, 233, 248, import matplotlib.pyplot as plt
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
hits1 = [25, 43, 41, 37]  # 修改数值，路径长度3时效果最好
hits3 = [27, 44, 43, 36]
hits10 = [30, 49, 45, 35]
mrr = [28, 46, 40, 37]

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
plt.show()225, 267],
    # Jaccard Similarity指标标准化处理（参考公式：参考资料3式4-7）[^3]
    'Jaccard Similarity': [0.857, 0.860, 0.895, 0.794, 0.927]
}

df = pd.DataFrame(data)

def plot_comparison(df):
    """双标尺对比可视化"""
    fig, ax1 = plt.subplots(figsize=(10, 6))

    # 左侧主坐标轴（0-300范围）
    bars = ax1.bar(df['Model'], df['Accuracy Score'],
                   width=0.4, align='center',
                   color='#207f4c', label='Accuracy (%)')
    ax1.set_ylim(0, 300)
    ax1.set_ylabel('Accuracy Score (0-300 scale)', color='#207f4c')
    ax1.tick_params(axis='y', labelcolor='#207f4c')

    # 在柱状图上显示数值
    for bar in bars:
        height = bar.get_height()
        ax1.text(bar.get_x() + bar.get_width() / 2., height + 5,
                 f'{int(height)}', ha='center', va='bottom',
                 fontsize=10, color='#207f4c')

    # 右侧次坐标轴（0-1范围）
    ax2 = ax1.twinx()
    line, = ax2.plot(df['Model'], df['Jaccard Similarity'],
                     marker='o', linestyle='--',
                     color='#d62728', label='Jaccard Similarity')
    ax2.set_ylim(0.0, 1.0)
    ax2.set_ylabel('Jaccard Similarity (0.0-1.0 scale)', color='#d62728')
    ax2.tick_params(axis='y', labelcolor='#d62728')

    # 在折线图上显示数值
    for i, (model, score) in enumerate(zip(df['Model'], df['Jaccard Similarity'])):
        ax2.text(i, score + 0.02, f'{score:.3f}', ha='center', va='bottom',
                 fontsize=10, color='#d62728')

    # 图表元数据设置
    plt.title('Model Performance Comparison\n(UMLS Dataset Metrics)', pad=20)
    fig.legend(loc='upper left', bbox_to_anchor=(0.15, 0.85))
    plt.tight_layout()
    plt.savefig('dual_scale_comparison.png', dpi=300)
    plt.show()

# 生成可视化结果
plot_comparison(df)
