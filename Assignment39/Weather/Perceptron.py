import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

class Perceptron:
    def __init__(self, lr_w=0.00001, lr_b=0.01, epochs=3):
        self.w = np.random.rand(1, 1)
        self.b = np.random.rand(1, 1)
        self.lr_w = lr_w
        self.lr_b = lr_b
        self.epochs = epochs
        self.Errors = []
        self.Errors_test = []
        self.W = []
        self.B = []
        
    def fit(self, X_train, X_test, Y_train, Y_test):
        fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(24, 6))
        
        for epoch in range(self.epochs):
            for i in range(X_train.shape[0]):    
                x = X_train[i]
                y = Y_train[i]
                
                y_pred = x * self.w + self.b
                e = y - y_pred
                
                self.w += self.lr_w * e * x
                self.b += self.lr_b * e * 1
                self.W.append(self.w)
                self.B.append(self.b)
                
            Y_pred = X_train * self.w + self.b
            Error = np.mean(Y_train - Y_pred) ** 2
            self.Errors.append(Error)
            ax2.clear()
            ax2.plot(self.Errors)

            Y_pred_test = X_test * self.w + self.b
            Error_test = np.mean(Y_test - Y_pred_test) ** 2
            self.Errors_test.append(Error_test)
            ax3.clear()
            ax3.plot(self.Errors_test)
                
            ax1.clear()
            ax1.scatter(X_train,Y_train, c='blue')
            ax1.plot(X_train,Y_pred, c='red')
                
        plt.show()  
        np.save('weight_and_biases.npy', self.W, self.B)

    def predict(self, x):
        y_pred_answer = np.matmul(x, self.w) + self.b
        return y_pred_answer

    def evaluate(self, X, Y, loss='MSE'):
        Y_pred = []
        for i in range(X.shape[0]):
            Y_pred.append(self.predict(X[i]))
        Y_pred = np.array(Y_pred)
        
        E = Y - Y_pred
        
        if loss == "MSE":
            return np.mean(E ** 2)
        elif loss == "MAE":
            return np.mean(np.abs(E))