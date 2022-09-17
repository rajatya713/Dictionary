import difflib
import json

from difflib import get_close_matches

data = json.load(open("dictionary.json"))
active=True

    
def ret_def(word):
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    
##    len > 0 because we can print only when the word has 1 or more close matches.
##    In the return statement, the last [0] represents the
##    first element from the list of close matches
    
    elif len(get_close_matches(word,data.keys())[0])>0:
        
        act=input(f"Did you mean {get_close_matches(word,data.keys())[0]} instead!! y or n :")
        if act=="y":
            return data[get_close_matches(word, data.keys())[0]]
        elif act=="n":
            return "The word cannot be found."
    
    else:
        return("Word not found.")
    
while active:    
    word=input("\tEnter a word: ")
    word=word.lower()
    output=ret_def(word)
    if type(output)==list:
        for elmt in output:
            print("- ",elmt)
    else:
        print("- ",output)      

    x=input("\n\nIf you want to continue press Enter else press any other key : ")
    if x!="":
        active=False
