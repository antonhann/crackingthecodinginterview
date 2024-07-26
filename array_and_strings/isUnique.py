"""
1.1 Is Unique: Implement an algorithm to determine if a string has all unique characters. What if you
cannot use additional data structures? 
Hints: #44, #117, #732  
"""
import check as check
def isUniqueWDSA(string):
    unique = set()
    for i in string:
        if i in unique:
            return False
        unique.add(i)
    return True

def isUniquewithoutDSA(string):
    string = sorted(string)
    for i in range(1,len(string)):
        if string[i - 1] == string[i]:
            return False
    return True

testcases = [
    "ABC",
    "AAC",
    "CAA",
]

shouldBe = [
    True,
    False,
    False   
]

check.checkOneParam(testcases,shouldBe,isUniqueWDSA)
check.checkOneParam(testcases,shouldBe,isUniquewithoutDSA)