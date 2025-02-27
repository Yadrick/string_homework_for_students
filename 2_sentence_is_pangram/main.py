"""
Панграмма - предложение, которое использует каждую букву алфавита (в нашем случае - английского алфавита).
Необходимо реализовать код, который скажет, является предложение панграммой или нет.
Буквы в верхнем и нижнем регистрах считаются эквивалентными.
Предложения содержат только буквы английского алфавита, без пробелов и т.п.
Проверка:
pytest ./2_sentence_is_pangram/test.py
"""


import string


def is_sentence_is_pangram(sentence: str) -> bool:
    """Пишите ваш код здесь."""

    char_array = set(sentence.lower())
    english_alphabet = set(string.ascii_letters.lower())

    return english_alphabet.issubset(char_array)
