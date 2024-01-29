import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl

mpl.use("module://matplotlib_pyodide.wasm_backend")

# 创建一个简单的数据集  
x = np.linspace(0, 10, 100)  
y = np.sin(x)  
  
# 创建一个图形和轴对象  
fig, ax = plt.subplots(figsize=(5, 2.5), layout='constrained')
  
# 绘制数据  
ax.plot(x, y)  
  
# 设置x轴刻度和标签  
ax.set_xticks([0, 2.5, 5, 7.5, 10])  
ax.set_xticklabels(['0', '2.5', '5', '7.5', '10'])  
  
# 设置y轴刻度和标签  
ax.set_yticks([-1, 0, 1])  
ax.set_yticklabels(['-1', '0', '1'])  
  
# 显示图形  
plt.show()
