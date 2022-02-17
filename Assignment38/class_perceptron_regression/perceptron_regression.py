import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Prepare Dataset
data = pd.read_csv('regressionOutliers.csv')
# print(data)

# حذف نویز دستی
data = data.loc[data['Y'] < 10]

X_train = data['X']
Y_train = data['Y']

X_train = np.array(X_train)
Y_train = np.array(Y_train)

X_train = X_train.reshape(-1, 1)
Y_train = Y_train.reshape(-1, 1)
# print(X_train.shape)

N = X_train.shape[0]

# Hyper parameters
learning_rate = 0.05
epochs = 2 # extra time for better learning

# Init weight
W = np.random.rand(1, 1)

fig, (ax1, ax2) = plt.subplots(1, 2)
Errors = []

# Train
for epoch in range(epochs):
    for i in range(N):
        y_pred = np.matmul(X_train[i], W)
        e = Y_train[i] - y_pred
        # print(e)
        
        # Update weight
        W += e * learning_rate * X_train[i]
        
        # Visualization
        Y_pred = np.matmul(X_train, W)
        ax1.clear()
        ax1.scatter(X_train, Y_train, c="#0000ff")
        ax1.plot(X_train, Y_pred, c="#ff0000", lw=4)
        
        Error = np.mean(Y_train - Y_pred)
        Errors.append(Error)        
        
        ax2.clear()
        ax2.plot(Errors)
        
        plt.pause(0.01)

plt.show()