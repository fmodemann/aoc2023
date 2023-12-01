endResult = 0

with open('sample_data.txt', 'r') as file:
    for line in file:
        numbersInLine = ''.join(filter(str.isdigit, line))
        if numbersInLine:
            endResult += int(numbersInLine[0] + numbersInLine[-1])

print(endResult)
