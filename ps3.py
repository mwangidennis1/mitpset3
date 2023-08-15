# 6.0001 Problem Set 3
#
# The 6.0001 Word Game
# Created by: Kevin Luu <luuk> and Jenna Wiens <jwiens>
#
# Name          : <your name>
# Collaborators : <your collaborators>
# Time spent    : <total time>

import math
import random
import string

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10,'*':0
}

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)

WORDLIST_FILENAME = "words.txt"

def load_words():
   
    
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.append(line.strip().lower())
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def get_frequency_dict(sequence):
    
    
    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq
	

# (end of helper code)
# -----------------------------------

#
# Problem #1: Scoring a word
#
def get_word_score(word, n):
    s=list(word.lower())
    k=[]
    for x in SCRABBLE_LETTER_VALUES:
        if x in s:
            p=s.count(x)
            k.append(p*SCRABBLE_LETTER_VALUES[x])
    op=7 * len(word) -3*(n-len(word))  
    if(op <1):
        op =1
    return sum(k) * op       
      
    

#
# Make sure you understand how this function works and what it does!
#
def display_hand(hand):
   
    
    for letter in hand.keys():
        for j in range(hand[letter]):
             print(letter, end=' ')      # print all on the same line
    print()                              # print an empty line

#
# Make sure you understand how this function works and what it does!
# You will need to modify this for Problem #4.
#
def deal_hand(n):
    
    hand={}
    num_vowels = int(math.ceil(n / 3))

    for i in range(num_vowels-1):
        x = random.choice(VOWELS)
        hand[x] = hand.get(x, 0) + 1
    
    for i in range(num_vowels, n):    
        x = random.choice(CONSONANTS)
        hand[x] = hand.get(x, 0) + 1
    hand["*"]=1
    return hand

#
# Problem #2: Update a hand by removing letters
#
def update_hand(hand, word):
    mycopy=hand.copy()
    myword=list(word.lower())
    for x in mycopy:
        if x in myword:
            p=myword.count(x)
            if mycopy[x] >= 1:
                mycopy[x] -= p
                if mycopy[x] < 1:
                    mycopy[x]=0
    return mycopy                

   
   

#
# Problem #3: Test word validity
#
def is_valid_word(word, hand, word_list):
    s=list(word.lower())
    occ=word.find("*")
    if occ == -1:
        pass
    else:
        mon =list(word.lower())
        for i in VOWELS:
            mon[occ] = i
            pit = ''.join(mon)
            
            if pit in word_list:
                return True
            else:
                pass    
    for x in s:
        p=s.count(x)
        if x in hand and p <= hand[x]:
            pass
        else:
            return False
    if word.lower() in word_list:
        return True
    else:
        return False                


    
#
# Problem #5: Playing a hand
#
def calculate_handlen(hand):
    
    xi=[]
    for x in hand:
        xi.append(hand[x])
    return sum(xi)    

    
   

def play_hand(hand, word_list):
    #newhand=hand
    siet=0
    score=[]
    display_hand(hand)
    inPut=str(input("Enter word, or !! to indicate that you are finished: "))
    #* When any word is entered (valid or invalid), it uses up letters from the hand.
    result =update_hand(hand,inPut)

    verifyword =is_valid_word(inPut,hand,word_list)
    if verifyword == False:
        inPut=str(input("Enter word, or s!! to indicate that you are finished: "))
    else:
        siet +=get_word_score(inPut,calculate_handlen(hand))    
        score.append(siet)
        print("Points: ", siet)
        display_hand(result)
    while(True):
    
        inPut=str(input("Enter word, or !! to indicate that you are finished: "))
        result =update_hand(result,inPut)
        print("Current hand ") 
        display_hand(result)
        if inPut == "!!":
            break
        else:
           # result =update_hand(hand,inPut)
            verifyword =is_valid_word(inPut,hand,word_list)
            if verifyword == False:
                print("That is not a valid word. Please choose another word." )
                if calculate_handlen(result) < 1:

                    print("Total score: ", sum(score))
                    return sum(score)
                    break
                inPut=str(input("Enter word, or !! to indicate that you are finished: "))
            else:
                siet=get_word_score(inPut,calculate_handlen(hand))  
                score.append(siet)  
                print("points ", siet)
                print("Total score: ", sum(score))
            if calculate_handlen(result) < 1:
                print("Ran out of letters. Total score: ", sum(score))
                return sum(score)
                break
#play_hand(deal_hand(8),load_words())







#
# Problem #6: Playing a game
# 


#
# procedure you will use to substitute a letter in a hand
#

def substitute_hand(hand, letter):
    mycopy = hand.copy()
    myletters=VOWELS+CONSONANTS
    for x in mycopy:
        if x == letter:
            guess=random.choice(myletters)
            for i in mycopy:
                if guess == i:
                    substitute_hand(hand,letter)
            if guess==letter:
                substitute_hand(hand,letter)  
            else:
                mycopy[guess] = mycopy[x]  
                del mycopy[x]  
    return mycopy               

   
       
    
def play_game(word_list):
    replayhands=0
    inputHands = int(input("Enter total number of hands:"))
    mkono=deal_hand(inputHands)
    print("Current hand: ")
    display_hand(mkono)
    
    substitute_letter= str(input("Would you like to substitute a letter? "))
    if substitute_letter == "yes":
        replacebo=str(input("Which letter would you like to replace: "))
        sub_hand= substitute_hand(mkono,replacebo)
        chebukati=play_hand(sub_hand,word_list)
        return chebukati
    elif substitute_letter == "no":
        gogni=play_hand(mkono,wordlist)
        replayhands=gogni
        substitute_replay=str(input("Would you like to replay the hand?"))
        if substitute_replay == "yes":
            yey=play_hand(mkono,wordlist)
            replayhands=max(replayhands,yey)
            return replayhands
        else:
            return replayhands    










   


#
# Build data structures used for entire session and play game
# Do not remove the "if __name__ == '__main__':" line - this code is executed
# when the program is run directly, instead of through an import statement
#
if __name__ == '__main__':
    word_list = load_words()
    play_game(word_list)
   