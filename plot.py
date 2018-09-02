import matplotlib.pyplot as plt

def Plot(X,Y,c):
    if c == 'yvx':
        plt.plot(X,Y)
        plt.xlabel('X')
        plt.ylabel('Y')
    elif c == 'bar':
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.bar(X,Y,label='Bar')
        plt.legend()
    elif c == 'hist':
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.hist(X,Y,histtype='bar',rwidth=0.8)
    elif c == 'sp':
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.scatter(X,Y)
    elif c == 'pie':
        plt.pie(X,labels=Y,autopct='%1.1f%%')

    plt.show()
