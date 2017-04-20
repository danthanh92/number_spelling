# Created by danthanh at 19/04/2017

Feature: Number Spelling
  # Enter feature description here
  # unit test
  Scenario Outline: Check number string
    Given a string "<num_string>"
    When call checking number method
    Then result is "<check_result>"
    Examples:
      | num_string | check_result |
      | 00001414   | 1            |
      | ag114      | 0            |


  # functional test
  Scenario Outline: Spelling number
    Given a string "<num_string>"
    And   language "<language>"
    When call number spelling method
    Then result is "<words>"
    Examples:
      | num_string        | language | words                                                |
      | 00001414          | E        | one thousand four hundred fourteen                   |
      | 010001            | E        | ten thousand and one                                 |
      | 10031401          | E        | ten million thirty one thousand four hundred and one |
      | 9000000100009     | E        | nine thousand billion one hundred thousand and nine  |
      | 10000000000000125 | E        | ten million billion one hundred twenty five          |

      | 00001414          | V        | một nghìn bốn trăm mười bốn                          |
      | 010001            | V        | mười nghìn linh một                                  |
      | 10031401          | V        | mười triệu ba mươi mốt nghìn bốn trăm linh một       |
      | 9000000100009     | V        | chín nghìn tỷ một trăm nghìn linh chín               |
      | 10000000000000125 | V        | mười triệu tỷ một trăm hai mươi lăm                  |