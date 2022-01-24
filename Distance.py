
"""
   * Author - avinash patil
   * Date -  24-01-2022
   * Time -  11.00AM
   * Title - Distance Program
"""
import math

x1 = int(input("Enter the value of point x1 :"))
y1 = int(input("Enter the value of point y1 :"))

x = 0
y = 0

dis = ((y1 * y1 - y * y) + (x1 * x1 - x * x))
print(  "Distance Is = " +  str(math.sqrt(dis)))