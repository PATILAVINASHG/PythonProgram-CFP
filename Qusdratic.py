"""
   * Author - Avinash patil
   * Date -  24-010=-2022
   * Time -  11.32AM
   * Title - Quadratic
"""
import cmath

b = int(input("Enter the value of b : "))
a = int(input("Enter the value of a : "))
c= int(input("Enter the value of c : "))

delta =(b*b - (4*a*c))

root1 = (-b+(cmath.sqrt(delta)))/(2*a)
root2 = (-b-(cmath.sqrt(delta)))/(2*a)

print("Root 1 is  = " , root1)
print("Root 2 is  = " , root2)