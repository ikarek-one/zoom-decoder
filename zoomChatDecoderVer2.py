
print("Decoding Zoom chat .txt-s")
print("Enter the name (or path) of your .txt file!")
print("Examples: myFile.txt OR C:/Documents/meeting_saved_chat.txt")
fileName = input("Name of file: \n")
if(fileName == ""):
    fileName = "meeting_saved_chat.txt"


print("\nEnter 'save' if you want to save your file. The file will be saved in the same directory ")
print("as the original file and have name <fileName>_MODIFIED.txt \n")

stream = open(fileName,'r').read()

#print("your file consists of " + str(len(stream)) + " symbols \n\n")

lines = stream.split("\n")
text = []
lastAuthor = []

for line in lines:
    line = line.split(" ")
    lineAuthor = []
    startflag = False
    endflag = False

    for word in line:
        if(endflag): #just plain message text
            text.append(word)

        if (startflag and not endflag): #an author of the current line
            lineAuthor.append(word)

        if(word == ":"): #add author name to the text and go to the message mode
            lineAuthor.append(" \n")
            if(lineAuthor != lastAuthor): #if an author wrote a few lines one by one, he'll be printed once
                lastAuthor = lineAuthor
                text.append("\n\t")
                for w in lineAuthor:
                    text.append(w.upper())
            endflag = True

        if(word == "From"): #starts 'author name' mode
            startflag = True


    if(not endflag): #if the current line hasn't got words From or : is loaded
        for w in line:
            text.append(w)

    text.append("\n") #adds the new-line symbol at the end of the line

text.append("\n\n\n\t\t END OF FILE! \n")

textAsString = ""
for word in text: #transforms a string array containing the whole result into one string
    textAsString = textAsString + word + " "


"""

print("Enter 'save' if you want to save your file. The file will be saved in the same directory as the original file and have name <fileName>_MODIFIED.txt")

print(textAsString)
isSaving = input()


"""


decision = ""

while(decision != "end"):
    decision = input("Write 'print', 'save' or 'end'! ")

    if(decision == "save"):
        newFilename: str = fileName[:-4] + "_MODIFIED.txt"

        newFile = open(newFilename, 'a')
        newFile.write(textAsString)
        newFile.close()

    if(decision == "print"):
        print(textAsString)




"""
isEnd = " "
while( != "end"): #to keep the console on and prevent from accidental closing
    isEnd = input("Enter 'end' to finish the programme: \n ")
"""


