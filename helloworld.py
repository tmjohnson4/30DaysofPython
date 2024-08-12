import math
print('Hello 30 days of Python challenge')

#Day 1

#simple arithmatic operators
print(2+3) #addition(+)
print(3-1) #subtraction (-)
print(3*2) #multipication (*)
print(3/2) #division (/)
print(3**2) #exponests (**)
print(3%2)  #mod(%)
print(3//2) #floor division operator(//)

#Checking data types
print(type(10)) #int
print(type(3.14)) #float
print(type(1 + 5j)) #complex number
print(type('Trinity')) #string
print(type([1,1,2,3])) #list
print(type({'name': 'Trinity'})) #dictionary
print(type({2,3,5,7})) #set
print(type((2,3,5,7))) #tuple


#Find Eclidian distance between (2,3) and (10,8
#euclidian distance: square root of (p1 -q1)^2+(p2-q2)^2
print(math.sqrt((2-10)**2+(3-8)**2)) #distance using formula
print(math.dist((2,3), (10,8))) #distance using function 