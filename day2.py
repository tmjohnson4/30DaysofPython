#30 days of python
#day 2

#Variables
import math

first_name = 'Trinity'
last_name = 'Johnson'
full_name = 'Trinity Johnson'
country = "US"
age = 21
year = 2024
is_married = False
is_true = True
is_light_no = False
day, month, time_zone = 13, 'August', 'Mountain'

print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_no))
print(type(day))
print(type(month))
print(type(time_zone))


print(len(first_name))
print(len(last_name))
print(max(len(first_name), len(last_name)))

num_one = 5
num_two = 4
total = num_one + num_two
print(total)
var_diff = num_two - num_one
var_product = num_one*num_two
var_division = num_one/num_two
var_remainder = num_two%num_one
var_exp = num_one**num_two

print(var_diff, var_product, var_division, var_remainder, var_exp)

area_of_circle = 3.14*(30**2)
print(area_of_circle)
circum_of_circle = 2*3.14*30
print(circum_of_circle)

radius = input("Enter the radius of a circle:" )
radius = int(radius)
area_of_circle = 3.14*(radius**2)
print(area_of_circle)
