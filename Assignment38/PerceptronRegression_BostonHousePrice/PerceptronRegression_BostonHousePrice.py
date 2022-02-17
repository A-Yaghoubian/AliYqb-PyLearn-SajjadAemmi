import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split

# Prepare Dataset
data_1 = load_boston()
X = data_1.data
Y = data_1.target

data_2 = pd.DataFrame(data_1.data, columns=data_1.feature_names)
data_2['Price'] = Y

X = data_2[['RM', 'DIS']]
X = X.to_numpy()

Y = data_2[['Price']]
Y = Y.to_numpy()
Y = Y.reshape(-1, 1)

X_train, X_test, Y_train, Y_test = train_test_split(X, Y)


class Perceptron:
    def __init__(self, epochs=1, learning_rate=0.001):
        self.W = np.random.rand(2, 1)
        self.epochs = epochs
        self.learning_rate = learning_rate
    
    def fit(self, X_train, Y_train):
        N = X_train.shape[0]
        self.Errors = []
        
        x_aranged = np.arange(X_train[:, 0].min(), X_train[:, 0].max())
        y_aranged = np.arange(X_train[:, 1].min(), X_train[:, 1].max())
        
        fig = plt.figure(figsize=(13, 7))
        
        for self.epoch in range(self.epochs):
            for i in range(N):
                # x = X[i].reshape(-1, 1)
                x = X_train[i, :]
                y_pred = np.matmul(x, self.W) 
                e = Y[i] - y_pred
                
                x = x.reshape(2, 1)
                self.W += self.learning_rate * x * e


                fig.clear()
                Y_pred = np.matmul(X_train, self.W)
                ax = fig.add_subplot(121, projection='3d')
                ax.clear()
                ax.scatter(X_train[:, 0], X_train[:, 1], Y_train, c='#00ffff')

                x, y = np.meshgrid(x_aranged, y_aranged)
                z = self.W[0] * x + self.W[1] * y
                
                ax.plot_surface(x, y, z, alpha=0.45)
                ax.set_xlabel("RM")
                ax.set_ylabel("DIS")
                ax.set_zlabel("Price")

                
                Error = np.mean(np.abs(Y_train - Y_pred))
                self.Errors.append(Error)

                ax2 = fig.add_subplot(122)
                ax2.clear()
                ax2.plot(self.Errors)
                
                ax2.set_title('Training Curve')
                ax2.set_ylabel("Cost")
                ax2.set_xlabel("Iteration #")
                    
                plt.pause(0.01)
                
            plt.show()
        
    def predict(self, X_test):
        Y_pred = np.matmul(X_test, self.W)
        return Y_pred
    
    def evaluate(self, X_test, Y_test):
        Y_pred = self.predict(X_test)
        MSE = np.mean((np.abs(Y_test - Y_pred)) ** 2)
        return MSE

perceptron = Perceptron()
perceptron.fit(X_train, Y_train)