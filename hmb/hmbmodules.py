#!/usr/bin/python env

#####################################################################
#
# Tilte: Hidz My Biz Modules
# File: hmbmodules.py
# Creator: Ellis, Kevin
# Date: 20180722
# Version: 1
# Description: hmbm.py contains the mocules for the main HidzMyBiz
#              program.
#
######################################################################

from random import randint
from string import printable
###############################################


# begin encode
def encodeInText(msg, fname): # function encodes msg into a random string of printable ascii characters
    cover=[] # creates a stego 8 times the length of the msg to hide encode the message into
    for x in range(len(msg) * 8):
        #cover.append(chr(randint(65, 122)))
        cover.append(printable[randint(0, len(printable[:-7]))])
        
    coverbin = [format(ord(x) , '0>8b') for x in cover] # Gets the binary representation of stego       
    index = 0 # will be the place holder for the stegobin index

    for char in msg:
        charbin = format(ord(char), '0>8b') # gets the binary representation of each character in msg
        for bit in charbin:
            coverlist=list(coverbin[index])
            coverlist[-1] = bit
            coverbin[index]=''.join(coverlist)
            index += 1

    with open(fname, 'w') as f:
        for x in coverbin:
            f.write(chr(int(x, 2)))
                        
# end encode
################################################


# begin decode
def decode(fname):
    with open(fname, 'r') as f:
        stego=f.read() # get a list form of the encoded message
        stegolist=list(stego)
    msg=[]
    msgbin=[]
    for char in stegolist:
        stegobin=format(ord(char), '0>8b')
        msgbin.append(stegobin[-1])
        if len(msgbin) == 8:
            msg.append(chr(int(''.join(msgbin), 2))) # gets each character from the encoded mesage
            msgbin=[] # resets the msgbin

    return ''.join(msg)
    
#end decode

#def main():

