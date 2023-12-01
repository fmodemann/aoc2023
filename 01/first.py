endResult = 0

with open('sample_data.txt', 'r') as file:
    for line in file:
        allNumbersOfLine = ''
        for char in line:
            if char.isdigit():
                allNumbersOfLine += char
        endResult += int(allNumbersOfLine[0] + allNumbersOfLine[-1])
print(endResult)
