import numpy as np
from collections import Counter
def entropy_node(y: list[int]) -> float:
    """
    Returns the Shannon entropy as a Python float.
    """
    # Write code here
    size = len(y)
    entropy = 0.0
    
    if size == 0: 
        return 0.0
    counts = Counter(y)
    
    for count in counts.values():
        p = count / size
        entropy -= p * np.log2(p)
        
    return entropy