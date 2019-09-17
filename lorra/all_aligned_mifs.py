# -*- coding: UTF-8 -*-
import os
import shutil
import re
#把mtcnn对齐好的所有按人名文件夹存放的照片，都扔到一个新文件夹里
path = '/mnt/hdd1/lorra/mtcnn_mifs_160'
new_dir = '/mnt/hdd1/lorra/mtcnn_mifs_oned'
dirr = os.listdir(path)
# print dirr,'\n\n'
i=0
for d in dirr:
    source_subf_path = os.path.join(path, d)
    if os.path.isdir(source_subf_path):
        i+=1
        for p in os.listdir(source_subf_path):
            old_path = os.path.join(source_subf_path,p)
            shutil.copy(old_path, new_dir)
print i
