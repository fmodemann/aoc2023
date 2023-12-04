endResult = 0

with open('sample_data.txt', 'r') as file:
    for line in file:
        withoutPrefix = line.replace(':', '|').split('|')[1:3]
        strList = [withoutPrefix[0].strip().split(' '), withoutPrefix[1].split(' ')]
        winnerNumbers = [int(x) for x in strList[0] if x.isdigit()]
        drawedNumbers = [int(x) for x in strList[1] if x.strip().isdigit()]

        counter = 0
        for drawedNumber in drawedNumbers:
            if drawedNumber in winnerNumbers:
                counter += 1

        if counter != 0:
            endResult += pow(2, counter - 1)

print(endResult)
