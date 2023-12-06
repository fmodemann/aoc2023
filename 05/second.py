def map_seed(seed: int, mapping: [int]) -> int:
    return seed + mapping[0] - mapping[1]


def get_intersection_range(range1: [int], range2: [int]) -> [int]:
    # Calculate the intersection range
    intersection_start = max(range1[0], range2[0])
    intersection_end = min(range1[1], range2[1])

    # Check if the ranges are intersecting
    if intersection_end >= intersection_start:
        return [intersection_start, intersection_end]
    else:
        return []  # No intersection


with open('sample_data.txt', 'r') as file:
    lines = file.readlines()

# first line
firstLine = lines[0].strip().split(':')
seeds = firstLine[1].strip().split(' ')
seeds = [int(x) for x in seeds]
extendedList = [[seeds[x], seeds[x] + seeds[x + 1] - 1] for x in range(0, len(seeds), 2)]

# get mappings
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

# solve problem
for mappingKey, mappingGroup in maps.items():
    print(mappingKey, len(extendedList))
    for seedRange in extendedList.copy():
        for mapping in mappingGroup:
            intersection = get_intersection_range(seedRange, [mapping[1], mapping[1] + mapping[2]])
            if intersection:
                print(seedRange, intersection, mapping)
                extendedList.remove(seedRange)
                newRanges = [[seedRange[0], intersection[0] - 1] if (seedRange[0] < intersection[0]) else None,
                             [map_seed(intersection[0], mapping), map_seed(intersection[1], mapping)],
                             [intersection[1] + 1, seedRange[1]] if (seedRange[1] > intersection[1]) else None]
                print('new1: ', newRanges)
                newRanges = [r for r in newRanges if (r is not None) and (r[0] <= r[1])]
                print('new2: ', newRanges, '\n')
                extendedList.extend(newRanges)
                break

print(min([x[0] for x in extendedList]))
