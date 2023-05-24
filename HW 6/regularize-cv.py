from statistics import mean
import numpy as np
import pandas as pd
from sklearn.linear_model import Ridge, Lasso
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

# Part 1
# Function that normalizes features in training set to zero mean and unit variance.
# Input: training data X_train
# Output: the normalized version of the feature matrix: X, the mean of each column in
# training set: trn_mean, the std dev of each column in training set: trn_std.
def normalize_train(X_train):

    # fill in
    trn_mean = []
    trn_std = []
    for col in X_train.T:
        mean = np.average(col)
        trn_mean.append(mean)
        std = np.std(col)
        trn_std.append(col)
        for i in col:
            i = i - mean
            i = i / std 

        
    return X_train, mean, std


# Part 2
# Function that normalizes testing set according to mean and std of training set
# Input: testing data: X_test, mean of each column in training set: trn_mean, standard deviation of each
# column in training set: trn_std
# Output: X, the normalized version of the feature matrix, X_test.
def normalize_test(X_test, trn_mean, trn_std):

    # fill in
    X = []
    for col in X_test.T:
        for i in range(0, len(col)):
            col[i] = col[i] - trn_mean
            col[i] = col[i] / trn_std
        print(col)
        X.append(col)
    X_return = np.array(X)
    return X_return.T


# Part 3
# Function to return a numpy array generated with `np.logspace` with a length
# of 51 starting from 1E^-1 and ending at 1E^3
def get_lambda_range():

    # fill in
    lmbda = np.logspace(.1, .001, num=51)
    return lmbda


# Part 4
# Function that trains a ridge regression model on the input dataset with lambda=l.
# Input: Feature matrix X, target variable vector y, regularization parameter l.
# Output: model, a numpy object containing the trained model.
def train_model(X, y, l):

    # fill in
    model = Ridge(alpha = l, fit_intercept=True)
    model.fit(X,y)
    return model

#Part 5
#Function that trains a Lasso regression model on the input dataset with lambda=l.
#Input: Feature matrix X, target variable vector y, regularization parameter l.
#Output: model, a numpy object containing the trained model
def train_model_lasso(X,y,l):

    #fill in
    model = Lasso(alpha = l, fit_intercept=True)
    model.fit(X,y)

    return model

# Part 6
# Function that calculates the mean squared error of the model on the input dataset.
# Input: Feature matrix X, target variable vector y, numpdy model object
# Output: mse, the mean squared error
def error(X, y, model):

    # Fill in
    prediction = model.predict(X)
    mse = mean_squared_error(prediction, y)    

    return mse


def main():
    #Importing dataset
    diamonds = pd.read_csv('diamonds.csv')

    #Feature and target matrices
    X = diamonds[['carat', 'depth', 'table', 'x', 'y', 'z', 'clarity', 'cut', 'color']]
    y = diamonds[['price']]

    #Training and testing split, with 25% of the data reserved as the test set
    X = X.to_numpy()
    y = y.to_numpy()
    [X_train, X_test, y_train, y_test] = train_test_split(X, y, test_size=0.25, random_state=101)

    # Normalizing training and testing data
    [X_train, trn_mean, trn_std] = normalize_train(X_train)
    X_test = normalize_test(X_test, trn_mean, trn_std)

    # Define the range of lambda to test
    #lmbda = get_lambda_range()
    lmbda = [1,100]
    MODEL = []
    MSE = []
    for l in lmbda:
        # Train the regression model using a regularization parameter of l
        model = train_model_lasso(X_train, y_train, l)
        print(model.predict(X_test))
        # Evaluate the MSE on the test set
        mse = error(X_test, y_test, model)

        # Store the model and mse in lists for further processing
        MODEL.append(model)
        MSE.append(mse)

    # Part 6
    # Plot the MSE as a function of lmbda
    plt.plot(lmbda, MSE)  # fill in
    plt.xlabel("Mean Squared Error")
    plt.ylabel("Regularization Parameter Lambda")
    plt.title("MSE vs Lambda")
    # Part 7
    # Find best value of lmbda in terms of MSE
    ind = 0  # fill in
    [lmda_best, MSE_best, model_best] = [lmbda[ind], MSE[ind], MODEL[ind]]
    #evaluate the best model for
    #0.25 carat, 3 cut, 3 color, 5 clarity, 60 depth, 55 table, 4 x, 3 y, 2 z diamond (Use the Ridge regression model `train_model`)
    # NOTE: Make sure to normalize the given data

    print(
        "Best lambda tested is "
        + str(lmda_best)
        + ", which yields an MSE of "
        + str(MSE_best)
    )

    plt.show()
    return model_best


if __name__ == "__main__":
    model_best = main()
    # We use the following functions to obtain the model parameters instead of model_best.get_params()
    print(model_best.coef_)
    print(model_best.intercept_)
