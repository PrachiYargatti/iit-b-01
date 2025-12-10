import arithmetic
import geometry as geo
from geometry import calc_rect_area, calc_rect_peri

print("hello world")

num1 = int(input("enter num1 : "))
num2 = int(input("enter num2 : "))
arithmetic.add(num1,num2)
arithmetic.subtract(num1,num2)

l = int(input("enter length: "))
b = int(input("enter breadth: "))
calc_rect_area(l,b)
calc_rect_peri(l,b)