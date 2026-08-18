import numpy as np

def cosine_similarity(a, b):
    """
    Compute cosine similarity between two 1D NumPy arrays.
    Returns: float in [-1, 1]
    """
    a = np.asarray(a, dtype=np.float64)
    b = np.asarray(b, dtype=np.float64)

    mag_a = np.linalg.norm(a)
    mag_b = np.linalg.norm(b)
    if mag_a == 0 or mag_b == 0:
        return 0.0
    a_dot_b = np.dot(a,b)
    return float(a_dot_b/(mag_a * mag_b))
    