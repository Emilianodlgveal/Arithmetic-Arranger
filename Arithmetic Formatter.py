import string


def arithmetic_arranger(problems, solve = None):
    finalList = list()
    if len(problems) > 5:
        return "Error: Too many problems."
    for problem in problems:
        if ' / ' in problem or ' * ' in problem:
            return "Error: Operator must be '+' or '-'."
    for problem in problems:
        for character in problem:
            if character in string.ascii_letters:
                return "Error: Numbers must only contain digits."
    for problem in problems:
        splPro = problem.split()
        if len(splPro[0]) > 4 or len(splPro[2]) > 4:
            return "Error: Numbers cannot be more than four digits."
    arrangement = {'Top': '', 'Operand': '', 'Middle': '', 'Bottom': '' }
    for problem in range(len(problems)):
        numbersList = problems[problem].split()
        if len(numbersList[0]) >= len(numbersList[2]):
            largest = len(numbersList[0])
            shortest = len(numbersList[2])
        else:
            largest = len(numbersList[2])
            shortest = len(numbersList[0])
        if problems[problem] == problems[-1]:
            arrangement['Top'] = int(problems[problem].split()[0])
            finalList.append(str(arrangement['Top']).rjust(2+largest) + '\n')
        else:
            arrangement['Top'] = int(problems[problem].split()[0])
            finalList.append(str(arrangement['Top']).rjust(2+largest) + '    ')
    for problem in range(len(problems)):
        numbersList = problems[problem].split()
        if len(numbersList[0]) >= len(numbersList[2]):
            largest = len(numbersList[0])
            shortest = len(numbersList[2])
        else:
            largest = len(numbersList[2])
            shortest = len(numbersList[0])
        if problems[problem] == problems[-1]:
            arrangement['Operand'] = problems[problem].split()[1]
            arrangement['Middle'] = problems[problem].split()[2]
            if largest == len(numbersList[2]) and largest is not shortest:
                finalList.append((arrangement['Operand'] + (' ') + str(arrangement['Middle'])).rjust(2+largest) + '\n')
            else:
                finalList.append((arrangement['Operand'] + (' '*(largest-shortest+1)) + str(arrangement['Middle'])).rjust(2+largest) + '\n')
        else:
            arrangement['Operand'] = problems[problem].split()[1]
            arrangement['Middle'] = problems[problem].split()[2]
            if largest == len(numbersList[2]) and largest is not shortest:
                finalList.append((arrangement['Operand'] + (' ') + str(arrangement['Middle'])).rjust(2+largest) + '    ')
            else:
                finalList.append((arrangement['Operand'] + (' '*(largest-shortest+1)) + str(arrangement['Middle'])).rjust(2+largest)+'    ')
    for problem in range(len(problems)):
        numbersList = problems[problem].split()
        if len(numbersList[0]) > len(numbersList[2]):
            largest = len(numbersList[0])
        else:
            largest = len(numbersList[2])
        if solve == True:
            if problems[problem] == problems[-1]:
                arrangement['Operand'] = problems[problem].split()[1]
                arrangement['Middle'] = problems[problem].split()[2]
                finalList.append(str('-' * int(largest) + '--').rjust(2+largest) + '\n')
            else:
                arrangement['Operand'] = problems[problem].split()[1]
                arrangement['Middle'] = problems[problem].split()[2]
                finalList.append(str('-' * int(largest) + '--').rjust(2+largest)+'    ')
        else:
            if problems[problem] == problems[-1]:
                arrangement['Operand'] = problems[problem].split()[1]
                arrangement['Middle'] = problems[problem].split()[2]
                finalList.append(str('-' * int(largest) + '--').rjust(2+largest))
            else:
                arrangement['Operand'] = problems[problem].split()[1]
                arrangement['Middle'] = problems[problem].split()[2]
                finalList.append(str('-' * int(largest) + '--').rjust(2+largest)+'    ')
    if solve == True:
        for problem in range(len(problems)):
            numbersList = problems[problem].split()
            if len(numbersList[0]) >= len(numbersList[2]):
                largest = len(numbersList[0])
                shortest = len(numbersList[2])
            else:
                largest = len(numbersList[2])
                shortest = len(numbersList[0])
            arrangement['Top'] = problems[problem].split()[0]
            arrangement['Operand'] = problems[problem].split()[1]
            arrangement['Middle'] = problems[problem].split()[2]
            if problems[problem] == problems[-1] and arrangement['Operand'] == '+':
                arrangement['Bottom'] = int(arrangement['Top']) + int(arrangement['Middle'])
                finalList.append(str(arrangement['Bottom']).rjust(2 + largest))
            elif problems[problem] == problems[-1] and arrangement['Operand'] == '-':
                arrangement['Bottom'] = int(arrangement['Top']) - int(arrangement['Middle'])
                finalList.append(str(arrangement['Bottom']).rjust(2 + largest))
            elif arrangement['Operand'] == '+':
                arrangement['Bottom'] = int(arrangement['Top']) + int(arrangement['Middle'])
                finalList.append(str(arrangement['Bottom']).rjust(2+largest)+'    ')
            else:
                arrangement['Bottom'] = int(arrangement['Top']) - int(arrangement['Middle'])
                finalList.append(str(arrangement['Bottom']).rjust(2+largest)+'    ')
    return ''.join(finalList)


print(arithmetic_arranger(["11 + 4", "3801 - 2999", "1 + 2", "123 + 49", "1 - 0"]))
# print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"], True))
# print(arithmetic_arranger(["32 - 698", "1 - 3801", "45 + 43", "123 + 49"], True))

