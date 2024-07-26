"""
1.2 Check Permutation: Given two strings, write a method to decide if one is a permutation of the
other.
Hints: #7, #84, #722, #737 
"""

import collections
import check as check
def checkPermuation(wordOne, wordTwo):
    freqOne = collections.defaultdict(int)
    freqTwo = collections.defaultdict(int)
    for i in wordOne:
        freqOne[i] += 1
    for i in wordTwo:
        freqTwo[i] += 1
    return freqOne == freqTwo


testcases = [
    ("abc","abc"),
    ("abca","abc"),
    ("ab", "ba"),
]

shouldBe = [
    True,
    False,
    True   
]

check.checkTwoParam(testcases,shouldBe,checkPermuation)