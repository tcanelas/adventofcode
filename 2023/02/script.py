import re

filename = "input.txt"
input = []
with open(filename) as file:
    input = [line.strip() for line in file.readlines()]

def part1():
    max = {
        "red" : 12,
        "green" : 13,
        "blue": 14
    }
    ids = []
    impossibleids = []
    for line in input:
        id = int(line.split(':')[0].replace("Game ",""))
        ids.append(id)
        games = line.split(':')[1].split(';')
        for game in games:
            if re.search(r'\d+ blue', game) is not None:
                blue = int(re.search(r'(?P<blue>\d+) blue', game).group('blue'))
            else:
                blue = 0
            if re.search (r'\d+ red', game) is not None:
                red = int(re.search(r'(?P<red>\d+) red', game).group('red'))
            else:
                red = 0
            if re.search(r'\d+ green', game) is not None:
                green = int(re.search(r'(?P<green>\d+) green', game).group('green'))
            else:
                green = 0
            if red > max['red'] or blue > max['blue'] or green > max['green']:
                impossibleids.append(id)
    setids = {s for s in ids}
    setimpossibleids = {s for s in impossibleids}
    possibleids = {s for s in setids - setimpossibleids}
    return sum(possibleids)

def part2():
    powers = []
    for line in input:
        games = line.split(':')[1].split(';')
        maxred = 0
        maxblue = 0
        maxgreen = 0
        for game in games:
            if re.search(r'\d+ blue', game) is not None:
                blue = int(re.search(r'(?P<blue>\d+) blue', game).group('blue'))
            else:
                blue = 0
            if re.search (r'\d+ red', game) is not None:
                red = int(re.search(r'(?P<red>\d+) red', game).group('red'))
            else:
                red = 0
            if re.search(r'\d+ green', game) is not None:
                green = int(re.search(r'(?P<green>\d+) green', game).group('green'))
            else:
                green = 0
            if red > maxred : maxred = red
            if blue > maxblue : maxblue = blue
            if green > maxgreen : maxgreen = green
        power = maxred*maxgreen*maxblue
        powers.append(power)
    return sum(powers)
print("Part one :",part1())
print("Part two :", part2())