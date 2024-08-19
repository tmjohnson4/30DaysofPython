#30 days of python challange
#day 3

age = 21
my_height = 5.5
num_complex = 3 +4j
base = int(input("Enter base: "))
height = int(input("Enter height: "))
area = 0.5 * base * height
print("The area of the triangle is ", area)



print(len('python'))
print(len('dragon'))
print(len('dragon')> len('python'))

#see of substring is in string 
print('on is in pythone and dragon', 'on' in 'python' and 'on' in 'dragon')
print('jargon' in 'I hope this course is not full of jargon')

#change type of input
len_py = len('pyton')
print(len_py)
print(type(len_py))
len_py = float(len_py)
print(len_py)
print(type(len_py))
len_py = str(len_py)
print(len_py)
print(type(len_py))

#is number even or odd
num = int(input("Ener a number to see of its even: "))
print(num%2 == 0)

#calulate pay of person
hours = int(input("Enter hours: "))
rate = int(input('Enter rate per hour: '))
print("Your weekly earing is : ", hours*rate)

years = int(input('Enter number of years: '))
years_in_seconds = years * 31536000
print('You have lived for ' + years_in_seconds + 'seconds')