import random
    
win_jackpot = False

def keep_gambling():
    rand = random.randint(1, 10) # Get a random number between 1 and 10
    print(rand)
    if rand == 10: # If the random number is 10
        return True # You win the jackpot
    return False

while not win_jackpot: # While you didn't win jackpot
    win_jackpot = keep_gambling() # Keep gambling
    
print("gacor")

# Life's pro tips:
# 1. There are no losers, only winners and quitters. Keep gambling.

