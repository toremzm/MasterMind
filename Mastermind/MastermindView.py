from colorama import *
from os import system
from time import sleep
from MastermindControl import *
from MastermindModel import *

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

        print("\n         the masterword is made up of these :  	" + " ".join(ALLOWEDNUMBERS) + "     numbers. \n         it is 5 numbers long.\n")

        #start control
        start()
        for i in range(1,11):
            print("\n")
            print("             this is your " + str(i) + " guess")
            guess = input("             please input your guess :")

            if(inputControl(guess) == 1):
                print("\n") #to start a new line
                print("                 ", end='')
                for i in range(0,5):
                    x = checkInput(guess[i], i)
                    
                    if(x == 0):
                        print(" " + Fore.RED + guess[i], end='' )
                    elif(x == 2):
                        print(" " + Fore.GREEN + guess[i], end='' )
                    elif(x == 1):
                        print(" " + Fore.YELLOW + guess[i], end='' ) 

                if(guess == getMaster()):
                    print("\n")
                    print("             Congrats, you've won")
                    end()


            elif(inputControl(guess) == 0):  #to not progress the for loop
                i -= i -1
        if(guess != getMaster):        
            print("you suck, git gud")      
            end() 


#funny response
    else:
        print("oh, you think you're reeeaaallyy funny huh?")
        main()

if __name__ == "__main__":
    main()
    
