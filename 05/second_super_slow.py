import sys
import numpy as np
import threading


def map_seed(seed: int, mapping: [int]) -> int:
    return seed + mapping[0] - mapping[1]


def process_seeds(start_index, end_index, extendedList, maps):
    global smallestLocation
    for seedIndex in range(start_index, end_index):
        seed = extendedList[seedIndex]
        location = seed
        for mappingGroup in maps.values():
            for mapping in mappingGroup:
                if mapping[1] <= seed <= mapping[1] + mapping[2]:
                    location = map_seed(seed, mapping)
                    break
            seed = location

        smallestLocation = location if location < smallestLocation else smallestLocation


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

# Number of threads
num_threads = 200  # You can adjust this as needed

# Divide the work among threads
thread_list = []
seed_count = len(extendedList)
chunk_size = seed_count // num_threads

for i in range(num_threads):
    start = i * chunk_size
    end = (i + 1) * chunk_size if i < num_threads - 1 else seed_count
    thread = threading.Thread(target=process_seeds, args=(start, end, extendedList, maps))
    thread_list.append(thread)

# Start the threads
for thread in thread_list:
    thread.start()

# Wait for all threads to finish
for thread in thread_list:
    thread.join()

print("Smallest Location:", smallestLocation)
