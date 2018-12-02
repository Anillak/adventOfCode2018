from unittest import TestCase

from day1.find_frequency import *


class TestFindFrequency(TestCase):

    def test_should_read_file(self):
        self.assertEqual(read_file("input.txt").readline(), "+13\n")

    def test_find_frequency_with_positive_numbers(self):
        test_data = "+1 +2 +3"
        self.assertEqual(find_resulting_frequency(test_data.split(" ")), 6)

    def test_find_frequency_with_negative_numbers(self):
        test_data = "-1 -2 -3"
        self.assertEqual(find_resulting_frequency(test_data.split(" ")), -6)

    def test_find_frequency_passing_zero(self):
        test_data = "-1 +2 -4 +3"
        self.assertEqual(find_resulting_frequency(test_data.split(" ")), 0)

    def test_gives_correct_frequency_for_game_input(self):
        self.assertEqual(find_resulting_frequency(read_file("input.txt")), 576)

    def test_find_first_appearing_frequency_zero(self):
        test_data = "-1 +1"
        self.assertEqual(find_first_twice_appearing_frequency(test_data.split(" "), False), 0)

    def test_find_first_appearing_frequency_with_double_loop(self):
        test_data = "+3 +3 +4 -2 -4"
        self.assertEqual(find_first_twice_appearing_frequency(test_data.split(" "), False), 10)

    def test_gives_correct_first_encountered_frequency_for_game_input(self):
        self.assertEqual(find_first_twice_appearing_frequency(read_file("input.txt"), True), 77674)


