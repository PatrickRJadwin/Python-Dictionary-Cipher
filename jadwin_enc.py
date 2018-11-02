# Name: Patrick Jadwin
# Class: CITC 1317
# Date: Nov 2, 2018

# Import external dictionary for encapsulating encryption
from encryption import encrypt as e  # delete 'as e' to reverse encryption
import argparse
import sys
import re


# Error checking for correct file
if len(sys.argv) < 2:
    print('You must specify a file to encrypt')
    exit(0)
if len(sys.argv) > 2:
    print('You can only pass one argument')
    exit(0)
if not re.match(".*\.txt", sys.argv[1]):
    print('not a text file')

# Check for duplicate values in encryption dictionary
count = 0
for k, v in e.items():
    for key, val in e.items():
        if v is val:
            count += 1
        if count > 1:
            print('Duplicate value found')
            print(v + ' appears more than once')
            exit(0)
    count = 0

words = []

# Uncomment next line to reverse encryption
# e = {v: k for k, v in encrypt.items()}

# provided file
passFile = sys.argv[1]

# store lines in array
with open(passFile, 'r') as f:
    words = f.readlines()

# split into character array
for i in range(len(words)):
    words[i] = list(words[i])

# encryption
for i in range(len(words)):
    for x in range(len(words[i])):
        if words[i][x] is "\n":
            continue
        if not re.match('[a-zA-Z]', words[i][x]):
            continue
        words[i][x] = e[words[i][x]]

encryptedWords = []

# regenerate as encrypted string
for i in range(len(words)):
    word = ''.join(words[i]) + ' '
    encryptedWords.append(word)

# newly encrypted string of text
string = ''.join(encryptedWords)

# write encrypted file
with open("encrypted_" + passFile, "w") as newFile:
    newFile.write(string)
    newFile.close()
