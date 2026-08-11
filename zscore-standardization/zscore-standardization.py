import numpy as np

def zscore_standardize(X, axis=0, eps=1e-12):
    """
    Standardize X: (X - mean)/std. If 2D and axis=0, per column.
    Return np.ndarray (float).
    """
    # Write code here
    mn = np.mean(X, axis, keepdims=True)
    st = np.std(X, axis, keepdims=True)
    X = (X-mn)/(st+eps)
    return X