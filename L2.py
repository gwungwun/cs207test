import numpy as np

def L2(v, *args):
    
    """Returns the L2 norm of a vector v weighted by vector w
    
    INPUTS
    =======
    v: list of floats, required
       a vector to be calculated L2 norm
    w: list of floats, optional, default value is a list of 1
       a vector of weighted coefficient
    
    RETURNS
    ========
    weighted L2 norm: float
       Return a float unless the length of w does not match with length of v
       in which case a ValueError exception is raised

    NOTES
    =====
    PRE: 
         - v, w are lists and have numeric type
    POST:
         - v and w are not changed by this function
         - raises a ValueError exception if len(v) is not equal to len(w)
         - returns a float

    EXAMPLES
    =========
    >>> L2([3, 4])
    5.0
    
    >>> L2([1, 2, 3, 4], [0.25, 0.25, 0.25, 0.25])
    1.3693063937629153
    """
    
    s = 0.0 # Initialize sum
    if len(args) == 0: # No weight vector
        for vi in v:
            s += vi * vi
    else: # Weight vector present
        w = args[0] # Get the weight vector
        if (len(w) != len(v)): # Check lengths of lists
            raise ValueError("Length of list of weights must match length of target list.")
        for i, vi in enumerate(v):
            s += w[i] * w[i] * vi * vi
    return np.sqrt(s)