# tool used to separate the files in the folder
import os
import shutil

def move_files(path):
    # 创建新的目录
    prpd_path = os.path.join(path, 'prpd')
    waveform_path = os.path.join(path, 'waveform')
    os.makedirs(prpd_path, exist_ok=True)
    os.makedirs(waveform_path, exist_ok=True)

    # 遍历指定路径下的所有文件
    for filename in os.listdir(path):
        # 检查文件名中是否包含'PRPD'或'WAVEFORM'
        if 'PRPD' in filename:
            # 将文件移动到'prpd'目录下
            shutil.move(os.path.join(path, filename), os.path.join(prpd_path, filename))
        elif 'WaveForm' in filename:
            # 将文件移动到'waveform'目录下
            shutil.move(os.path.join(path, filename), os.path.join(waveform_path, filename))

# 使用函数
Path = '/media/mldadmin/home/s123mdg34_04/WangShengyuan/FYP/data/noise'
move_files(Path)
print('Done!')