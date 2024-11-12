import re
import string

filename = "input.txt"
input = []
with open(filename) as file:
    input = [line.strip() for line in file.readlines()]

def possiblesymbols(line,span):
    possiblesymbols = []
    for column in range(span[0]-1,span[1]+1):
        possiblesymbols.append(f"{line-1},{column}")
        possiblesymbols.append(f"{line+1},{column}")
    possiblesymbols.append(f"{line},{span[0]-1}")
    possiblesymbols.append(f"{line},{span[1]}")
    return possiblesymbols
    
def part1():
    symbolindices = []
    partsindices = []
    validparts = []
    lineindex = 1
    for line in input:
        for item in [m.start(0) for m in re.finditer(r'[^0-9\.]', line)]:
            symbolindices.append(f"{lineindex},{item}")
        for decimal,span in [(m[0],m.span()) for m in re.finditer(r'\d+', line)]:
            partsindices.append(f"{decimal};{lineindex};{span}")
        lineindex += 1
    for part in partsindices:
        decimal,line,span = part.split(";")
        for x in possiblesymbols(int(line),eval(span)):
            if x in symbolindices:
                validparts.append(int(decimal))
                break
    return sum(validparts)

def part2():
    symbolindices = []
    ratios = {}
    gearratios = 0
    partsindices = []
    validparts = []
    lineindex = 1
    for line in input:
        for item in [m.start(0) for m in re.finditer(r'[^0-9\.]', line)]:
            symbolindices.append(f"{lineindex},{item}")
        for decimal,span in [(m[0],m.span()) for m in re.finditer(r'\d+', line)]:
            partsindices.append(f"{decimal};{lineindex};{span}")
        lineindex += 1
    for part in partsindices:
        decimal,line,span = part.split(";")
        for x in possiblesymbols(int(line),eval(span)):
            if x in symbolindices:
                try:
                    ratios[x].append(decimal)
                except KeyError:
                    ratios[x] = [decimal]        
    for possiblegear in ratios:
        if len(ratios[possiblegear]) == 2:
            gearratios += int(ratios[possiblegear][0])*int(ratios[possiblegear][1])
    return gearratios
print("Part one:", part1())
print("Part two:", part2())