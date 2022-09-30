import matplotlib.pyplot as plt


def plot(x, y, xName = 'x - axis', yName = 'y - axis', plotName = 'plot'):
    # plot points
    plt.plot(x,y)

    # rename axises
    plt.xlabel(xName)
    plt.ylabel(yName)

    # set graph title
    plt.title(plotName)

    # show graph
    plt.show()
