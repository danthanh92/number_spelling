# -*- coding: utf-8 -*-
import re


class NumberSpelling(object):
    def __init__(self):
        self._unit = []
        self._tens = []
        self._block_name = []
        self._link_word = ""

    def number_to_word(self, num_string):
        num_string = validate_number(num_string)
        if len(num_string) <= 3:
            return self._block_to_word(num_string, True)

        odd_block = len(num_string) % 3
        if odd_block:
            num_string = ("00" if odd_block == 1 else "0") + num_string

        block_position = 0
        words = ""
        for i in range(len(num_string), 2, -3):
            if i == 3:
                block = self._block_to_word(num_string[i - 3: i], True)
            else:
                block = self._block_to_word(num_string[i - 3: i], False)

            block_name = self._block_name[block_position]
            if len(block) != 0:
                words = block + " " + block_name + (" " if len(words) else "") + words
            elif block_position == len(self._block_name) - 1:
                words = block_name + (" " if len(words) else "") + words

            if block_position == len(self._block_name) - 1:
                block_position = 1
            else:
                block_position += 1

        return words.strip()

    def _block_to_word(self, block, is_first_block):
        words = ""
        number = int(block)
        if is_first_block is True and number < 10:
            return self._unit[number]
        elif number == 0:		# number = 0 and is_first_block = False
            return words

        first_digit = number // 100
        number %= 100
        if first_digit != 0:		# read first digit (hundreds)
            words = self._unit[first_digit] + " " + self._tens[10] + (" " if number else "")
        if number == 0:			# second and third digit = 0
            return words
        elif number < 10:		# second digit = 0
            return words + self._link_word + " " + self._unit[number]
        elif number < 20:		# second digit = 1
            return words + self._unit[number]

        second_digit = number // 10
        number %= 10
        if number != 0:			# third digit != 0
            words += self._tens[second_digit] + " " + self._unit[number]
        else:					# third digit = 0
            words += self._tens[second_digit]

        return words


def is_valid_number(num_string):
    if num_string.isdigit():
        return True
    else:
        return False


def validate_number(num_string):
    match = re.search('[^0]', num_string)
    if match:
        return num_string[match.start():]
    else:
        return '0'




