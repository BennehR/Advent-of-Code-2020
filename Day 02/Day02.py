from datetime import datetime

with open("G:\Benneh\Documents\Projects\Python\Advent of Code 2020\Day 02\input.txt", "r") as f:
    inputlist = f.readlines()
inputcount = len(inputlist)

#Part 1

clock1start = datetime.now()

#Set global variables
validpassword = 0

for line in inputlist:
    #Set variables
    targetcount = 0

    #Split the input string into 3 usable chunks
    linesplit = line.split(" ")
    
    #Set limit variables
    limits = linesplit[0].split("-")
    lowerlimit = int(limits[0])
    upperlimit = int(limits[1])

    #Set target char
    targetchar = linesplit[1].strip(":")
    print(f"target character is \'{targetchar}\' between {lowerlimit}-{upperlimit}")

    #Set password string
    pwstring = linesplit[2].strip()

    #Compute
    for letter in pwstring:
        if letter is targetchar:
            targetcount += 1
    
    if targetcount < lowerlimit:
        print(f"{pwstring} invalid, too few {targetchar}\'s")
    elif targetcount > upperlimit:
        print(f"{pwstring} invalid, too many {targetchar}\'s")
    else:
        validpassword += 1
        print(f"{pwstring} is a valid password")

print(f"{validpassword} valid passwords\n")

clock1end = datetime.now()

#Part 2

clock2start = datetime.now()

#Set global variables
validpassword = 0

for line in inputlist:
    #Set variables
    targetcount = 0

    #Split the input string into 3 usable chunks
    linesplit = line.split(" ")
    
    #Set limit variables
    limits = linesplit[0].split("-")
    firstlocation = int(limits[0]) - 1
    secondlocation = int(limits[1]) - 1

    #Set target char
    targetchar = linesplit[1].strip(":")
    print(f"target character is \'{targetchar}\' in places {lowerlimit} OR {upperlimit}")

    #Set password string
    pwstring = linesplit[2].strip()

    #Compute
    if pwstring[firstlocation] is targetchar and pwstring[secondlocation] is targetchar:
        print(f"{pwstring} invalid, both locations contain \'{targetchar}\'")
    elif (pwstring[firstlocation] is targetchar and pwstring[secondlocation] is not targetchar) or (pwstring[firstlocation] is not targetchar and pwstring[secondlocation] is targetchar):
        print(f"{pwstring} is a valid password")
        validpassword += 1
    else:
        print(f"{pwstring} invalid, neither location contained \'{targetchar}\'")

print(f"{validpassword} valid passwords")

clock2end = datetime.now()
print(f"\nPart 1 took {clock1end - clock1start} to complete")
print(f"Part 2 took {clock2end - clock2start} to complete")