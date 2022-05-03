
# coding: utf-8

# In[49]:


import numpy as np
import matplotlib.pyplot as pyplot
import matplotlib.mlab as mlab
import math

#19.a.
print "19."
x= 109
n = 200

prop = float(x)/float(n)

print "Best estimate of proportion of shoppers injured: " + str(prop)


lower = prop-1.96*((prop*(1-prop)/n)**0.5)
upper = prop+1.96*((prop*(1-prop)/n)**0.5)

print "95% confidence interval: (" + str(lower) + ", " + str(upper) + ")"

#24.b.
print "24."
n = float(12)
p = float(3)/float(12)
q = float(9)/float(12)
stdev = (n*p*q)**0.5
print "Standard deviation: " + str(stdev)
#c.
var = (float(stdev))**2
print "Variance: " + str(var)
#d.
probTwo = 0.25**2 + 0.75**10
print "Probability of two wrinkled: " + str(probTwo)

#27.
print "27."
winter = 766
total = 1636
p1 = float(766)/float(1636) 
lowerBnd = p1-1.96*((p1*(1-p1)/total)**0.5)
upperBnd = p1+1.96*((p1*(1-p1)/total)**0.5)
print "95% confidence interval: (" + str(lowerBnd) + ", " + str(upperBnd) + ")"
#The upper bound of the 95% confidence interval for proportion of suicides taking place in the winter is not even >= 0.5, so there is no evidence to support the claim that suicide rates are higher in the winter.

#29.a.
print "29."
mu = 0.3*7
sigma = (0.3*0.7*7)**0.5
v = sigma**2
x = np.linspace(mu-3*sigma, mu+3*sigma, 100)
pyplot.plot(x, mlab.normpdf(x, mu, sigma))
pyplot.xlabel('Number of Vancomycin Resistant Isolates')
pyplot.ylabel('Frequency')
pyplot.show()

#31.a.
print "31."
mu1 = float(13)
sigma1 = ((float(13)/float(16))*(float(3)/float(16))*16)**0.5
v1 = sigma1**2
x1 = np.linspace(mu1-3*sigma1, mu1+3*sigma1, 100)
pyplot.plot(x1, mlab.normpdf(x1, mu1, sigma1))
pyplot.xlabel('Number of Diverse Clades')
pyplot.ylabel('Frequency')
pyplot.show()

