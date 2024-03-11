import pandas as pd
import matplotlib.pyplot as plt

# 读取CSV文件并存储数据在DataFrame中
data = pd.read_csv('/media/mldadmin/home/s123mdg34_04/WangShengyuan/FYP/test/Results/results_lr0.001.csv')

# 创建第一张图，显示train_acc和test_acc
plt.figure(1)
plt.plot(data['epoch'], data['train_acc'], label='Train Accuracy')
plt.plot(data['epoch'], data['test_acc'], label='Test Accuracy')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.title('Accuracy vs Epoch')
plt.legend()
plt.savefig('accuracy_lr0.001.png')

# 创建第二张图，显示train_loss和test_loss
plt.figure(2)
plt.plot(data['epoch'], data['train_loss'], label='Train Loss')
plt.plot(data['epoch'], data['test_loss'], label='Test Loss')
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.title('Loss vs Epoch')
plt.legend()
plt.savefig('loss_lr0.001.png')

# 显示图形
