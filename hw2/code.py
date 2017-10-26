''' Logistic Regression
	CS-5001 : HW#2 
	Submission : T220010242017
	Author : Ronith Muttur
	Problem designed by Dr. Ricardo Morales
'''

'''
	Name: Logistic Regression, and pizzas.... and cats.

	Problem Description:
	Dr. Farnsworth is exploring a new venture to fund his research:
	Pizzas for Cats!  Earth cats that is, not evil space cats. In 
	order to develop the most tasty and acceptable toppings for his 
	pizza-for-cats, Dr. Farnsworth has tested multiple different 
	topping combinations against test subject cats, and recorded if 
	the combination was or was not accepted by the test subjects. 
	Now, he wants to train a predictor from the gathered data. Help 
	Dr. Farnsworth build a predictor to know whether a topping 
	combination will be accepted by cats. You will train a 
	"single neuron" to perform logistic regression on the data 
	collected by Dr. Farnsworth.

	Input:
	The given file  pizzacatdata.txt  contains the data for this logistic 
	regression problem. Each row of the data file consists of 5 boolean 
	[0,1] values. The first 4 values indicate weather the pizza tested 
	had Pepperoni, Sausage, Mushroom and Cheese, the last value indicates 
	whether the cat subject accepted the pizza (1) or not (0).

	Ouput:
	SSE
	Final weight vector

	** SPECIAL NOTE!! **: NO CATS WERE HURT GATHERING THIS DATA :P
'''

'''
	Algorithmic implementation note: 
	The activation function used is sigmoid. So the gradient was 
	calculated using the derivative of sigmoid (which is f(x)*(1-f(x)).
	And because of lack of precision (derivative of sigmoid becomes 
	either 0 or 1) and the weights being initialized 
	randomly betweem -100 and 100 the weight updation are very small, 
	which results in large sse. The work around for this is to
	intitialize the weights in such a way as to maximize the output
	from the derivative of sigmoid function, which peaks at x = 0.5
'''
from random import randint
import math

print "CS-5001 : HW#2 : Logistic Regression."
print "Programmer: Ronith Muttur"
print "No cats were hurt gathering this data. \n"

eta = 0.05
iterations = 5000
X = []
w = [0]*5
sse = []
Y = []

def sigmoid(x):
	# to avoid math range error on large negative x
	if x < 0:
		return round(1 - 1/(1 + math.exp(x)), 12) 
  	else:
		return round(1/(1 + math.exp(-x)), 12)

def z(it):
	out  = w[0] * 1
	for i in range(len(X[it])):
		out += X[it][i] * w[i + 1]
	return out

f = open("pizzacatdata.txt","r")

for i in range(5):
	w[i] = randint(-100,100)

print "Using Learning rate eta = ", eta
print "After %d iterations:" %iterations

# parse input
for line in f.readlines():
	inputs = line.split(" ")
	temp = []
	for it in range(len(inputs)-2):
		temp.append(int(inputs[it]))
	X.append(temp)
	Y.append(int(inputs[4]))  

# Logistic Regression
for i in range(iterations):

	for it in range(len(X)):
		ycap = sigmoid(z(it))
		error = Y[it] - ycap
		w[0] = w[0] + eta * error * ycap * (1 - ycap)
		for k in range(len(X[it])):
			w[k+1] = w[k+1] + eta * error * ycap * (1 - ycap) * X[it][k]
	# Calculate Sum of Squares Errors in the last iteration
	if(i == iterations - 1):
		for it in range(len(X)):
			ycap = sigmoid(z(it))
			sse.append((Y[it] - ycap)**2)

print "Sum of Squares Errors = ",sum(sse)
print "Weights:"
for i in range(5):
	print "w%d = %f"%(i,w[i])