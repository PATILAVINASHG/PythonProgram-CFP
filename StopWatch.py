"""
   * Author - Avinash patil
   * Date -  24-01-2022
   * Time -  5.10 PM
   * Title - Stopwatch
"""

import time
input("press enter key to star the time ")
start_time = time.time()
input("press Enter key to stop the time ")
end_time = time.time()
elapsed_time = end_time - start_time

print("The time elasped is : " , elapsed_time , "ms")






