import random
import sys
import emoji
from enum import Enum

class RPS(Enum):
  ROCK = 1 
  PEPPER = 2
  SEC = 3
welcome = '''
*************************
*        Welcome        *
*        kidus game     *
*************************
'''
print(welcome)
   
print("")
playerc = input("Enter ..\n # 1 for Rock 🪨\n # 2 for pepper 📝\n # 3 for sec 🔪\n")
play = int(playerc)
if play  | play > 3 :
 sys.exit("Choose  1-3")


computerc = random.choice("123")
computer = int(computerc)
print("You choose " +str(RPS(play)).replace("RPS.","") +"." )
print("Python choose " + str(RPS(computer)).replace("RPS.","")+"." )
if play == 1 and computer == 3:
  print("🎉 You win ")
elif play == 2 and computer == 1:
  print("🎉 You win")
elif play == 3 and computer == 2:
 print("🎉 You win")
elif play == computer :
 print("😒 Tig game")
else:
  print("🐍 Python win")
