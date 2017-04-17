# -*- coding: utf-8 -*-
from src.english_number_spelling import EnglishNumberSpelling
from src.vietnamese_number_spelling import VietnameseNumberSpelling

language = raw_input("Enter language E(English) or V(Vietnamese): ")
if language == 'E':
    spelling = EnglishNumberSpelling()
elif language == 'V':
    spelling = VietnameseNumberSpelling()
else:
    print "Not support the language"
    quit()

print "Enter number"
while True:
    num_string = raw_input()
    is_number, valid_number = spelling.is_valid_number(num_string)
    if is_number:
        # print valid_number
        print spelling.number_to_word(valid_number)
    else:
        print "Invalid number"
