def swap(b, h):
    hold = b
    b = h
    h = hold
    return b, h

def histogram(data, n, b, h):
    # data is a list
    # n is an integer
    # b and h are floats
    
    # Write your code here
    
    #declares list hist that will be the return value
    hist = []
    
    #creates variable to track total number of items -> used to find number that belongs in last bin
    count = 0

    #checks if b and h are the same value
    if (b == h):
        print("b and h are the same value")
        return hist
    
    #checks if b is larger than h
    elif (b > h):
        b, h = swap(b, h)
    
    #checks if n is equal to 0
    if (n <= 0):
        return hist

    #initializes hist as a list of n 0s
    for i in range(n):
        hist.append(0)

    #removes data points that are greater than h or less than b
    data = [i for i in data if i < h]
    data = [i for i in data if i > b]

    #calculates bin width
    w = (h-b)/n

    #iterates through list and places values in appropriate bin
    for i in range(0,n-1):
        for x in range(0, len(data)):
            if (data[x] >= (b + i*w)) and (data[x] < (b + (i+1) * w)):
                hist[i] += 1
                count += 1

    #finds value for last bin
    hist[n - 1] = len(data) - count
    

    # return the variable storing the histogram
    # Output should be a list
    return hist


def happybirthday(name_to_day, name_to_month, name_to_year):
    #name_to_day, name_to_month and name_to_year are dictionaries
    
    # Write your code here
    name = list(name_to_month.keys())
    month = list(name_to_month.values())
    day = list(name_to_day.values())
    year = list(name_to_year.values())
    age = []

    month_to_all = {}
    
    for i in range(0, len(name)):
        age.append(2022 - year[i])
        dya = (day[i] , year[i], age[i])
        n_dya = (name[i], dya)

        month_to_all[month[i]] = n_dya
        
        
    # return the variable storing name_to_all
    # Output should be a dictionary
    return month_to_all
