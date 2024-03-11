import csv
import matplotlib.pyplot as plt

# 读取CSV文件
csv_file = '/media/mldadmin/home/s123mdg34_04/WangShengyuan/FYP/testdata/internal/waveform.csv'

with open(csv_file, 'r') as file:
    reader = csv.reader(file)
    next(reader)  # 跳过标题行
    for i, row in enumerate(reader, start=1):
        # 将字符串转换为浮点数列表
        waveform = [float(value) for value in row]

        # 绘制波形图
        plt.plot(waveform)
        plt.xlabel('Sample')
        plt.ylabel('Amplitude')
        plt.title(f'Waveform {i}')

        # 保存波形图
        save_path = f'../testdata/data/internal/{i}.png'
        plt.savefig(save_path)
        plt.clf()  # 清除图形

        print(f'Saved waveform {i} as {save_path}')
