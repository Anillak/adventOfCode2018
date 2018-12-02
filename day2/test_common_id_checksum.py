from unittest import TestCase

from day2.common_id_checksum import *


class TestFindChecksum(TestCase):

    def test_checksum_is_zero_from_both_twos_and_threes(self):
        test_data = "abcdef"
        self.assertEqual(find_checksum(test_data.split(" ")), 0)

    def test_checksum_is_zero_from_twos(self):
        test_data = "babfbc"
        self.assertEqual(find_checksum(test_data.split(" ")), 0)

    def test_checksum_is_zero_from_threes(self):
        test_data = "badafc"
        self.assertEqual(find_checksum(test_data.split(" ")), 0)

    def test_checksum_is_one(self):
        test_data = "bababc"
        self.assertEqual(find_checksum(test_data.split(" ")), 1)

    def test_does_not_count_doubles_twice(self):
        test_data = "bababcc"
        self.assertEqual(find_checksum(test_data.split(" ")), 1)

    def test_does_not_count_threes_twice(self):
        test_data = "bababccc"
        self.assertEqual(find_checksum(test_data.split(" ")), 1)

    def test_does_not_count_more_occurrences(self):
        test_data = "bababbbbccc"
        self.assertEqual(find_checksum(test_data.split(" ")), 1)

    def test_find_checksum_of_example(self):
        test_data = "abcdef bababc abbcde abcccd aabcdd abcdee ababab"
        self.assertEqual(find_checksum(test_data.split(" ")), 12)

    def test_able_to_find_count_of_differences_when_none(self):
        self.assertEqual(letter_difference_between("abcdefg", "abcdefg"), 0)

    def test_able_to_find_count_of_differences_when_one(self):
        self.assertEqual(letter_difference_between("abcdefg", "bbcdefg"), 1)
        self.assertEqual(letter_difference_between("abcdefg", "abadefg"), 1)
        self.assertEqual(letter_difference_between("abcdefg", "abcdef1"), 1)

    def test_able_to_find_count_of_differences_when_more(self):
        self.assertEqual(letter_difference_between("abcdefg", "bxcdefg"), 2)
        self.assertEqual(letter_difference_between("abcdefg", "abaxxxg"), 4)
        self.assertEqual(letter_difference_between("abcdefg", "abcdxx1"), 3)

    def test_get_common_letters_when_difference_at_beginning(self):
        self.assertEqual(get_string_without_different_letter("xbcdefg", "abcdefg"), "bcdefg")

    def test_get_common_letters_when_difference_in_middle(self):
        self.assertEqual(get_string_without_different_letter("abcxefg", "abcdefg"), "abcefg")

    def test_get_common_letters_when_difference_at_end(self):
        self.assertEqual(get_string_without_different_letter("abcdefg", "abcdefx"), "abcdef")
