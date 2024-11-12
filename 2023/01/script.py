import re

def transformtoints(string,length):
    tomodify = string[:length]
    tokeep = string[length:]
    string = tomodify.replace("one","1").replace("two","2").replace("three","3").replace("four","4").replace("five","5").replace("six","6").replace("seven","7").replace("eight","8").replace("nine","9") + tokeep
    if length < len(string) :
        return transformtoints(string,length+1)
    else :
        return string

def searchints(string):
    return list(map(int, re.findall(r'\d+', string)))

def formatlist(list):
    newlist = []
    for elem in list:
        if(elem > 9):
            newlist += [int(i) for i in str(elem)]
        else:
            newlist.append(elem)
    return newlist
            

def mypart1(filename):
    sum = 0
    file = open(filename, mode='r')
    for line in file.readlines():
        list = formatlist(searchints(line))
        sum += int(str(list[0])+str(list[-1]))
    print("MyPart one: %d" % sum)
    file.close()
    
def mypart2(filename):
    sum = 0
    file = open(filename, mode='r')
    for line in file.readlines():
        list = formatlist(searchints(transformtoints(line,0)))
        sum += int(str(list[0])+str(list[-1]))
    print("MyPart two: %d" % sum)
    file.close()
    
mypart1('./input.txt')
mypart2('./input.txt')

# Not mine
filename = "input.txt"
input = []
with open(filename) as file:
    input = [line.strip() for line in file.readlines()]
    
def part1():
    total = 0
    for line in input:
        line = re.sub('\D', '', line)       # remove non-digits from string
        nums = int(line[0] + line[-1])      # retain only first and last digit, convert to integer
        total += nums                       # add to running total
    return total

def part2():
    values = {
        "one": "1", 
        "two": "2", 
        "three": "3", 
        "four": "4", 
        "five": "5", 
        "six": "6", 
        "seven": "7", 
        "eight": "8", 
        "nine": "9"
        }
    pairs = []
    for line in input:
        digits = []
        # start at the first letter and move through it letter by letter.
        # this is the only way i've found to account for overlapping words.
        # an example is "oneight", which only matches "one" when using re.findall.
        for i,c in enumerate(line):
            if line[i].isdigit():
                digits.append(line[i])
            else:
                for k in values.keys():
                    if line[i:].startswith(k):
                        digits.append(values[k])
        pairs.append(int(f"{digits[0]}{digits[-1]}"))
    return sum(pairs)

print("Part one:", part1())
print("Part two:", part2())