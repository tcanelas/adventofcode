import re

filename = "input.txt"
input = []
with open(filename) as file:
    input = [line.strip() for line in file.readlines()]

def part1():
    score = 0
    for line in input:
        winningcards = re.findall(r'\d+',line.split(":")[1].split("|")[0])
        mycards = re.findall(r'\d+',line.split(":")[1].split("|")[1])
        number = len(list(set(winningcards) & set(mycards)))
        if number > 0:
            score += pow(2,number-1)
    return score

def part2():
    cards = {}
    for x in range(1,len(input)+1):
        cards[x] = 1
    for line in input:
        card = int(line.split(":")[0].replace("Card","").strip())
        winningcards = re.findall(r'\d+',line.split(":")[1].split("|")[0])
        mycards = re.findall(r'\d+',line.split(":")[1].split("|")[1])
        number = len(list(set(winningcards) & set(mycards)))
        for j in range(0,cards[card]):
            for i in range(1,number+1):
                cards[card+i] +=1
    return sum(cards.values())

print("Part one:", part1())
print("Part two:", part2())