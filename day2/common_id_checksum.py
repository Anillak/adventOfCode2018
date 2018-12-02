def read_file(input_file):
    file = open(input_file, "r")
    return file


def build_dictionary(line):
    line_dictionary = dict()
    for letter in line:
        if letter not in line_dictionary:
            line_dictionary[letter] = 1
        else:
            line_dictionary[letter] = line_dictionary[letter] + 1
    return line_dictionary


def find_checksum(input_source):
    has_two_count = 0
    has_three_count = 0
    for line in input_source:
        line_dictionary = build_dictionary(line)
        if 2 in line_dictionary.values():
            has_two_count = has_two_count + 1
        if 3 in line_dictionary.values():
            has_three_count = has_three_count + 1
    return has_two_count * has_three_count


def letter_difference_between(first_string, second_string):
    return sum(first_string[i] != second_string[i] for i in range(len(first_string)))


def get_string_without_different_letter(first_string, second_string):
    difference_position = next(i for i in range(len(first_string)) if first_string[i] != second_string[i])
    return first_string[:difference_position] + second_string[difference_position + 1:]


def find_common_part_of_correct_ids(input_source):
    while True:
        current_string = input_source.readline().strip()
        if not current_string:
            break
        current_position = input_source.tell()
        for line in input_source:
            compare_to_string = line.strip()
            if letter_difference_between(current_string, compare_to_string) == 1:
                return get_string_without_different_letter(current_string, compare_to_string)
        input_source.seek(current_position)
    return ""


print(find_common_part_of_correct_ids(read_file("input.txt")))
