import numpy as np

def cosine_similarity(a, b):
    """
    Compute cosine similarity between two 1D NumPy arrays.
    Returns: float in [-1, 1]
    """
    if np.sum(a) == 0 or np.sum(b) == 0:
        return 0.0
    a = np.asarray(a)
    b = np.asarray(b)
    a_dot_b = np.dot(a,b)
    return float(a_dot_b/(np.sqrt(np.sum(a**2)) * np.sqrt(np.sum(b**2))))
    