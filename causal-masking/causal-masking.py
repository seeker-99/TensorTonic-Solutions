import numpy as np

def apply_causal_mask(scores: list, mask_value: float = -1e9) -> np.ndarray:
    """
    Returns a causally masked NumPy array matching the shape of scores.
    """
    n = scores.shape[-1]

    mask = np.triu(np.ones((n, n), dtype=bool), k=1)

    output = scores.copy()
    output[..., mask] = mask_value

    return output