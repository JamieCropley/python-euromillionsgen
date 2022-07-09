import random

def lottoGen():
    
    mainNums = (random.sample(range(1, 50), 5))
    luckyNums = (random.sample(range(1, 12), 2))

    # 5 Main numbers from 1 to 50
    print(mainNums)
    
    # 2 Lucky stars numbers from 1 to 12
    print(luckyNums)
    
    
lottoGen()

while True:
   answer = input('Do you want to continue? y to generate again n to exit:')
   if answer.lower().startswith("y"):
      lottoGen()
   elif answer.lower().startswith("n"):
      print("Created by @JamieCropley if you win send me some money!")
      exit()