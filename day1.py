from functools import reduce


def read_file(input_file):
    file = open(input_file, "r")
    return file


def find_resulting_frequency(input_source):
    return reduce(lambda result, item: int(result) + int(item), input_source)


def find_first_twice_appearing_frequency(input_source, source_is_file):
    current_frequency = 0
    frequency_set = {current_frequency}
    while True:
        for line in input_source:
            current_frequency = current_frequency + int(line)
            if current_frequency in frequency_set:
                return current_frequency
            else:
                frequency_set.add(current_frequency)
        if source_is_file:
            input_source.seek(0)


print(find_first_twice_appearing_frequency(read_file("input.txt"), True))
