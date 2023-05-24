import scipy.stats as stats
import matplotlib.pyplot as plt
import numpy as np
import math


def get_data(filename="input.txt"):
    return np.loadtxt(filename)


def get_coordinates(data, each_dist):
    # Part B
    """
    :param: np.ndarray, str
    :return: np.ndarray, np.ndarray
    """
    # Your code starts here...
    prob = stats.probplot(data, dist = each_dist)
    x = prob[0][0]
    y = prob[0][1]

    xy = (x,y)
    return xy


def calculate_distance(x, y):
    # Part B

    """
    :param: float, float
    :return: float
    """
    dist = math.sqrt(((x - ((x+y)/2))**2) + ((y - ((x+y)/2))**2))
    return dist


def find_dist(sum_err, dists):
    # Part B
    """
    :param: list[float], list[str]
    :return: str, float
    """
    # Your code starts here...
    small_val = min(sum_err) #finds smallest values
    small_index = sum_err.index(small_val) #finds indexes of smallest value from original list
    return (dists[small_index], small_val)


def main(data_file):
    """
        Input a csv file and return distribution type, the error corresponding to the distribution type (e.g. return 'norm',0.32)
    :param: *.csv file name (str)
    :return: str, float
    """
    # Part B
    data = get_data(data_file)
    dists = ("norm", "expon", "uniform", "wald")
    sum_err = [0] * 4
    for ind, each_dist in enumerate(dists):
        X, Y = get_coordinates(data, each_dist)
        for x, y in zip(X, Y):
            sum_err[ind] += calculate_distance(x, y)
    return find_dist(sum_err, dists)

if __name__ == "__main__":
    for each_dataset in [
        "sample_norm.csv",
        "sample_expon.csv",
        "sample_uniform.csv",
        "sample_wald.csv",
    ]:
        print(main(each_dataset))
