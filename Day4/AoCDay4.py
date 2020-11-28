'''
Advent of Code 2019 - Day 4
'''
    
def isValidPasscode(number, part2 = False):

    hasRepeatedDigit = False
    isStrictlyIncreasing = True

    strNumber = str(number)

    for n in range(1, len(strNumber)):
        
        if not(hasRepeatedDigit) and strNumber[n] == strNumber[n-1]:
            hasRepeatedDigit = True
            
            if part2:
                if n == 1 and strNumber[2] == strNumber[0]:
                    hasRepeatedDigit = False
                elif (n >= 2 and n <= 4) and (strNumber[n-2] == strNumber[n-1] or strNumber[n+1] == strNumber[n-1]):
                    hasRepeatedDigit = False
                elif n == 5 and strNumber[4] == strNumber[3]:
                    hasRepeatedDigit = False
            
        if int(strNumber[n]) < int(strNumber[n-1]):
            isStrictlyIncreasing = False

    return len(strNumber) == 6 and number >= 138241 and number <= 674034 \
        and hasRepeatedDigit and isStrictlyIncreasing

validPassword = 0 

for guess in range(138241, 674034+1):
    if isValidPasscode(guess):
        validPassword += 1
 
print('In part 1, there are ', validPassword, ' different passcodes that meet the criteria.')

validPassword = 0

for guess in range(138241, 674034+1):
    if isValidPasscode(guess, True):
        validPassword +=1

print('In part 2, there are ', validPassword, ' different passcodes that meet the criteria.')
