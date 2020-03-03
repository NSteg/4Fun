#!/usr/bin/python
##########***************************************
#####-Nicholas-Stegelman-************************
#####-Created:2020-02-09-************************
#####-"Keep Talking and No One Explodes":-*******
#####-"On The Subject of Passwords"-Solver-******
###-A toy program that is intended to aid in-****
#-the solving of the password modules in the-****
#-game, "Keep Talking and No one Explodes".-*****
#-The program asks for the first two rotors and-*
#-narrows the permutations to the subset used-***
#-by the game to use as keyes. The program then-*
#-executes a dictionary call based on the two-***
#-letter key and returns the possible strings.-**
#-In some cases the program may ask for the-*****
#-third rotor when amassing keyes.-**************
#####-Updated:2020-02-21-************************
#####-Version:1.01-******************************

import argparse
import types

helpmsg = "usage: ./[programName] [opts] \n Options: \n -h : Help; prints help information on this program. \n -v : Verbose; Prints usage instructions during all steps of program execution. \n \n "

words={
  "ab": "about",
  "af": "after",
  "ag": "again",
  "be": "below",
  "co": "could",
  "ev": "every",
  "fi": "first",
  "fo": "found",
  "gr": "great",
  "ho": "house",
  "la": "large",
  "le": "learn",
  "ne": "never",
  "ot": "other",
  "pl": "place/plant",
  "po": "point",
  "ri": "right",
  "sm": "small",
  "so": "sound",
  "sp": "spell",
  "st": "still/study",
  "th": "their/there/these/thing/think/three",
  "wa": "water",
  "wh": "where/which",
  "wo": "world/would",
  "wr": "write"
}

def rotIn():
    rotorString = input("$>")
    #print(rotorString) # TEST PRINT
    rotorString = rotorString.lower()
    rotorString = ''.join(sorted(rotorString))
    #print(rotorString) # TEST PRINT
    return rotorString
# END_FUNC: rotIn()

def firstRotor(rotorString):
    candidateString = ""
    for can in rotorString:
        #print(can) # TEST PRINT
        if can in "dijkmquvxyz":
            #print(can) # TEST PRINT
            continue
        else:
            candidateString = candidateString + can
        # END_IF
    # END_LOOP
    return candidateString
# END_FUNC: firstRotor()

def secondRotor(rotorString):
    candidateString = ""
    for can in rotorString:
        #print(can) # TEST PRINT
        if can in "cdjknqsuwxyz":
            #print(can) # TEST PRINT
            continue
        else:
            candidateString = candidateString + can
        # END_IF
    # END_LOOP
    return candidateString
# END_FUNC: secondRotor()

# TODO: Add methods for thirdRotor and fourth

def search3(rotCom):
    rotThree = rotIn()
    #TODO: Make dictionaries for three letters

def search4(rotCom):
    rotFour = rotIn()
    #TODO: Make dictionary for four letters

def search2(rotorOne, rotorTwo):
    for lett in rotorOne:
        for tter in rotorTwo:
            sigil = lett + tter
            if sigil in words:
                print("Your Password is: ", words[sigil])
            else:
                continue
            # END_IF
        # END_LOOP
    # END_LOOP
# END_FUNC: search2()

#++++++++++Main_Function_Block++++++++++
parser = argparse.ArgumentParser(description='This program is intended for use with the game "Keep Talking and No One Explodes". It takes two strings of 5 characters -- no white spaces -- from the rotors of the "On the Subject of Passwords" module. The program then generates a sorted list of dictionary keyes and and returns the match(es). In the Event that the matched key has more than one associated word, the program may ask for the thrid rotor before providing more instructions.')

parser.add_argument("-v", "--verbose", help="Prints additional messages.", action="store_true")

args = parser.parse_args()

if args.verbose == True:
    print("Hello World")
    print("What is the first rotor? -- No whitespaces.")
    rotOne = rotIn()
    rotOne = firstRotor(rotOne)
    print("What is the second rotor? -- No whitespaces.")
    rotTwo = rotIn()
    rotTwo = secondRotor(rotTwo)
    # print(rotOne, "+", rotTwo) # TEST PRINT
    search2(rotOne, rotTwo)
    print("Buh-Bye")
else:
    rotOne = rotIn()
    rotOne = firstRotor(rotOne)
    
    rotTwo = rotIn()
    rotTwo = secondRotor(rotTwo)
    # print(rotOne, "+", rotTwo) # TEST PRINT
    search2(rotOne, rotTwo)
# END_IF

#++++++++++END_OF_MAIN_FUNCTION_BLOCK++++++++++
