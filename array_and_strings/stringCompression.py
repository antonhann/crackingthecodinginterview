import check as check
def stringCompression(string):
    curr = 0
    res = ""
    while curr < len(string):
        currChar = string[curr]
        res += currChar
        length = 0
        while curr < len(string) and string[curr] == currChar:
            length += 1
            curr += 1
        res += str(length)
    print(res)
    return res
testcases = [
    "aabcccccaaa"
]

shouldBe = [
    "a2b1c5a3"
]

check.checkOneParam(testcases,shouldBe,stringCompression)