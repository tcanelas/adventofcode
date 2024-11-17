import re

filename = "input.txt"
input = []
with open(filename) as file:
    input = [line.strip() for line in file.readlines()]

def part1():
    order_list = 'AKQJT98765432'
    hands = {
        1 : [], # High Card
        2 : [], # One pair
        3 : [], # Two pairs
        4 : [], # Three of a kind
        5 : [], # Full house
        6 : [], #Four of a kind
        7 : [] # Five of a kind
    }
    total = 0
    for line in input:
        hand,bid = line.split(" ")
        hand2 = {
            "A" : 0,
            "K" : 0,
            "Q" : 0,
            "J" : 0,
            "T" : 0,
            "9" : 0,
            "8" : 0,
            "7" : 0,
            "6" : 0,
            "5" : 0,
            "4" : 0,
            "3" : 0,
            "2" : 0
        }
        for letter in hand:
            hand2[letter] += 1
        match max(set(hand2.values())):
            case 5:
                hands[7].append({"hand":hand,"bid":bid})
            case 4:
                hands[6].append({"hand":hand,"bid":bid})
            case 3 if 2 in hand2.values():
                hands[5].append({"hand":hand,"bid":bid})
            case 3 if 2 not in hand2.values():
                hands[4].append({"hand":hand,"bid":bid})
            case 2 if list(hand2.values()).count(2) == 2:
                hands[3].append({"hand":hand,"bid":bid})
                continue
            case 2 :
                hands[2].append({"hand":hand,"bid":bid})
            case 1:
                hands[1].append({"hand":hand,"bid":bid})
            case _:
                raise Exception(f"Hand {hand} not recognized")
    multiplier = len(input)
    for type in reversed(range(1,8)):
        hands[type].sort(key=lambda x:[order_list.index(y) for y in x["hand"]])
        for hand in hands[type]:
            total += int(hand["bid"])*multiplier
            multiplier -= 1
    return total

def part2():
    order_list = 'AKQT98765432J'
    hands = {
        1 : [], # High Card
        2 : [], # One pair
        3 : [], # Two pairs
        4 : [], # Three of a kind
        5 : [], # Full house
        6 : [], #Four of a kind
        7 : [] # Five of a kind
    }
    total = 0
    for line in input:
        hand,bid = line.split(" ")
        hand2 = {
            "A" : 0,
            "K" : 0,
            "Q" : 0,
            "T" : 0,
            "9" : 0,
            "8" : 0,
            "7" : 0,
            "6" : 0,
            "5" : 0,
            "4" : 0,
            "3" : 0,
            "2" : 0
        }
        hand2J = 0
        for letter in hand:
            if letter == "J":
                hand2J +=1
            else:
                hand2[letter] += 1
        match max(set(hand2.values()))+hand2J:
            case 5:
                hands[7].append({"hand":hand,"bid":bid})
            case 4:
                hands[6].append({"hand":hand,"bid":bid})
            case 3 if 2 in hand2.values() and hand2J != 1:
                hands[5].append({"hand":hand,"bid":bid})
            case 3 if list(hand2.values()).count(2) == 2 and hand2J == 1:
                hands[5].append({"hand":hand,"bid":bid})
            case 3 if 2 in hand2.values() and hand2J == 1:
                hands[4].append({"hand":hand,"bid":bid})
            case 3 if 2 not in hand2.values():
                hands[4].append({"hand":hand,"bid":bid})
            case 2 if list(hand2.values()).count(2) == 2:
                hands[3].append({"hand":hand,"bid":bid})
                continue
            case 2 :
                hands[2].append({"hand":hand,"bid":bid})
            case 1:
                hands[1].append({"hand":hand,"bid":bid})
            case _:
                raise Exception(f"Hand {hand} not recognized")
    multiplier = len(input)
    for type in reversed(range(1,8)):
        hands[type].sort(key=lambda x:[order_list.index(y) for y in x["hand"]])
        for hand in hands[type]:
            print(type,hand,multiplier,total)
            total += int(hand["bid"])*multiplier
            multiplier -= 1
    return total

print("Part one:", part1())
print("Part two:", part2())