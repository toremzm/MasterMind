from MastermindModel import *
from colorama import *
from MastermindView import *
#that the colors reset after each use
init(autoreset=True)

#this one is for controling the data


        
#is called upon running the programm
def start(x):
    if(x == "1"):
        setMaster(generate_word(getMasterLength()))


     

#generate a word with a given length , per default is 5. is called at the start
def generate_word(length):
    word = ""
    for i in range(length):
        word += random.choice(ALLOWEDNUMBERS)
    return word



#check if input meets requirements
#guess is supposed to 5 numbers long. 
#ALLOWEDNUMBER showcases the allowed numbers
def inputControl(guess):
    for char in guess:
        if(char not in ALLOWEDNUMBERS):
            return 0
           
        elif(len(guess) != getMasterLength()):
            return 0
    return 1    
    





#called upon ending the game
def end():
    raise SystemExit(0)  
         
       

#check if guess is in the masterword
def checkInput(char, i):
        if(char not in str(getMaster())): #nicht drin
            return 0
        elif(char == str(getMaster())[i]): #drin an der stelle
            return 2
        elif(char in str(getMaster())): #drin, aber nicht an der stelle
            return 1
     
  

