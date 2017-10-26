''' Linear Regression
	CS-5001 : HW#1 
	Submission : T220010122017
	Author : Ronith Muttur
	Problem Designed by Dr. Ricardo Morales
'''

'''
	Name: Linear Regression and Trashcans

	Problem Description:
	Dr. Zoidberg is always in the lookout for a good meal, 
	especially if it is free! And the best meals can be found 
	in the trash cans behind restaurants. Dr. Zoidberg has surveyed 
	the city's restaurants and over many months has collected 
	extensive data on the number of customers a restaurant serves
	during the day together with the quantity of tasty treats that
	can be found in the restaurant's trash can at the end of the
	day. Help Dr. Zoidberg make predictions about how much he can 
	expect to eat given the number of customers a restaurant serves. 
	You will train a "single neuron" to perform regression on the 
	data collected by Dr. Zoidberg.

	Input:
	The given file zdata.txt  contains the data for this 
	regression problem. The first column is the number of customers 
	a restaurant serves in a particular day. the second column is the
	number of calories that Dr. Zoidberg found at the end of the day.

	Ouput:
	SSE
	Final Weight vector
'''
from random import randint

print "CS-5001 : HW#1 : Regression with one variable."
print "Programmer: Ronith Muttur \n"

#Open file and initialize variables
f = open("zdata.txt","r")
inputs = []
y = []
werror = [0.0,0.0]
sum_of_squares = []
final_ycap = [] # for plotting the final y predicteds
w = [randint(1,20000),randint(1,20000)]
eta = 0.001
iterations = 1500


print "Learning rate eta = ", eta
print "After %d iterations:" %iterations

#import your input data into memory
for row in f.readlines():
	inputs.append(int(row.split("\t")[0]))
	y.append(int(row.split("\t")[1]))

#iterations loop            
for i in range(iterations):
	#Update the error vector by calculating ycap for each data entry
	for example in range(len(inputs)):
		ycap = w[0] * 1 + w[1] * inputs[example]
		werror[0] = werror[0] + (y[example] - ycap) * 1
		werror[1] = werror[1] + (y[example] - ycap) * inputs[example]
	#Update the weights vector with the normalized error 
	for j in range(2):
		werror[j] = (1.0/len(inputs)) * werror[j]
		w[j] = w[j] + eta * werror[j]
	#for the last iteration in the loop make a final ycap list
	#along with sum of squares calculated using the final weights
	if i == iterations - 1:
		for example in range(len(inputs)):
			ycap = w[0] * 1 + w[1] * inputs[example]
			delta = y[example] - ycap
			final_ycap.append(ycap)
			sum_of_squares.append(delta ** 2) 
		
print "Sum of Squares Errors = %f" %sum(sum_of_squares)
print "Weights:"
print "w0 = %f \nw1 = %f" %(w[0],w[1])
