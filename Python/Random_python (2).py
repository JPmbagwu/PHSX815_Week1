#!/usr/bin/env python
# coding: utf-8

# In[11]:


# imports of external packages to use in our code

get_ipython().run_line_magic('matplotlib', 'inline')

import sys
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc, rcParams

# Make use of TeX\ufeff
rc('text',usetex=True)
# Change all fonts to 'Computer Modern'
rc('font',**{'size':14, 'family':'serif','serif':['Times New Roman']})
rc('xtick.major', size=5, pad=7)
rc('xtick', labelsize=15)
rc('ytick.major', size=5, pad=7)
rc('ytick', labelsize=15)

#################
# Random class
#################
# class that can generate random numbers
class Random:
    """A random number generator class"""

    # initialization method for Random class
    def __init__(self, seed = 4444):
        self.seed = seed
        self.m_v = np.uint64(4101842887655102017)
        self.m_w = np.uint64(1)
        self.m_u = np.uint64(1)
        
        self.m_u = np.uint64(self.seed) ^ self.m_v
        self.int64()
        self.m_v = self.m_u
        self.int64()
        self.m_w = self.m_v
        self.int64()

    # function returns a random 64 bit integer
    def int64(self):
        self.m_u = np.uint64(self.m_u * 2862933555777941757) + np.uint64(7046029254386353087)
        self.m_v ^= self.m_v >> np.uint64(17)
        self.m_v ^= self.m_v << np.uint64(31)
        self.m_v ^= self.m_v >> np.uint64(8)
        self.m_w = np.uint64(np.uint64(4294957665)*(self.m_w & np.uint64(0xffffffff))) + np.uint64((self.m_w >> np.uint64(32)))
        x = np.uint64(self.m_u ^ (self.m_u << np.uint64(21)))
        x ^= x >> np.uint64(35)
        x ^= x << np.uint64(4)
        with np.errstate(over='ignore'):
            return (x + self.m_v)^self.m_w

    # function returns a random floating point number between (0, 1) (uniform)
    def rand(self):
        return 5.42101086242752217E-20 * self.int64()

# main function for this Python code
if __name__ == "__main__":
    # if the user includes the flag -h or --help print the options
    if '-h' in sys.argv or '--help' in sys.argv:
        print ("Usage: %s [-seed number]" % sys.argv[0])
        print
        sys.exit(1)

    # default seed
    seed = 1

    # read the user-provided seed from the command line (if there)
    if '-seed' in sys.argv:
        p = sys.argv.index('-seed')
        seed = sys.argv[p+1]

    # set random seed for numpy
    np.random.seed(seed)

    # class instance of our Random class using seed
    random = Random(seed)

    # create some random data
    N = 1000

    # an array of random numbers from numpy
    x = np.random.rand(N)

    # an array of random numbers using our Random class saved in jp.text
    f = open('jp.text','w+')
    for i in range(0,N):
        f.write(str(random.rand())+'\n')
    f.close()
    
# Lets import data.txt
filename = 'jp.text'
dat = np.loadtxt(filename)

# creates histogram
n, bins, patches = plt.hist(dat, 70, density=True, color='b', histtype='step', label= 'Random numbers', alpha=1.0)

# plot formating options
plt.xlabel('x')
plt.ylabel('Probability')
plt.title('Plot of the data in jp.text file')
plt.grid(False)

#Lets plot it!
plt.savefig("RN.pdf", format="pdf", bbox_inches="tight")
plt.legend()
    
# Tweak spacing to prevent clipping of ylabel
plt.tight_layout()

# show figure (program only ends once closed
plt.show()


# In[ ]:




