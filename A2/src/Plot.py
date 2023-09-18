## @file Plot.py
#  @title Plot
#  @author Michael Hammal
#  @brief This class displays three graphs of the data provided
#  @details This class displays three labelled x-y graphs of the data points
#  provided showing plots for x versus y, y versus t, y versus x

import matplotlib.pyplot as plt


def plot(w, t):
    if len(w) != len(t):
        raise ValueError
    x = [w[i][0] for i in range(len(w))]
    y = [w[i][1] for i in range(len(w))]
    figure, axes = plt.subplots(3)
    axes[0].plot(t, x)
    axes[0].set_ylabel("x(m)")
    axes[1].plot(t, y)
    axes[1].set_ylabel("y(m)")
    axes[2].plot(x, y)
    axes[2].set_ylabel("y(m)")
    axes[2].set_xlabel("x(m)")
    figure.suptitle("Motion simulation")
    plt.show()
