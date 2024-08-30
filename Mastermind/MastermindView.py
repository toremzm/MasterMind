from colorama import *
from os import system
from time import sleep
from MastermindControl import *
from MastermindModel import *
from getpass import getpass

#this is one is for UI

#that the colors reset after each use
init(autoreset=True)


#just ui things to explain the game
def main():  

    print("Type Start to begin the game")
    text = input("")
    if (text.lower() == "start"):
        print("\033[2;37;40m THE GAME IS MASTERMIND\033[0;37;40m \n")
        print("      your goal is to guess the random word chosen at the start. \n      you have 10 tries.\n")
        print(Fore.GREEN    + "         This means the character is at the correct spot")
        print(Fore.RED      + "         This means the character is not in the word")
        print(Fore.YELLOW   + "         This means the character is at the wrong spot, but in the word")


        mult = input("\n         will you play singleplayer or multiplayer? \n         please type in 1 for singleplayer or 2 for multiplayer \n            in singleplayer a code will be chosen at random. \n            in multiplayer another player will choose the code \n \n            your choice : ")
        while(mult not in ["1","2"]):
            mult = input("\n            please type in 1 for singleplayer or 2 for multiplayer")

        while(mult == "2"):
            code = int(getpass("\n             please type in your secret code. it can be 5 to 7 digits long. \n            you always have 8 guesses \n \n              "))
            if(len(str(code)) in [5,6,7]):
                setMaster(code)
                setNumberOfGuesses(8)
                break
              
        if(mult == "1"):
            dif = input("           please type your chosen difficulty \n           1. Easy \n           2. Middle \n           3. Hard \n \n           your chosen difficulty : ")
            i = 0
            while(dif not in ["1","2","3"]):
                print("\n          please input 1 , 2 or 3")
                dif = input("\n           choose your difficulty : ")

            setDifficulty(dif)    


        print("\n         the masterword is made up of these :  	" + " ".join(ALLOWEDNUMBERS) + "     numbers. \n         it is " +  str(getMasterLength()) + " numbers long.\n         please type in a " + str(getMasterLength()) + " digit long number")
        print("\n         you have " + str(getNumberOfGuesses()) +" tries.\n")
        
        #start control
        start(mult)
        if (mult == 2):
            setMaster(code)
        a = 0
        i = 1
        while(i < getNumberOfGuesses()+1): # so it iterates 10 times on easy and 9 times on middle and 8 times on hard
            print("\n")
            print("             this is your " + str(i) + " guess")      
            guess = input("             please input your guess : ")

            if(inputControl(guess) == 1):
                print("\n") #to start a new line
                print("                 ", end='')
                i = i +1
                for a in range(getMasterLength()):
                    
                    x = checkInput(guess[a], a)
                    
                    if(x == 0):
                        print(" " + Fore.RED + guess[a], end='' )
                    elif(x == 2):
                        print(" " + Fore.GREEN + guess[a], end='' )
                    elif(x == 1):
                        print(" " + Fore.YELLOW + guess[a], end='' ) 

                if(guess == str(getMaster())):
                    print("\n")
                    print("             Congrats, you've won")
                    end()


            elif(inputControl(guess) == 0):  #to not progress the for loop
                print("\n             please input a " + str(getMasterLength())+" digit long number")

        if(guess != str(getMaster())):        
            print("\n \n             you suck, git gud")      
            end() 


#funny response
    else:
        print("oh, you think you're reeeaaallyy funny huh?")
        main()

if __name__ == "__main__":
    main()
    
