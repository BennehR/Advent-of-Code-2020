from datetime import datetime

with open("G:\Benneh\Documents\Projects\Python\Advent of Code 2020\Day 01\input.txt", "r") as f:
    inputlist = f.readlines()
inputcount = len(inputlist)
targetnum = 2020

clockstart = datetime.now()

for firstnum in inputlist:
    for listindex in range(inputcount):
        firstnum = int(firstnum)
        secnum = int(inputlist[listindex])
        numsum = firstnum + secnum
        if numsum != targetnum:
            continue # numbers did not equal 2020
        else:
            numsum = firstnum * secnum
            print(f"{firstnum} + {secnum} = 2020")
            print(f"multiplied = {numsum}")
            break # answer found
    else:
        continue # only continues to the next loop if nested loop did not break
    break # breaks the nested loops as the answer has been found

clockfinish = datetime.now()
difference = clockfinish - clockstart
print(f"Time taken: {difference}\n")

clockstart = datetime.now()

for firstnum in inputlist:
    for listindex1 in range(inputcount):
        for listindex2 in range(inputcount):
            firstnum = int(firstnum)
            secnum = int(inputlist[listindex1])
            thirdnum = int(inputlist[listindex2])
            numsum = firstnum + secnum + thirdnum
            if numsum != targetnum:
                continue
            else:
                numsum = firstnum * secnum * thirdnum
                print(f"{firstnum} + {secnum} + {thirdnum} = 2020")
                print(f"multiplied = {numsum}")
                break # answer found
        else:
            continue
        break
    else:
        continue
    break

clockfinish = datetime.now()
difference = clockfinish - clockstart
print(f"Time taken: {difference}\n")