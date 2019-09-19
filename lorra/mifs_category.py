# -*- coding: UTF-8 -*-
import os
import shutil
import re

path = '/mnt/hdd1/lorra/MIFS-Uncropped'
new_dir = '/mnt/hdd1/lorra/mifs_cate'
#新建117个文件夹
sort_folder_number = [x for x in range(0,117)]
for number in sort_folder_number:
    s=str(number+1)
    for i in range(3-len(str(number+1))):
        s='0'+s
    new_folder_path = os.path.join(new_dir, s)
    if not os.path.exists(new_folder_path):
        os.makedirs(new_folder_path)

#列出所有图片,按名称形成列表
file_list = os.listdir(path)
print '总文件数量：',len(file_list)
#提取出图片的命名数字，并根据数字决定将问价发往那个文件夹
for i in range(len(file_list)):
    old_file_path = os.path.join(path,file_list[i])
    if os.path.isdir(old_file_path):
        print "Is a dir", old_file_path
        pass
    elif not os.path.exists(old_file_path):
        print "Not exist", old_file_path
        pass
    else:
        s = file_list[i][0:3]
        new_file_path = os.path.join(new_dir,s)
        shutil.copy(old_file_path, new_file_path)

