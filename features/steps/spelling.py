# -*- coding: utf-8 -*-
from behave import *
from src.english_number_spelling import EnglishNumberSpelling
from src.vietnamese_number_spelling import VietnameseNumberSpelling
from src.number_spelling import *


@given('a string "{num_string}"')
def step_impl(context, num_string):
    """
    :type context: behave.runner.Context
    :type num_string: str
    """
    context.number_string = num_string


@when("call checking number method")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.is_valid_number = is_valid_number(context.number_string)


@then('result is "{check_result:d}"')
def step_impl(context, check_result):
    """
    :type context: behave.runner.Context
    :type check_result: int
    """
    assert (context.is_valid_number == check_result)


# functional test steps
@when("call number spelling method")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.words = context.spelling.number_to_word(context.number_string)


@then('result is "{words}"')
def step_impl(context, words):
    """
    :type context: behave.runner.Context
    :type words: str
    """
    print("words_1 = [%s]" % context.words)
    print("words_2 = [%s]\n" % words)
    assert (context.words == words)


@step('language "{language}"')
def step_impl(context, language):
    """
    :type context: behave.runner.Context
    :type language: str
    """
    context.language = language.strip()
    if context.language == 'E':
        context.spelling = EnglishNumberSpelling()
    elif context.language == 'V':
        context.spelling = VietnameseNumberSpelling()
