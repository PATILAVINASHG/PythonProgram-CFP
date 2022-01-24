
"""
   * Author - Avinash patil
   * Date -  20-01-22
   * Time -  19.10 PM
   * Title - flip coin
"""
import random

coin_head, coin_tails,time_flipped = 0 ,0, 0
while time_flipped <100:
    coin_flip = random.randrange(2)
   # print(coin_flip)
    if coin_flip == 0:
        coin_head += 1
    else:
        coin_tails += 1
    time_flipped += 1

print("out of 100 flip, " + str(coin_head ) +" % " + " of coins has head \n  " +
      str( coin_tails )+ " %" + " of coins the Tails ")
