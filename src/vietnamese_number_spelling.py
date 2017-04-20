# # -*- coding: utf-8 -*-
from .number_spelling import *


class VietnameseNumberSpelling(NumberSpelling):
    def __init__(self):
        self._unit = ["không", "một", "hai", "ba", "bốn", "năm", "sáu", "bảy", "tám", "chín", "mười",
                     "muời một", "mười hai", "mười ba", "mười bốn", "mười lăm", "mười sáu", "mười bảy",
                     "mười tám", "mười chín"]
        self._tens = ["", "", "hai mươi", "ba mươi", "bốn mươi", "năm mươi", "sáu mươi", "bảy mươi",
                      "tám mươi", "chín mươi", "trăm"]
        self._block_name = ["", "nghìn", "triệu", "tỷ"]
        self._link_word = "linh"

    def _block_to_word(self, block, is_first_block):
        words = super(VietnameseNumberSpelling, self)._block_to_word(block, is_first_block)
        words = words.replace("mươi một", "mươi mốt")
        words = words.replace("mươi năm", "mươi lăm")
        return words
