import re

filename = "input.txt"
input = []
with open(filename) as file:
    input = [line.strip() for line in file.readlines()]

def buildsublist(list):
    start = list[0]
    output = []
    for elem in list[1:]:
        output.append(elem-start)
        start = elem
    return output      

def last_element(list):
    tab = []
    tab.append(list)
    while any(tab[-1]):
        tab.append(buildsublist(tab[-1]))
    last = 0
    tab.reverse()
    for elem in tab:
        if elem != 0:
            elem.append(last+elem[-1])
            last = elem[-1]
        else :
            elem.append(0)
    return tab[-1][-1]

def first_element(list):
    tab = []
    tab.append(list)
    while any(tab[-1]):
        tab.append(buildsublist(tab[-1]))
    first = 0
    tab.reverse()
    for elem in tab:
        if elem != 0:
            elem.insert(0,elem[0]-first)
            first = elem[0]
        else :
            elem.append(0)
    return tab[-1][0]

def part1():
    values = []
    lastelem = 0
    for line in input:
        values.append(list(map(int,re.findall(r"-?\d+",line))))
    for line in values:
        lastelem += last_element(line)
    return lastelem

def part2():
    values = []
    firstelem = 0
    for line in input:
        values.append(list(map(int,re.findall(r"-?\d+",line))))
    for line in values:
        firstelem += first_element(line)
    return firstelem

print("Part one:", part1())
print("Part two:", part2())