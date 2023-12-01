endResult = 0
word_to_number = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
}


def is_num_in_there(word):
    for word_number, number in word_to_number.items():
        if word_number in word:
            return number
    return ''


with open('sample_data.txt', 'r') as file:
    for line in file:
        subString = ''
        allNumbersOfLine = ''
        for char in line:
            if char.isdigit():
                allNumbersOfLine += char
                subString = ''
                continue
            subString += char
            if is_num_in_there(subString) != '':
                allNumbersOfLine += is_num_in_there(subString)
                subString = subString[-1]
                continue
        endResult += int(allNumbersOfLine[0] + allNumbersOfLine[-1])
print(endResult)
