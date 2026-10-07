import numpy as np

def pad_sequences(seqs: list, pad_value: int = 0, max_len: int | None = None) -> np.ndarray:
    """
    Returns: np.ndarray of shape (N, L) where:
      N = len(seqs)
      L = max_len if provided else max(len(seq) for seq in seqs) or 0
    """
    # Your code here
    if max_len is None:
        max_len = max((len(seq) for seq in seqs), default=0)
    if not seqs:
        return np.empty((0, max_len), dtype=int)
    return np.array([seq[:max_len] + [pad_value] * max(0, max_len-len(seq)) for seq in seqs], dtype=int)
    # for i in range(len(seqs[]))
    # return seqs[0][2]
    pass