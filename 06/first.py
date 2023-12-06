with open('sample_data.txt', 'r') as file:
    lines = file.readlines()

times = lines[0].strip().split(':')[1].strip().split()
distances = lines[1].strip().split(':')[1].strip().split()

times = [int(x) for x in times]
distances = [int(x) for x in distances]
endResult = 1

for n in range(0, len(times)):
    counter = 0
    for j in range(1, times[n]):
        distanceTravel = j * (times[n] - j)
        if distanceTravel > distances[n]:
            counter += 1
    endResult *= counter

print(endResult)
