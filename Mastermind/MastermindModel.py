from colorama import *
import random
import sys


#this on is for data logic

ALLOWEDNUMBERS = "0123456789"




def getAllowed():
    return ALLOWEDNUMBERS    

def setMaster(word):
    global masterword 
    masterword = word
    setMasterWithLength(len(str(masterword)))

def getMaster():
    return masterword    

def setMasterWithLength(x):
    global masterLength
    masterLength = x

def getMasterLength():
    return masterLength

def setNumberOfGuesses(x):
    global NumberGuesses
    NumberGuesses = int(x)

def getNumberOfGuesses():
    return NumberGuesses    

               
def setDifficulty(x):
    global difficulty
    difficulty = ""
    match x:
        case "1":
            setMasterWithLength(5)
            difficulty = "1"
            setNumberOfGuesses(10)
        case "2":
            setMasterWithLength(6)
            difficulty = "2"
            setNumberOfGuesses(9)
        case "3":
            setMasterWithLength(7)
            difficulty = "3"
            setNumberOfGuesses(8)        

    

def getDifficulty():
    return difficulty    



