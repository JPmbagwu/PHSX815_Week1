#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('matplotlib', 'inline')

import sys
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc, rcParams

# Let's generate random floating point values
from random import seed
from random import random
# seed random number generator
seed(1)
# generate random numbers between 0-1
for _ in range(1000):
 value = random()
 print(value)


# In[ ]:




