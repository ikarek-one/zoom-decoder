"""
This mini-programme can format your copied Zoom chat into easier to read.
Please note that it does not include info about the message author.
LP, 06.03.2021
"""

print("Decoding Zoom chat .txt-s")

fileName = input("Enter the name (or path) of your .txt file! \n")
stream = open(fileName,'r').read()

print("your file consists of " + str(len(stream)) + " words \n\n")

lines = stream.split("\n")
text = []
for line in lines:
    line = line.split(" ")
    flag = False

    for jj in range(len(line)):
        if(flag):
            text.append(line[jj])
        if(line[jj] == ":"):
            flag = True

    if(not flag):
        for jj in range(len(line)):
            text.append(line[jj])

    text.append("\n")


dialogue = ""
for w in text:
    dialogue = dialogue + w + " "

print(dialogue)


isEnd = " "
while(isEnd != "end"):
    isEnd = input("Enter 'end' to finish the programme: \n ")


