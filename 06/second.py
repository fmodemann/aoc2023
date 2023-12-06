import time

with open('sample_data.txt', 'r') as file:
    lines = file.readlines()

start_time = time.time()
total_time = int(lines[0].strip().split(':')[1].strip().replace(' ', ''))
distance = int(lines[1].strip().split(':')[1].strip().replace(' ', ''))

top = 0
bottom = 0
for j in range(1, total_time):
    distanceTravel = j * (total_time - j)
    if distanceTravel > distance:
        bottom = j
        break

for j in range(total_time, bottom, -1):
    distanceTravel = j * (total_time - j)
    if distanceTravel > distance:
        top = j + 1
        break

end_time = time.time()
elapsed_time = end_time - start_time
print(elapsed_time, 'seconds -----', top - bottom)
