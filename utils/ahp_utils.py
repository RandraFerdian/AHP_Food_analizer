import numpy as np

def calc_norm(M):
    if M.ndim == 1:
        return M / np.sum(M)
    else:
        return M / np.sum(M, axis=0)

