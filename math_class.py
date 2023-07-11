
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt 
import numpy as np

x = np.random.randint(0, 100, size=(100, 1))
y = np.array([ np.random.randint(n - 20, n + 20) for n in x ])

linear = LinearRegression()
linear.fit(x, y)

plt.scatter(x, y)
plt.plot(x, linear.predict(x), color="red")
plt.show()