import re

endResult = 0
lines = []


def look_left(line: str, index: int) -> int:
    if not line[index].isdigit():
        return index + 1
    return look_left(line, index - 1)


def look_right(line: str, index: int) -> int:
    if not line[index].isdigit():
        return index
    return look_right(line, index + 1)


def find_and_sum_substr(line: str, start: int, end: int) -> int:
    if line[start].isdigit():
        start = look_left(line, start - 1)
    if line[end].isdigit():
        end = look_right(line, end + 1)

    string_list = re.split(r'\D+', line[start: end])
    total = 0
    for item in string_list:
        try:
            total += int(item)
        except ValueError:
            continue
    return total


with open('sample_data.txt', 'r') as file:
    for line in file:
        lines.append(line)

    for lineIndex, line in enumerate(lines):
        for cIndex, c in enumerate(line):
            c = str(c)
            if (not c.isalnum()) & (c != '.') & (c != '\n'):
                # above
                if lineIndex != 0:
                    print('above:')
                    endResult += find_and_sum_substr(lines[lineIndex - 1], cIndex - 1, cIndex + 1)
                # below
                if lineIndex != len(lines) - 1:
                    print('below:')
                    endResult += find_and_sum_substr(lines[lineIndex + 1], cIndex - 1, cIndex + 1)
                # right
                if cIndex <= len(line) - 3:
                    print('right:')
                    endResult += find_and_sum_substr(line, cIndex + 1, cIndex + 1)
                # left
                if cIndex != 0:
                    print('left:')
                    endResult += find_and_sum_substr(line, cIndex - 1, cIndex - 1)

print(endResult)
