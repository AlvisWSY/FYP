import pandas as pd
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix


# 读取数据
def load_data(path):
    return pd.read_csv(path, header=None)

# 加载 internal 和 noise 数据
internal_data = load_data('/media/mldadmin/home/s123mdg34_04/WangShengyuan/FYP/testdata/internal/waveform.csv')
noise_data = load_data('/media/mldadmin/home/s123mdg34_04/WangShengyuan/FYP/testdata/noise/waveform.csv')

# 创建标签
internal_data['label'] = 0
noise_data['label'] = 1

# 合并数据集
data = pd.concat([internal_data, noise_data])

# 分割特征和标签
X = data.drop('label', axis=1)
y = data['label']

# 划分训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 应用 LDA
lda = LDA(n_components=1)
X_train_lda = lda.fit_transform(X_train, y_train)
X_test_lda = lda.transform(X_test)

# 进行预测
y_pred = lda.predict(X_test)

# 展示结果
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))
