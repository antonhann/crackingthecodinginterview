"""
Palindrome Permutation: Given a string, write a function to check if it is a permutation of a palindrome. A palindrome is a word or phrase that is the same forwards and backwards. A permutation
is a rearrangement of letters. The palindrome does not need to be limited to just dictionary words.
1.5
1.6
EXAMPLE
Input: Tact Coa
Output: True (permutations: "taco cat", "atco eta", etc.)
Hints: #106, #121, #134, #136
"""
import collections
import check as check
def palindromePermutation(string):
    string = string.lower()
    freqCount = collections.defaultdict(int)
    for i in string:
        if i.isalpha():
            freqCount[i] += 1
    hasOneOdd = False
    for count in freqCount.values():
        if count % 2 == 1:
            if hasOneOdd:
                return False
            hasOneOdd = True
    return True

testcase = [
    "Tact Coa"
]

shouldBe = [
    True
]

check.checkOneParam(testcase,shouldBe,palindromePermutation)



    