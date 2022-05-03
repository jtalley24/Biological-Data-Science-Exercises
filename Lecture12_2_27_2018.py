import numpy as np
import matplotlib.pyplot as pyplot
import math as math
from scipy.stats import norm

# First questions - plot normal distribution

min = 0
max = 10
norm_range = np.arange(min, max+1, 0.01)

mu = 5
sigma = 1
norm_y = norm.pdf(norm_range, mu, sigma)

print norm_range
print norm_y

pyplot.figure()
pyplot.plot(norm_range, norm_y)
pyplot.show()

#Second question - see how parameters change things

norm_range = np.arange(150, 351, 0.001)
a_mu = 280
a_sig = 20
b_mu = 210
b_sig = 20
c_mu = 190
c_sig = 10
# Creating three different distributions
pdf_a = norm.pdf(norm_range, a_mu, a_sig)
pdf_b = 0.5 * norm.pdf(norm_range, b_mu, b_sig)
pdf_c = 0.2 * norm.pdf(norm_range, c_mu, c_sig)
# Adding them together and plotting
pyplot.plot(norm_range, pdf_a, norm_range, pdf_b, norm_range, pdf_c)
pyplot.xlim(150, 350)
pyplot.show()


#Third question, Central Limit Theorem

data = [62, 64, 37,100, 74, 82, 64, 77, 71, 66, 97, 76, 79, 82, 88, 77, 85, 48, 80, 85, 93, 78, 88, 75, 81, 76, 82, 85, 87, 56, 86, 77, 85, 74, 77, 82, 71, 78, 64, 79, 93, 75, 67]
print data

size_2 = []
size_5 = []
size_10 = []
size_20 = []
size_30 = []

for i in range(0, 1000):
    size_2.append(np.mean(np.random.choice(data, 2)))
    size_5.append(np.mean(np.random.choice(data, 5)))
    size_10.append(np.mean(np.random.choice(data, 10)))
    size_20.append(np.mean(np.random.choice(data, 20)))
    size_30.append(np.mean(np.random.choice(data, 30)))
    
pyplot.figure(1)

pyplot.subplot(231)
pyplot.hist(data, bins = 20)
pyplot.title('Grade Distribution')

pyplot.subplot(232)
pyplot.hist(size_2, bins = 20)
pyplot.title('Sample of 2')

pyplot.subplot(233)
pyplot.hist(size_5, bins = 20)
pyplot.title('Sample of 5')

pyplot.subplot(234)
pyplot.hist(size_10, bins = 20)
pyplot.title('Sample of 10')

pyplot.subplot(235)
pyplot.hist(size_20, bins = 20)
pyplot.title('Sample of 20')

pyplot.subplot(236)
pyplot.hist(size_30, bins = 20)
pyplot.title('Sample of 30')

pyplot.show()
    