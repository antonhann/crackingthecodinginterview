"""
1.3 URLify: Write a method to replace all spaces in a string with '%20'. You may assume that the string
has sufficient space at the end to hold the additional characters, and that you are given the "true"
length of the string. (Note: If implementing in Java, please use a character array so that you can
perform this operation in place.)
EXAMPLE
Input: "Mr John Smith ", 13
Output: "Mr%20John%20Smith"
Hints: #53, # 118 
"""
import check as check
#my first thought but didnt use length
def URLify(string, length):
    filler = "%20"
    res = ""
    l = 0
    while l < len(string):
        if string[l] == " ":
            while l < len(string) and string[l] == " ":
                l += 1
            if l < len(string):
                res += filler
        else:
            res += string[l]
            l += 1
    return res

testcase = [
    ("Mr John Smith ", 13)
]

shouldBe = [
    "Mr%20John%20Smith"
]

check.checkTwoParam(testcase,shouldBe,URLify)



