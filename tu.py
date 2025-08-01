import pandas as pd
import matplotlib.pyplot as plt

# 加载 Excel 文件
file_path = 'data.xlsx'
df = pd.read_excel(file_path, header=None)

# 获取第一行作为 x 数据
x = df.iloc[0]

# 生成图表
for i in range(1, len(df)):
    # 获取第 i 行作为 y 数据
    y = df.iloc[i]

    # 绘制图表
    plt.figure()
    plt.plot(x, y)
    plt.xlabel('X')
    plt.ylabel(f'Y (Row {i + 1})')
    plt.title(f'Plot for Row {i + 1}')

    # 保存图表为 PNG 文件
    plt.savefig(f'{i}.png')
    plt.close()
