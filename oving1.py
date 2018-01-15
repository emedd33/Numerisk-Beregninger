import numpy as np
import matplotlib.pyplot as plt


def matrixPrint():
    # A)
    print("hello world")

    # B)
    a = np.array([1, 2, 3])
    b = np.array([4, 5, 6])
    A = np.array(((1, 2, 4), (1, 3, 4), (2, 3, 5)))
    B = np.array(((2, 8, 14), (4, 10, 16), (6, 12, 18)))

    print(a)
    print(b)
    print(A)
    print(B)

    print(a + b)
    print(a * b)
    print(A * B)

    print(np.transpose(A))
    C = np.invert(A)
    print(C)

    print(C * b)


def fib(n):
    tall_1 = 1
    tall_2 = 1
    x = [tall_1]
    x.append(tall_2)
    if (n > 1):
        print(tall_1)
        print(tall_2)
        for i in range(1, n):
            temp = tall_1 + tall_2
            print(temp)
            tall_1 = tall_2
            tall_2 = temp
            x.append(tall_2)
        plt.plot(x)
        plt.show()

def plotSin(n):
    step = (2*np.pi)/n
    temp = 0
    x = [None]*n
    for i in range(n):
        x[i] = np.sin(temp)
        temp = step+temp
    plt.plot(x)
    plt.ylabel("function value")
    plt.xlabel("variable value")
    plt.legend()
    plt.show()

