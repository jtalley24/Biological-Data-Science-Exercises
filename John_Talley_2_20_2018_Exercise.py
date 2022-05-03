
# coding: utf-8

# In[4]:


import numpy as np
import matplotlib.pyplot as pyplot
import matplotlib.mlab as mlab
import math
import random

header = []
data = []

input = open("femaleMiceWeights.csv", 'rU')

for line in input:
#print line
    if line.startswith('#'):
        print line
        header = line.strip('\n').split(',')
    else:
        #print line
        line = line.strip('\n').split(',')
        data.append(line)
input.close()

chow = []
hf = []

for i in range(0, len(data)):
    if data[i][0] == 'chow':
        chow.append(data[i][1])
    elif data[i][0] == 'hf':
        hf.append(data[i][1])

for j in range(0,len(chow)):
    chow[j] = float(chow[j])
print 'Chow List: ', chow

for k in range(0,len(hf)):
    hf[k] = float(hf[k])
print 'High-Fat List: ', hf

chowMean = np.mean(chow)
print 'Chow Mean: ', chowMean
hfMean = np.mean(hf)
print 'High-Fat Mean: ', hfMean

test = hfMean - chowMean
print test

x_OT = [1] * len(chow)
x_D = [3] * len(hf)  
pyplot.plot(x_OT, chow, marker = 'o', linestyle = 'None')
pyplot.plot(x_D, hf, marker = 'o', linestyle = 'None')
pyplot.xlim(0,4)
pyplot.xticks(range(1,4,2), ['Chow', 'High-Fat']) # Set some labels
pyplot.ylabel('Weight')
pyplot.show()

input = open("femaleControlsPopulation.csv", 'rU')

popHeader = []
popData = []

for popLine in input:
#print popLine
    if popLine.startswith('#'):
        print popLine
        popHeader = popLine.strip('\n').split(',')
    else:
        #print line
        popLine = popLine.strip('\n').split(',')
        popData.append(popLine)
input.close()

ctrls = []

for p in range(1, len(popData)):
        ctrls.append(popData[p][0])

for q in range(0,len(ctrls)):
    ctrls[q] = float(ctrls[q])
print 'Female Population List: ', ctrls

sample1 = []
for r in range(0,12):
    sample1.append(ctrls[r])
mean1 = np.mean(sample1)
print 'Sample 1 Mean: ', mean1

sample2 = []
for s in range(12,24):
    sample2.append(ctrls[s])
mean2 = np.mean(sample2)
print 'Sample 2 Mean: ', mean2

sample3 = []
for t in range(24,36):
    sample3.append(ctrls[t])
mean3 = np.mean(sample3)
print 'Sample 3 Mean: ', mean3

sample4 = []
for u in range(36,48):
    sample4.append(ctrls[u])
mean4 = np.mean(sample4)
print 'Sample 4 Mean: ', mean4

sample5 = []
for v in range(48,60):
    sample5.append(ctrls[v])
mean5 = np.mean(sample5)
print 'Sample 5 Mean: ', mean5

randSample = []
randMeans =[]
meanDiff = []

for x in range(0,10000):
    for w in range(0,24):
        randWeight = ctrls[random.randint(0,len(ctrls)-1)]
        randSample.append(randWeight)
    split1 = []
    split2 = []
    for y in range(0,12):
        split1Weight = randSample[random.randint(0,len(randSample)-1)]
        split1.append(split1Weight)
    split1mean = np.mean(split1)
    for z in range(0,12):
        split2Weight = randSample[random.randint(0,len(randSample)-1)]
        split2.append(split2Weight)
    split2mean = np.mean(split2)
    dMean = split2mean - split1mean
    meanDiff.append(dMean)

greater = 0
for a in range(0,10000):
    if meanDiff[a] > 3.02083333333:
        greater += 1
percent = 100*(float(greater)/10000)
print 'Percent: ', percent

pvalue = float(percent)/100
print 'P-value: ', pvalue


# In[3]:


pyplot.figure()
pyplot.hist(meanDiff,50,normed=True)
pyplot.xlabel('Difference in Split 1 and Split 2 Mean Weights')
pyplot.ylabel('Relative Frequency')
pyplot.axvline(x = 3.02083333333, color='r', linestyle='dashed', linewidth=2)
pyplot.show()

