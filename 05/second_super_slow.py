import sys

import numpy as np


def map_seed(seed: int, mapping: [int]) -> int:
    return seed + mapping[0] - mapping[1]


# Read the input file
with open('sample_data.txt', 'r') as file:
    lines = file.readlines()

# first line
firstLine = lines[0].strip().split(':')
seeds = firstLine[1].strip().split(' ')
seeds = [int(x) for x in seeds]
extendedList = []
for i in range(0, len(seeds), 2):
    extendedList = np.append(extendedList, np.arange(seeds[i], seeds[i] + seeds[i + 1]))

maps = {}
current_map = None

for line in lines:
    if line.strip().endswith(" map:"):
        map_name = line.split(' map:')[0]
        current_map = []
        maps[map_name] = current_map
    elif (current_map is not None) & (line.strip() != ''):
        values = list(map(int, line.strip().split()))
        current_map.append(values)
smallestLocation = sys.maxsize
location = 0
for seedIndex, seed in enumerate(extendedList):
    location = seed
    for mappingGroup in maps.values():
        for mapping in mappingGroup:
            if (seed >= mapping[1]) & (seed <= mapping[1] + mapping[2]):
                location = map_seed(seed, mapping)
                break
        seed = location

    smallestLocation = location if location < smallestLocation else smallestLocation
    print(seedIndex / len(extendedList) * 100, "%")
print(smallestLocation)
