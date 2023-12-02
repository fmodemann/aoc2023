import re

endResult = 0

with open('sample_data.txt', 'r') as file:
    for line in file:
        withoutPrefix = line.split(':').pop()
        test = re.split(r'[,;]', withoutPrefix)
        maxValues = {
            'red': 0,
            'green': 0,
            'blue': 0
        }
        for pair in test:
            value, color = pair.split()
            maxValues[color] = max(maxValues[color], int(value))
        gameResult = 1
        for value in maxValues.values():
            gameResult *= value
        endResult += gameResult

print(endResult)
