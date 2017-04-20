from .number_spelling import *


class EnglishNumberSpelling(NumberSpelling):
    def __init__(self):
        self._unit = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine",
                      "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen",
                      "eighteen", "nineteen"]
        self._tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety", "hundred"]
        self._block_name = ["", "thousand", "million", "billion"]
        self._link_word = "and"
