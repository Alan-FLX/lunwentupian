import matplotlib.pyplot as plt
import numpy as np

# 创建图形和轴
fig, ax = plt.subplots(figsize=(10, 6))

# 绘制实体空间
ax.text(1.5, 8, "Entity Space", fontsize=12, ha='center')
ax.text(1.5, 7.5, "Person", fontsize=10, ha='center', color='purple')
ax.text(1.5, 6.5, "City", fontsize=10, ha='center', color='green')

# 绘制概念空间
ax.text(7.5, 8, "Concept Space", fontsize=12, ha='center')
ax.text(7.5, 7.5, "Person", fontsize=10, ha='center', color='orange')
ax.text(7.5, 6.5, "City", fontsize=10, ha='center', color='gray')

# 绘制实体和概念的点
entities = {
    "Barack Obama": (2, 7),
    "Hawaii": (2, 5)
}
concepts = {
    "c_s": (8, 7),
    "c_t": (8, 5)
}

for name, (x, y) in entities.items():
    ax.scatter(x, y, s=100, label=name)
    ax.text(x, y, name, fontsize=9, ha='center')

for name, (x, y) in concepts.items():
    ax.scatter(x, y, s=100, label=name, color='orange' if name == "c_s" else 'gray')
    ax.text(x, y, name, fontsize=9, ha='center')

# 绘制映射箭头
ax.annotate("M", xy=(3, 7), xytext=(6, 7), arrowprops=dict(arrowstyle="->", color='black'))
ax.annotate("M", xy=(3, 5), xytext=(6, 5), arrowprops=dict(arrowstyle="->", color='black'))

# 绘制关系箭头
ax.annotate("r", xy=(8, 7), xytext=(8, 6), arrowprops=dict(arrowstyle="->", color='black'))

# 设置图形范围和网格
ax.set_xlim(0, 10)
ax.set_ylim(4, 9)
ax.grid(True, linestyle='--', alpha=0.6)

# 添加图例
ax.legend(loc='upper left', fontsize=10)

# 显示图形
plt.title("Entity to Concept Mapping", fontsize=14)
plt.show()