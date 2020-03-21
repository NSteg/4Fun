#!/usr/bin/python
##########***************************************
#####-Nicholas-Stegelman-************************
#####-Created:2020-03-14-************************
#####-Cryptographic Substitution Cipher:-********
#####-Ceasar / Rotation -- Encoder/Decoder-******
###-A toy program that takes user input and-*****
#-Either encodes or decodes a user given string-*
#-By a specified number of rotations. There is-**
#-Also a 'Brute-Force' option for decoding.-*****
#####-Version:0.00.10-***************************
#####-Updated:2020-03-14-************************

parser = argparse.ArgumentParser(description='This is a simple Cryptographic program that implements a Ceasar-Cipher. This type of cipher encodes or decodes a user string using a user selected number of roations')

    parser.add_argument("-bf", "--brute", help="Attempts to Brute-force the decryption of the input string or file", action="store_true")