import numpy as np
from numpy import *
import matplotlib.pyplot as plt 

data = genfromtxt('scores.csv', delimiter=',')

#Extract the data needed to perform a regression
x, y = np.hsplit(data, 2)

def estimate_coef(x, y): 
	# number of observations/points 
	n = np.size(x) 

	# Get the mean of x and y vector (hint: use built-in functions)
	m_x = x.mean()
	m_y = y.mean()

	# calculating cross-deviation and deviation about x 
	SS_xy = np.sum(y*x) - n*m_y*m_x 
	SS_xx = np.sum(x*x) - n*m_x*m_x 

	# Calculate the regression coefficients 
	beta_1 = SS_xy / SS_xx
	beta_0 = m_y - beta_1 * m_x
	
	return (beta_0, beta_1) 

def estimate_error(x, y, b):
	return np.sum(np.square(y - (b[0] + b[1] * x)))

def plot_regression_line(x, y, b): 
	# plot the actual points as scatter plot 
	plt.scatter(x,y)
	plt.xlabel('Hours of study')
	plt.ylabel('Test scores')

	# compute the predicted response vector 
	y_pred = x * b[1] + b[0]

	# plotting the regression line 
	plt.plot(x, y_pred, color = "k") 

	# putting labels 
	plt.xlabel('x') 
	plt.ylabel('y') 

	# function to show plot 
	plt.show() 

# DATASET INPUT
def main(): 	

	# estimating coefficients 
	b = estimate_coef(x, y) 
	print(f'The estimated coefficients are {repr(b[0])} and {repr(b[1])}')

	error = estimate_error(x, y, b)
	print(f'Residual error: {repr(error)}')
	# plotting regression line 
	plot_regression_line(x, y, b) 
	
if __name__ == "__main__": 
	main() 