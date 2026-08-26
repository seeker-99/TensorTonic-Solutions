import numpy as np
import math

def positional_encoding(seq_len: int, d_model: int, base: float = 10000.0) -> np.ndarray:
    """
    Returns a NumPy array of shape (seq_len, d_model).
    """
    # Write code here
    arr = np.zeros((seq_len, d_model))
    
    for i in range(seq_len):
        for j in range(d_model):
            angle = i / (base ** (2 * (j//2) / d_model))
            if (j % 2) == 0:
                arr[i][j] = math.sin(angle)
            else:
                arr[i][j] = math.cos(angle)     
    return arr