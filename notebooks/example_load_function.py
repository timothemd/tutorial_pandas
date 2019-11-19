import matplotlib.pyplot as plt
import numpy as np

np.random.seed(289380)
data = np.random.randn(2, 1000)

fig, axs = plt.subplots(2,figsize=(5,5))
axs[0].hist(data[0])
axs[1].scatter(data[0],data[1])

plt.show()