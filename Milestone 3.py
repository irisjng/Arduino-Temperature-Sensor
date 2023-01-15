#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pyfirmata as pf
from time import sleep
import matplotlib.pyplot as plt
from jupyterplot import ProgressPlot


# In[2]:


board = pf.Arduino('COM8') #only run once


# In[3]:


it = pf.util.Iterator(board)
it.start()
board.analog[0].enable_reporting()
board.analog[1].enable_reporting()


# In[4]:


#board.digital[3].write(1) #on
#board.digital[3].write(0) #off


# In[5]:


#V_in = board.analog[1].read()*5
#V_in


# In[6]:


#V_in = board.analog[1].read()*5
#V_drop = board.analog[0].read()*5

#R_0 = 1035
#R_U = ((V_in-V_drop)*1000)/ V_drop
#alpha = 0.00385
#T_0 = 0

#T = (R_U/(R_0 * alpha)) - (1 / alpha)

#T


# In[ ]:


pp = ProgressPlot(y_lim=[-11,30])
x = [] #t
y = []
with open('textt.csv','a') as f:
    for i in range(400):
        board.digital[3].write(1)
        sleep(0.5)
        R_0 = 1035
        alpha = 0.00385
        V_drop = board.analog[0].read()*5
        R_U = ((5-V_drop)*1000)/ V_drop
        T = (R_U/(R_0 * alpha)) - (1 / alpha)
        
        x.append(i)
        y.append(T)
        pp.update(T)
        f.write(str(i) + ', ' + str(T) + '\n')
        board.digital[3].write(0)
        sleep(30)


# In[ ]:


type(V_drop)


# In[147]:


board.digital[3].write(1)
V_drop = board.analog[0].read()*5
R_U = ((5-V_drop)*1000)/ V_drop
R_0 = 1035
alpha = 0.00385

T = (R_U/(R_0 * alpha)) - (1 / alpha)
R_U


# In[ ]:




