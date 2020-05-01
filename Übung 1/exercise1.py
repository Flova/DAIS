import numpy as np
import matplotlib.pyplot as plt


def make_grades_plot():
    lecture1 = np.loadtxt("./DAMI2-PlotData/Grades_lecture1.dat").astype(np.uint8)
    lecture2 = np.loadtxt("./DAMI2-PlotData/Grades_lecture2.dat").astype(np.uint8)
    lecture1_hist, _ = np.histogram(lecture1, bins=5)
    lecture2_hist, _ = np.histogram(lecture2, bins=5)

    width = 0.3
    plt.bar(np.arange(1,6) - width/2, lecture1_hist, width, label='Lecture 1')
    plt.bar(np.arange(1,6) + width/2, lecture2_hist, width, label='Lecture 2')
    plt.title('Grade Histogram')
    plt.ylabel('Count')
    plt.xlabel('Grade')
    plt.tight_layout()
    plt.legend()
    plt.show()


if __name__ == "__main__":
    make_grades_plot()