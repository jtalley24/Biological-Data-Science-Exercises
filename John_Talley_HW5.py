
# coding: utf-8

# In[22]:


import numpy as np
import matplotlib.pyplot as pyplot
import matplotlib.mlab as mlab
import math

#14.d.
obs = [30.0, 15.0, 8.0]
exp = [17.67, 17.67, 17.67]

chiSq = 0

for i in range(0,len(obs)):
    chiSq = chiSq + ((obs[i]-exp[i])**2)/(exp[i])
    
print 'Chi-Squared Value Birds: ', chiSq

#Yes, as 14.30 > 5.991, which is the critical value at alpha = 0.05 and df = 1, the test indicated that the probability of birds being killed by crashing into a window is dependent on the angle.

#19.a.
canes = []
for j in range(0,50):
    canes.append(0)
for k in range(0,39):
    canes.append(1)
for l in range(0,7):
    canes.append(2)
for m in range(0,4):
    canes.append(3)
#no years had greater than 3
mean = np.mean(canes)
print 'Mean hurricanes per year: ', mean
#c.
expPrX =[]
obsYrs = [50,39,7,4]
for n in range (0,4):
    denom = math.factorial(n)
    PrX =  100*(2.718**-mean)*(mean**n)/denom
    expPrX.append(PrX)
print expPrX

chiSqCanes = 0
for p in range(0,len(expPrX)):
    chiSqCanes = chiSqCanes + ((obsYrs[p]-expPrX[p])**2)/(expPrX[p])
    
print 'Chi-squared of hurricanes: ', chiSqCanes
# df = 3-1-0 = 2
# 3.406 < 5.991 critical value at alpha = 0.05 and df = 2, so we fail to reject the null hypothesis for the distribution.

#24.a. Bar Graph is most appropriate.
vol = float(17)/float(30)
solv = float(2)/float(30)
left = float(7)/float(30)
right = float(4)/float(30)

objects = ('Volatile', 'Solvent', 'Left', 'Right')
y_pos = np.arange(len(objects))
directions = [vol, solv, left, right]
 
pyplot.bar(y_pos, directions, align='center', alpha=0.5)
pyplot.xticks(y_pos, objects)
pyplot.ylabel('Frequency')
pyplot.title('Direction of Growth')
 
pyplot.show()

