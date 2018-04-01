# des-metal
A Python DES implementation designed for analysis of the algorithm rather than for performance.

# Design
The core of des-metal is contained in the file des.py. This implementation tries to break apart the several components of DES (the Feistel Scheme, the permutations, the Feistel Function, the key schedule) into several functions that can be composed together to form the standard DES (this is done in the function std_des). This allows flexibility regarding the number of rounds wanted, the application or not of the S-Boxes, the alteration of S-Boxes, and other things.

# Usage
The function std_des implements DES, but currently it takes only a bit array (that is, a Python list of 1s and 0s), that represents exactly 64 bits for the text and the key. ECB mode will be implemented, but other modes won't.

# linear.py
This file contains functions that are useful for linear cryptanalysis of DES.
