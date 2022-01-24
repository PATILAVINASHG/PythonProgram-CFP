
"""
   * Author - Avinash patil
   * Date -  24-01-2022
   * Time -  12.01pm
   * Title - SumOfInteger add to zero
"""

arr = [ 0, -1, 2 , -3 ,1 , 3, 4, 5]
count = 0
for i in range(len(arr)):
    for j in range(1,len(arr)):
        for k in range(2,len(arr)):
            s=(arr[i]+arr[j]+arr[k])
            if s==0:
                count+=1
                print(arr[i],arr[j],arr[k])
print(count,"triplet exists")