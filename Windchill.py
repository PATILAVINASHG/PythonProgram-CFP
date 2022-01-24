"""
   * Author - Avinash patil
   * Date -  24-01-2022
   * Time -  12.01pm
   * Title - WindChill
"""
import math
try:
    t_tempreture = int(input("Enter the Tempreture in Fahranheit: "))
    v_windspeed = int(input("Enter the Wind Speed in miles per hours: "))

    effective_tempreture = (35.74 + 0.6215 * t_tempreture + (0.4275 * t_tempreture - 35.75) * v_windspeed ** 0.16)

    if (t_tempreture < 50 and (v_windspeed < 120 or v_windspeed > 3)):
        print(effective_tempreture)
    else:
        print(" condition not met please enter angain ")
except Exception as e:
    print("Enter int value", e)
