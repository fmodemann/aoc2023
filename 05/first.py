def map_seed(seed: int, mapping: [int]):
    return seed + mapping[0] - mapping[1]


# Read the input file
with open('sample_data.txt', 'r') as file:
    lines = file.readlines()

# first line
firstLine = lines[0].strip().split(':')
seeds = firstLine[1].strip().split(' ')
seeds = [int(x) for x in seeds]

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

location = -1
locations = []
for seed in seeds:
    location = seed
    for mappingGroup in maps.values():
        for mapping in mappingGroup:
            if (seed >= mapping[1]) & (seed <= mapping[1] + mapping[2]):
                location = map_seed(seed, mapping)
                break
        seed = location
    locations.append(location)

print(min(locations))