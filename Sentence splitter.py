    #open the file
def sentencesplit(text):
    f=open(text,"r",encoding="utf-8")
    txt=f.read().split()
    #Exceptions of titles 
    exceptions=["Mr.","Jr.","Ms.","Mrs.","Dr."]
    new_text=""
    for word in txt:
        if "?" not in word and "!" not in word:
            #appending the word to the new text
            new_text+=(word + " ")
            #to check whether we want to add a line break or not
            #strip checks the front and back of the string for the specified character
            #if the fullstop is in between two words it splits it and passes it
            if "." in word.strip(".") and word not in exceptions:
                pass
            #then if its in the end or in index -1 and its not part of an exception it presses enter on it making a new line
            elif "." in word[-1] and word not in exceptions:
                new_text+="\n"
        #add word + enter 
        else:
            new_text+=(word + "\n")
    #print it
    print(new_text)
sentencesplit("sampletext2.txt")
