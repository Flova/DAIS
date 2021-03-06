import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


def make_grades_plot():
    lecture1 = np.loadtxt("./DAMI2-PlotData/Grades_lecture1.dat")
    lecture2 = np.loadtxt("./DAMI2-PlotData/Grades_lecture2.dat")
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

def make_musik_plot():
    sizes = np.loadtxt("./DAMI2-PlotData/Music.dat")
    labels = ['Grunge', 'Hip Hop', 'Metal', 'Schlager music', 'Rock']

    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
    plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.title('Music Taste')
    plt.show()

def make_airline_plot():
    data = pd.read_csv("./DAMI2-PlotData/AirlineSafety.csv", delimiter=',')   # TODO
    mio_seat_kilometers_per_week = (data.avail_seat_km_per_week*52*15) / 10**10  # Scale time to 15 years and scale to 10 billion seat km
    corrected_fat_85_99 = data.fatalities_85_99 / mio_seat_kilometers_per_week
    corrected_fat_00_14 = data.fatalities_00_14 / mio_seat_kilometers_per_week
    plt.boxplot([corrected_fat_85_99, corrected_fat_00_14], labels=["1985 - 1999", "2000 - 2014"])
    plt.title('Destribution of airline safety through the ages')
    plt.ylabel('Fatalities per 10 Billion Seat Kilometers')
    plt.show()
    
def make_brexit_plot():
    data = pd.read_csv("./DAMI2-PlotData/Economist_Brexit.csv", delimiter=',', names=['dates', 'pro', 'contra'], header=0)
    data.dates = pd.to_datetime(data.dates, format='%d/%m/%y')
    data.set_index(['dates'], inplace=True)
    plt.plot(data.index, data.pro, label=data.pro.name)
    plt.plot(data.index, data.contra, label=data.contra.name)
    plt.title('Brexit')
    plt.ylabel('Percent')
    plt.xlabel('Date')
    plt.legend()
    plt.show()

def make_gender_pay_gap_plot():
    data = pd.read_csv("./DAMI2-PlotData/GenderPayGap_2015OECD.csv", delimiter=',', header=0)
    data.set_index(['LOCATION'], inplace=True)
    data.sort_values(['Value'], ascending=[0], inplace=True)
    plt.barh(data.index, data.Value, 0.7)
    plt.title('Gender wage gap by country')
    plt.xlabel('Gender wage gap')
    plt.ylabel('Country')
    plt.show()


if __name__ == "__main__":
    make_grades_plot()
    make_musik_plot()
    make_airline_plot()
    make_brexit_plot()
    make_gender_pay_gap_plot()