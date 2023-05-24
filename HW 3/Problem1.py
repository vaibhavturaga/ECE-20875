import numpy as np
import matplotlib.pyplot as plt


def norm_histogram(hist):
    """
    takes a histogram of counts and creates a histogram of probabilities
    :param hist: a numpy ndarray object
    :return: list
    """
    total = 0
    for i in hist:
        total += i
    
    for i in range(0, len(hist)):
        hist[i] = hist[i] / total
    return hist


def compute_j(histo, width):
    """
    takes histogram of counts, uses norm_histogram to convert to probabilties, it then calculates compute_j for one bin width
    :param histo: list
    :param width: float
    :return: float
    """
    #J(w) = (2/(m-1) * w) - ((m+1)/(m-1)*w)(p1^2 + p2^2 ... + pn^2)
    num_samples = sum(histo)
    hist_probability = norm_histogram(histo)
    hist_prob_squared = [i * i for i in hist_probability]
    J = (2 / ((num_samples - 1) * width)) - ((num_samples + 1) * sum(hist_prob_squared) / ((num_samples - 1) * width))
    return J


def sweep_n(data, minimum, maximum, min_bins, max_bins):
    """
    find the optimal bin
    calculate compute_j for a full sweep [min_bins to max_bins]
    please make sure max_bins is included in your sweep
    :param data: list
    :param minimum: int
    :param maximum: int
    :param min_bins: int
    :param max_bins: int
    :return: list
    """
    
    j_vals = []
    for i in range(min_bins, max_bins + 1):
        histo = plt.hist(data, bins = i, range = (minimum, maximum))[0]
        width = (maximum - minimum) / i
        j_vals.append(compute_j(histo, width))
    
    return j_vals


def find_min(l):
    """
    takes a list of numbers and returns the mean of the three smallest number in that list and their index.
    return as a tuple i.e. (the_mean_of_the_3_smallest_values,[list_of_the_3_smallest_values])
    For example:
        A list(l) is [14,27,15,49,23,41,147]
        The you should return ((14+15+23)/3,[0,2,4])

    :param l: list
    :return: tuple
    """
    sorted_list = sorted(l) # sorts list in descending order and assigns to new list
    small_list = sorted_list[:3] #creates list of smallest 3 values
    index_list = []
    for i in small_list:
        if i in l:
            index_list.append(l.index(i))
    
    mean_min = ((sum(small_list)/3), index_list) #creates tuple with mean of smallest 3 values and the indexes

    return mean_min


if __name__ == "__main__":
    data = np.loadtxt("input.txt")  # reads data from input.txt
    lo = min(data)
    hi = max(data)
    bin_l = 1
    bin_h = 100
    js = sweep_n(data, lo, hi, bin_l, bin_h)
    """
    the values bin_l and bin_h represent the lower and higher bound of the range of bins.
    They will change when we test your code and you should be mindful of that.
    """
    print(find_min(js))
