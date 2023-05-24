import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# Return fitted model parameters to the dataset at datapath for each choice in degrees.
# Input: datapath as a string specifying a .txt file, degrees as a list of positive integers.
# Output: paramFits, a list with the same length as degrees, where paramFits[i] is the list of
# coefficients when fitting a polynomial of d = degrees[i].
def main(datapath, degrees):
    paramFits = []
    # fill in
    # read the input file, assuming it has two columns, where each row is of the form [x y] as
    # in poly.txt.
    # iterate through each n in degrees, calling the feature_matrix and least_squares functions to solve
    # for the model parameters in each case. Append the result to paramFits each time.
    data = pd.read_csv(datapath, sep=" ")
    data.columns = ["x", "y"]
    data.sort_values(by=["x"])
    X = data["x"]
    y = data["y"]
    for n in degrees:
        print(least_squares(feature_matrix(X, n), y))
        paramFits.append(least_squares(feature_matrix(X, n), y))
    return paramFits


# Return the feature matrix for fitting a polynomial of degree d based on the explanatory variable
# samples in x.
# Input: x as a list of the independent variable samples, and d as an integer.
# Output: X, a list of features for each sample, where X[i][j] corresponds to the jth coefficient
# for the ith sample. Viewed as a matrix, X should have dimension #samples by d+1.
def feature_matrix(x, d):

    # fill in
    # There are several ways to write this function. The most efficient would be a nested list comprehension
    # which for each sample in x calculates x^d, x^(d-1), ..., x^0.
    retArray = [x[0]**(d) for i in range(0,len(x))]
    for z in range(1, d+1):
        line = [x[i]**(d-z) for i in range(0,len(x))]
        retArray = np.vstack((retArray, line))
    return retArray.T


# Return the least squares solution based on the feature matrix X and corresponding target variable samples in y.
# Input: X as a list of features for each sample, and y as a list of target variable samples.
# Output: B, a list of the fitted model parameters based on the least squares solution.
def least_squares(X, y):
    X = np.array(X)
    y = np.array(y)

    # fill in
    # Use the matrix algebra functions in numpy to solve the least squares equations. This can be done in just one line.
    B = np.linalg.lstsq(X, y)
    return B


if __name__ == "__main__":
    datapath = "poly.txt"
    degrees = [2, 4]

    paramFits = main(datapath, degrees)
    index = [i for i in range(len(paramFits[1][0]))]
    print((paramFits[0][0]).sort())
    print((paramFits[1][0]).sort())
    plt.plot((paramFits[0][0]), label = "2 degrees")
    plt.plot((paramFits[1][0]), label = "4 degrees")
    plt.legend()
    plt.show()

