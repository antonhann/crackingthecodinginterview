import check as check
import collections
def oneAway(one,two):
    freqOne = collections.defaultdict(int)
    freqTwo = collections.defaultdict(int)
    for i in one:
        freqOne[i] += 1
        freqTwo[i] = 0
    for i in two:
        if i not in freqOne:
            freqOne[i] = 0
        freqTwo[i] += 1
    movedUsed = 0
    for letter, count in freqOne.items():
        difference = count - freqTwo[letter]
        movedUsed += difference
        if movedUsed > 1 or movedUsed < -1:
            return False
    return True
print(oneAway("pal","pale"))