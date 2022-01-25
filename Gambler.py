"""
   * Author - Avinash patil
   * Date -  24-01-2022
   * Time -  1.30pm
   * Title - Gambler program
"""

import random
def Gambler ( stake, goal,):
        bet =1
        win = loss = temp = 0
        while stake <= goal :
            if(random.random() >=  0.5 ):
                win +=1
                stake += bet
                print("stake is : ", stake)
                if(stake == goal):
                     break
            else:
                loss += 1
                stake -= bet
                print("Stake is : " , stake)
                if(stake == 0):
                    break
        temp = win+loss
        print("Win percentage:" ,(win /temp )*100)
        print("Loss percentage",(loss / temp)*100)
        print(stake)
Gambler(1, 100)
