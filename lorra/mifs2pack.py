# -*- coding: UTF-8 -*-
import mxnet as mx
from mxnet import ndarray as nd
import argparse
import pickle
import sys
import os
import numpy as np

def read_pairs(pairs_filename):
  pairs = []
  with open(pairs_filename, 'r') as f:
    for line in f.readlines():
      pair = line.strip().split()
      pairs.append(pair)
  return np.array(pairs)

def get_paths(mifs_dir, pairs, file_ext):
  nrof_skipped_pairs = 0
  path_list = []
  issame_list = []
  #pair就是标签中每行的三元素组成的列表
  for pair in pairs:
    # print pair
    p0, p1 = pair[0], pair[1]
    if file_ext not in p0:
      p0 = pair[0].replace(pair[0][-3:], file_ext)
    if file_ext not in p1:
      p1 = pair[1].replace(pair[1][-3:], file_ext)
    path0 = os.path.join(mifs_dir, p0)
    path1 = os.path.join(mifs_dir, p1)
    # print(path0,path1)
    if os.path.exists(path0) and os.path.exists(path1):  # Only add the pair if both paths exist
      path_list += (path0, path1)
      # print path_list
      if pair[2] == '1':
        issame = True
      else:
        issame = False
      issame_list.append(issame)
    else:
      print('not exists', path0, path1)
      nrof_skipped_pairs += 1
    if nrof_skipped_pairs > 0:
      print('Skipped %d image pairs' % nrof_skipped_pairs)
  return path_list, issame_list

parser = argparse.ArgumentParser(description='Package MIFS images')
# general
parser.add_argument('--data-dir', default='/mnt/hdd1/lorra/112_tgt_mifs', help='')
parser.add_argument('--image-size', type=str, default='112,112', help='')
parser.add_argument('--output', default='all_mifs.bin', help='path to save.')
args = parser.parse_args()
mifs_dir = args.data_dir
image_size = [int(x) for x in args.image_size.split(',')]
#pairs是一个二维列表，每个子列表分别是标签的三个元素。
mifs_pairs = read_pairs(os.path.join('all_pairs_856_749.txt'))
mifs_paths, issame_list = get_paths(mifs_dir, mifs_pairs, 'png')
print(len(mifs_paths),len(issame_list))
# print issame_list
mifs_bins = []
i = 0
for path in mifs_paths:
  with open(path, 'rb') as fin:
    _bin = fin.read()
    mifs_bins.append(_bin)
    #img = mx.image.imdecode(_bin)
    #img = nd.transpose(img, axes=(2, 0, 1))
    #lfw_data[i][:] = img
    i+=1
    if i%1000==0:
      print('loading mifs', i)

with open(args.output, 'wb') as f:
  pickle.dump((mifs_bins, issame_list), f, protocol=pickle.HIGHEST_PROTOCOL)

