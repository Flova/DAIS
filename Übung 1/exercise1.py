import numpy as np
import matplotlib.pyplot as plt

def make_grades_plot():
    lecture1 = np.loadtxt("./DAMI2-PlotData/Grades_lecture1.dat")
    lecture2 = np.loadtxt("./DAMI2-PlotData/Grades_lecture2.dat")
    combined = np.stack([lecture1, lecture2], axis=1)
    num_grades = 5
    plt.hist(combined, num_grades, histtype='bar', color=['red', 'blue'], alpha=0.5)
    plt.show()


if __name__ == "__main__":
    make_grades_plot()