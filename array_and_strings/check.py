def checkOneParam(cases, expected_results, function):
    isCorrect = True
    for i in range(len(cases)):
        print(function(cases[i]), expected_results[i])
        if function(cases[i]) != expected_results[i]:
            isCorrect = False
            break
    print("Algorithm is correct" if isCorrect else "Algorithm is incorrect")

def checkTwoParam(cases, expected_results, function):
    isCorrect = True
    for i in range(len(cases)):
        one = cases[i][0]
        two = cases[i][1]
        if function(one,two) != expected_results[i]:
            isCorrect = False
            break
    print("Algorithm is correct" if isCorrect else "Algorithm is incorrect")

