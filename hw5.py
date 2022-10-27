import numpy as np
import random
import csv
import sys
import matplotlib.pyplot as plt


def Qs():
    
    #Q2
    x = []
    y = []
    with open(sys.argv[1], newline='') as csvfile:
            lines = csv.reader(csvfile, delimiter=',')
            next(lines)
            for row in lines:
                x.append(int(row[0]))
                y.append(int(row[1]))
            
            plt.plot(x, y)
            plt.xlabel('Year')
            plt.ylabel('Number of frozen days')
            plt.savefig("plot.jpg")
            
    #resets values to re-open for next Qs        
    x = []
    y = []
    
    
    with open(sys.argv[1], newline='') as csvfile:
            lines = csv.reader(csvfile, delimiter=',')
            next(lines)
            for row in lines:
                x.append([1,int(row[0])])
                y.append(int(row[1]))
    
    
    #Q3
    X = np.array(x)
    Y = np.array(y)
    print("Q3a:")
    print(X)
    print("Q3b:")
    print(Y)
    
    #it took me longer than I'd like to admit to figure out how to do this part
    Z = X.transpose()@X
    print("Q3c:")
    print(Z)
    
    I = np.linalg.inv(Z)
    print("Q3d:")
    print(I)
    
    PI = I@X.transpose()
    print("Q3e:")
    print(PI)
    
    hat_beta= PI@Y
    print("Q3f:")
    print(hat_beta)
    
    #Q4
    y_test = hat_beta[0] + hat_beta[1]*2021
    print("Q4: " + str(y_test))
    
    #5
    if(hat_beta[1] < 0):
        print("Q5a: " + "<")
        print("Q5b: " + "the negative sign indicates the number of frozen days are becoming less frequent every year")
    elif(hat_beta[1] > 0):
        print("Q5a: " + ">")
        print("Q5b: " + "the positive sign indicates the number of frozen days are becoming more frequent every year")
    else:
        print("Q5a: " + "=")
        print("Q5b: " + "the equals sign indicates the number of frozen days are consistent every year")
    
    
    #6
    x_star = (-hat_beta[0])/hat_beta[1]
    print("Q6a: " + str(x_star))
    print("Q6b: " + "yes, sice we are observing a downward trend in frequency of frozen days, in a span of 500 years it seems reasonable to arrive at this point point")
    return



if __name__ == '__main__':   
    Qs()
    pass