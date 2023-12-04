endResult = 0
lines = []
with open('sample_data.txt', 'r') as file:
    for line in file:
        lines.append([1, line])

for lineNumber, line in enumerate(lines):
    withoutPrefix = line[1].replace(':', '|').split('|')[1:3]
    strList = [withoutPrefix[0].strip().split(' '), withoutPrefix[1].split(' ')]
    winnerNumbers = [int(x) for x in strList[0] if x.isdigit()]
    drawedNumbers = [int(x) for x in strList[1] if x.strip().isdigit()]

    counter = 0
    for drawedNumber in drawedNumbers:
        if drawedNumber in winnerNumbers:
            counter += 1

    if counter != 0:
        for n in range(counter):
            lines[lineNumber + n + 1][0] += 1 * (line[0])
    endResult += line[0]

print(endResult)
