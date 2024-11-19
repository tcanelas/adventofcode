import re
from math import lcm
from functools import reduce

filename = "input.txt"
input = []
with open(filename) as file:
    input = [line.strip() for line in file.readlines()]


def part1():
    instructions = input[0]
    start = "AAA"
    step = 0
    end = start
    map = {}
    for line in input[2:]:
        key,left,right = re.findall(r"(\w+)",line)
        map[key] = {'L' : left,'R' : right}
    while end != "ZZZ":
        end = map[end][instructions[step%len(instructions)]]
        step += 1
    return step

def part2():
    instructions = input[0]
    map = {}
    for line in input[2:]:
        key,left,right = re.findall(r"(\w+)",line)
        map[key] = {'L' : left,'R' : right}
    starts = [x for x in map.keys() if x[2] == "A"]
    ends = []
    for start in starts:
        step = 0
        while start[2] != "Z":
            start = map[start][instructions[step%len(instructions)]]
            step += 1
        ends.append(int(step))
    return reduce(lambda a,b: lcm(a,b), ends)

print("Part one:", part1())
print("Part two:", part2())