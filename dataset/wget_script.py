import os
import multiprocessing as mp
import numpy as np

def wget_magic(f):
    cmdstring = 'wget "https://api.seedly.sg/api/v4/product/items/{}/reviews?i={}&per=501"'.format(f, f)
    os.system(cmdstring)
    print(f)
    return 0


# lst = [47, 44, 46, 48, 68, 45, 215, 209, 219, 214, 220, 222]
lst = np.array(range(251)) + 1


pool = mp.Pool(mp.cpu_count())

results = pool.starmap_async(wget_magic, [[j] for j in lst]).get()

pool.close()
