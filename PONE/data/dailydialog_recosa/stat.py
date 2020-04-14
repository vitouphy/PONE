import numpy as np
with open('../dailydialog_hred/src-train.txt') as f:
    c = []
    for line in f.readlines():
        c.append(len(line.split()))
    print(np.mean(c))
