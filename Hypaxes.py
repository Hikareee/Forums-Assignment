#Import string library
import string
#make function
def hapax(ZaFile):
    #Declare file variable 
    file = open(ZaFile, "r", encoding='utf-8')
    #Read the file and lower everything the remove the enter and replace it with a blank
    text = file.read().lower().replace("\n","")
    #Make an empty string var
    newTxt=""
    #use a loop to check if its not in a punctuation
    for i in text:
        if i not in string.punctuation:
            newTxt += i
    #redeclarte text
    text = newTxt
    #Split the text
    list = text.split(" ")
    #Create an empty dictionary
    l = {}
    #use loop to detect how many times the word is showing
    for i in list:
        if i not in l:
            l[i] = 1
        else:
            l[i] +=1
    #Final list of words
    newl = []
    #loop to append all the words in the list
    for i in l:
        if l[i] == 1:
            newl.append(i)
    #Print em all out
    for word in newl:
        print(word)
        return(word)
hapax("Book.txt")

