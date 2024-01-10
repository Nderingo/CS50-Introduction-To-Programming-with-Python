#from random import choice
import random

#coin = random.choice(["heads", "tails"])
#print(coin)

#number = random.randint(1,12)
#print(number)

cards = ["queen", "king","jack","joker"]
random.shuffle(cards)
for cards in cards:
    print(cards)