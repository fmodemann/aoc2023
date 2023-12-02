colorRestrictions = {
    'red': 12,
    'green': 13,
    'blue': 14
}

endResult = 0

with open('sample_data.txt', 'r') as file:
    for line in file:
        withoutPrefix = line.removeprefix('Game ').split(':')
        gameIndex = int(withoutPrefix.pop(0))
        gameSets = withoutPrefix.pop(0).strip().split(";")
        addIndex = True
        for gameSet in gameSets:
            drawDict = {}
            for draw in gameSet.strip().split(','):
                drawedColors = draw.strip().split()
                drawDict[drawedColors.pop()] = int(drawedColors.pop(0))
            for color, cubeAmount in colorRestrictions.items():
                if drawDict.get(color, 0) > cubeAmount:
                    addIndex = False
                    break
        if not addIndex:
            continue
        endResult += gameIndex

print(endResult)
