from colorama import *
import random
import sys


#this on is for data logic


ALLOWEDNUMBERS = "0123456789"


def getAllowed():
    return ALLOWEDNUMBERS

def getMaster():
    return masterword    

def setMaster(word):
    global masterword 
    masterword = word
               


if __name__ == "__main__":
    print(" " + Fore.RED + "e", end='' )



