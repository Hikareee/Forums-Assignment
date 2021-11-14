def numbered_lines(text):
    #Open the file in readmode 
    file = open(text,"r",encoding='UTF-8')
    #read the file and split the texts for each time \n(enter) happens
    f = file.read().split('\n')
    #starting value of number lables
    num = 1
    #Printing loop
    for i in f:
        #if exception for i is not empty to make sure the loop is not infinite
        if i != '':
            #format the print to have the number first and add 1 for each loop to num
            print(f'{num}. {i}')
            num += 1
    #close the file
    file.close()
#run it
numbered_lines("sampletext.txt")