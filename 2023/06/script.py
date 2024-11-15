import re

filename = "input.txt"
input = []
with open(filename) as file:
    input = [line.strip() for line in file.readlines()]

def ways(totaltime):
    ways = []
    for timehold in range(0,totaltime+1):
        ways.append(timehold * (totaltime-timehold))
    return ways
    

def part1():
    beatwaysproduct = 1
    times = re.findall(r"\d+", input[0])
    distances = re.findall(r"\d+", input[1])
    for x in range(0,len(times)):
        beatwaysproduct *= len([y for y in ways(int(times[x])) if y > int(distances[x])])
    return beatwaysproduct

def part2():
    time = int(re.search(r"\d+", input[0].replace(" ",""))[0])
    distance = int(re.search(r"\d+", input[1].replace(" ",""))[0])
    iterator = 0
    while distance > iterator*(time-iterator):
        iterator += 1
    return time-2*iterator+1

print("Part one:", part1())
print("Part two:", part2())
