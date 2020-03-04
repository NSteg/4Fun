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
#####-Version:2.00.10-***************************
#####-Updated:2020-03-03-************************

import argparse
import os
import types

helpmsg = "usage: ./[programName] [opts] \n Options: \n -h : Help; prints help information on this program. \n -v : Verbose; Prints usage instructions during all steps of program execution. \n \n "

#TODO; for Ver. 2: Convert dictionary 'words' into a list.
#   create checks fo each rotor
#   Write operations for 'Verbose mode' then copy into silent

# List of possible solutions to KTANE Passwords module
words=["about", "after", "again", "below", "could", "every", "first", "found", "great", "house", "large", "learn", "never", "other", "place", "plant", "point", "right", "small", "sound", "spell", "still", "study", "their", "there", "these", "thing", "think", "three", "water", "where", "which", "world", "would", "write"]

# define our clear function 
def clear(): 
  
    # for windows 
    if os.name == 'nt': 
        _ = os.system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = os.system('clear') 

def removeDuplicates(listofElements):
    
    # Create an empty list to store unique elements
    uniqueList = []
    
    # Iterate over the original list and for each element
    # add it to uniqueList, if its not already there.
    for elem in listofElements:
        if elem not in uniqueList:
            uniqueList.append(elem)
    
    # Return the list of unique elements        
    return uniqueList

def rotIn():
    rotorString = input("$>")
    #print(rotorString) # TEST PRINT
    rotorString = rotorString.lower()
    rotorString = ''.join(sorted(rotorString))
    #print(rotorString) # TEST PRINT
    return rotorString
# END_FUNC: rotIn()

def firstRotor(rotorString): # String
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

def secondRotor(rotorString): # String
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

def thirdRotor(rotorString): # String
    candidateString = ""
    for can in rotorString:
        #print(can) # TEST PRINT
        if can in "bcdfjkmnpqswxyz":
            #print(can) # TEST PRINT
            continue
        else:
            candidateString = candidateString + can
        # END_IF
    # END_LOOP
    return candidateString
# END_FUNC: thirdRotor()

def fourthRotor(rotorString): # String
    candidateString = ""
    for can in rotorString:
        #print(can) # TEST PRINT
        if can in "bfjkmpqvwxyz":
            #print(can) # TEST PRINT
            continue
        else:
            candidateString = candidateString + can
        # END_IF
    # END_LOOP
    return candidateString
# END_FUNC: fourthRotor()

def fifthRotor(rotorString): # String
    candidateString = ""
    for can in rotorString:
        #print(can) # TEST PRINT
        if can in "abcfijmopqsuvxy":
            #print(can) # TEST PRINT
            continue
        else:
            candidateString = candidateString + can
        # END_IF
    # END_LOOP
    return candidateString
# END_FUNC: fifthRotor()

def search(rotorOne, rotorTwo, verbosity, round): #String, String, Boolean, unsigned Int
    wList = []
    for lett in rotorOne:
        for tter in rotorTwo:
            sigil = lett + tter
            wList.append(sigil)
        # END_LOOP_INNER
    # END_LOOP_OUTER
    for lead in wList:
        for word in words:
            if lead in word[0:round]:
                if verbosity == True:
                    print("Your Password is: ", word)
                else:
                    print("+++", word)
            else:
                continue
            # END_IF
        #END_LOOP_INNER
    # END_LOOP_OUTER
    return wList
# END_FUNC: search2()

#++++++++++Main_Function_Block++++++++++
def main():
    parser = argparse.ArgumentParser(description='This program is intended for use with the game "Keep Talking and Nobody Explodes". It takes two strings of 5 characters -- no white spaces -- from the rotors of the "On the Subject of Passwords" module. The program then generates a sorted list of dictionary keyes and and returns the match(es). In the Event that the matched key has more than one associated word, the program may ask for the thrid rotor before providing more instructions.')

    parser.add_argument("-v", "--verbose", help="Prints additional messages.", action="store_true")

    args = parser.parse_args()

    if args.verbose == True:
        print("What is the first rotor? -- No whitespaces.")
        rotOne = rotIn()
        rotOne = firstRotor(rotOne)
        print("What is the second rotor? -- No whitespaces.")
        rotTwo = rotIn()
        rotTwo = secondRotor(rotTwo)
        #print(rotOne, "+", rotTwo) #TEST PRINT
        searchList = search(rotOne, rotTwo, args.verbose, 2)
        
        print("What is the third rotor? -- No whitespaces.")
        rotThree = rotIn()
        if (len(rotThree) == 0):
          return None
        rotThree = thirdRotor(rotThree)
        searchList = search(searchList, rotThree, args.verbose, 3)
        
        print("What is the fourth rotor? -- No whitespaces.")
        rotFour = rotIn()
        if (len(rotFour) == 0):
          return None
        rotFour = fourthRotor(rotFour)
        searchList = search(searchList, rotFour, args.verbose, 4)
        
        print("What is the fifth rotor? -- No whitespaces.")
        rotFive = rotIn()
        if (len(rotFive) == 0):
          return None
        rotFive = fifthRotor(rotFive)
        searchList = search(searchList, rotFive, args.verbose, 5)
    else:

        rotOne = rotIn()
        rotOne = firstRotor(rotOne)

        rotTwo = rotIn()
        rotTwo = secondRotor(rotTwo)

        #print(rotOne, "+", rotTwo) # TEST PRINT
        searchList = search(rotOne, rotTwo, args.verbose, 2)

        rotThree = rotIn()
        if (len(rotThree) == 0):
          return None
        rotThree = thirdRotor(rotThree)
        searchList = search(searchList, rotThree, args.verbose, 3)
        
        rotFour = rotIn()
        if (len(rotFour) == 0):
          return None
        rotFour = fourthRotor(rotFour)
        searchList = search(searchList, rotFour, args.verbose, 4)
        
        rotFive = rotIn()
        if (len(rotFive) == 0):
          return None
        rotFive = fifthRotor(rotFive)
        searchList = search(searchList, rotFive, args.verbose, 5)
    # END_IF

#++++++++++END_OF_MAIN_FUNCTION_BLOCK++++++++++
if __name__ == "__main__":
    while True:
        clear()
        main()
        exitVar = input("Press 'q' to Quit, Anything else Continues... ")
        if exitVar == 'q':
          exit()
    # END_WHILE
# END_IF