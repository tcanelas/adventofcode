import re

filename = "input.txt"
input = []
with open(filename) as file:
    input = [line.strip() for line in file.readlines()]

def conversion(source,sourcetodest):
    for a in sourcetodest:
        if source in range(a[1],a[1]+a[2]):
            return a[0]+(source-a[1])
    return source
def mypart1():
    seeds = []
    seedtosoil = []
    soiltofertilizer = []
    fertilizertowater = []
    watertolight = []
    lighttotemperature = []
    temperaturetohumidity = []
    humiditytolocation = []
    locations = []
    current = ""
    for line in input:
        if "seeds" in line:
            seeds = re.findall(r'\d+',line.split(":")[1])
        if "seed-to-soil" in line:
            current = "seedtosoil"
            continue
        if "soil-to-fertilizer" in line:
            current = "soiltofertilizer"
            continue
        if "fertilizer-to-water" in line:
            current = "fertilizertowater"
            continue
        if "water-to-light" in line:
            current = "watertolight"
            continue
        if "light-to-temperature" in line:
            current = "lighttotemperature"
            continue
        if "temperature-to-humidity" in line:
            current = "temperaturetohumidity"
            continue
        if "humidity-to-location" in line:
            current = "humiditytolocation"
            continue
        if line == "":
            current = ""
        elif current != "":
            eval(current).append([int(x) for x in line.split(" ")])
    for seed in seeds:
        locations.append(conversion(conversion(conversion(conversion(conversion(conversion(conversion(int(seed),seedtosoil),soiltofertilizer),fertilizertowater),watertolight),lighttotemperature),temperaturetohumidity),humiditytolocation))
    return min(locations)

# def mypart2():
#     seedsranges = []
#     seeds = []
#     global seedtosoil
#     global soiltofertilizer
#     global fertilizertowater
#     global watertolight
#     global lighttotemperature
#     global temperaturetohumidity
#     global humiditytolocation
#     seedtosoil = []
#     soiltofertilizer = []
#     fertilizertowater = []
#     watertolight = []
#     lighttotemperature = []
#     temperaturetohumidity = []
#     humiditytolocation = []
#     locations = []
#     current = ""
#     for line in input:
#         if "seeds" in line:
#             seedsranges = re.findall(r'\d+',line.split(":")[1])
#         if "seed-to-soil" in line:
#             current = "seedtosoil"
#             continue
#         if "soil-to-fertilizer" in line:
#             current = "soiltofertilizer"
#             continue
#         if "fertilizer-to-water" in line:
#             current = "fertilizertowater"
#             continue
#         if "water-to-light" in line:
#             current = "watertolight"
#             continue
#         if "light-to-temperature" in line:
#             current = "lighttotemperature"
#             continue
#         if "temperature-to-humidity" in line:
#             current = "temperaturetohumidity"
#             continue
#         if "humidity-to-location" in line:
#             current = "humiditytolocation"
#             continue
#         if line == "":
#             current = ""
#         elif current != "":
#             eval(current).append([int(x) for x in line.split(" ")])
#     for x in range(0,len(seedsranges)):
#         if x%2 == 0:
#             for y in range(int(seedsranges[x]),int(seedsranges[x])+int(seedsranges[x+1])):
#                 seeds.append(y)
#     print(seeds)
#     # for seed in seeds:
#     #     locations.append(location(humidity(temperature(light(water(fertilizer(soil(int(seed)))))))))
#     return min(locations)

print("Part one:", mypart1())
# print("Part two:", mypart2())

with open('input.txt', 'r') as f:
    puzzle_input = f.read()

def part1(puzzle_input):
    segments = puzzle_input.split('\n\n')
    seeds = re.findall(r'\d+', segments[0])
    min_location = float('inf')
    for x in map(int, seeds):
        for seg in segments[1:]:
            for conversion in re.findall(r'(\d+) (\d+) (\d+)', seg):
                destination, start, delta = map(int, conversion)
                if x in range(start, start + delta):
                    x += destination - start
                    break

        min_location = min(x, min_location)

    return min_location

def part2(puzzle_input):
    segments = puzzle_input.split('\n\n')
    intervals = []

    for seed in re.findall(r'(\d+) (\d+)', segments[0]):
        x1, dx = map(int, seed)
        x2 = x1 + dx
        intervals.append((x1, x2, 1))

    min_location = float('inf')
    while intervals:
        x1, x2, level = intervals.pop()
        if level == 8:
            min_location = min(x1, min_location)
            continue

        for conversion in re.findall(r'(\d+) (\d+) (\d+)', segments[level]):
            z, y1, dy = map(int, conversion)
            y2 = y1 + dy
            diff = z - y1
            if x2 <= y1 or y2 <= x1:    # no overlap
                continue
            if x1 < y1:                 # split original interval at y1
                intervals.append((x1, y1, level))
                x1 = y1
            if y2 < x2:                 # split original interval at y2
                intervals.append((y2, x2, level))
                x2 = y2
            intervals.append((x1 + diff, x2 + diff, level + 1)) # perfect overlap -> make conversion and let pass to next nevel 
            break

        else:
            intervals.append((x1, x2, level + 1))
  
    return min_location
print("Part one:", part1(puzzle_input))
print("Part two:", part2(puzzle_input))