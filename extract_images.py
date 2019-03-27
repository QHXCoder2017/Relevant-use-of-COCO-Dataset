import os
import shutil
import time

# 将文件夹中出现的txt中的文件名的图片移动到另一个文件夹
time1 = time.time()
filename = "path\\filename.txt"
rootdir = "path\\foldername"
dstdir = "path\\foldername"
imgname = []

for line in open(filename, 'r'):  # txt数据为一行一个，用换行符分隔
    imgname.append(line.split('.')[0])

lst = os.listdir(rootdir)  # 列出文件夹下所有的目录与文件
for i in range(0, len(lst)):
    path = os.path.join(rootdir, lst[i])
    name = path[-16:-4]  # 切出没有后缀的图片名字
    for j in range(0, len(imgname)):
        if imgname[j] == name:
            shutil.copy(path, dstdir)

time2 = time.time()
print('time:', time2 - time1)
print('well done!')

time1 = time.time()
filename = "path\\filename.txt"
rootdir = "path\\foldername"
dstdir = "path\\foldername"

# with open(filename, 'r') as file_to_read:  # txt数据在一行以空格符分隔
#     while True:
#         lines = file_to_read.readline()
#         if not lines:
#             break
#         imgname = [str(i) for i in lines.split()]  # 将txt中的图片名存放到list中
#
# lst = os.listdir(rootdir)  # 列出文件夹下所有的目录与文件
# for i in range(0, len(lst)):
#     path = os.path.join(rootdir, lst[i])
#     name = path[-16:-4]  # 切出没有后缀的图片名字
#     for j in range(0, len(imgname)):
#         if imgname[j] == name:
#             shutil.copy(path, dstdir)
#
# time2 = time.time()
# print('time:', time2 - time1)
# print('well done!')
