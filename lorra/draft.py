import numpy as np
def read_pairs(pairs_filename):
    pairs = []
    with open(pairs_filename, 'r') as f:

        for line in f.readlines()[1:]:
            print(line)
            pair = line.strip().split()
            print('--',pair)
            pairs.append(pair)
    return np.array(pairs)

read_pairs('ab_pairs_428.txt')