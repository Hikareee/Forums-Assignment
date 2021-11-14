def average_word(text):
    #Open the file on read mode with UTF-8 encoding style 
    file = open(text, "r",encoding="UTF-8")
    #Read through the file and split the words
    f = file.read().split()
    #Get the length of the index and use it to get the length of all the word with the for loop
    #Divide the result with the length of f (the number of words) to know the average length of every word
    average = sum(len(i)for i in f)/len(f)
    #print it out
    return (average)
result = average_word("sampletext.txt")
print (result)