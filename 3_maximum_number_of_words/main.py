"""
Вам дан список предложений.
предложения содержит только слова, которые разделены единичными пробелами.
Необзодимо вернуть максимальное количество слов, которое содержится в одном предложении.
sentences[i] - это одно предложение.
Если ни одно из предложений не содержит слов, то нужно вернуть 0
Проверка:
pytest ./3_maximum_number_of_words/test.py
"""


def get_max_number_of_words_from_sentences(sentences: list[str]) -> int:
    """Пишите ваш код здесь."""
    max_count_words = 0

    for sentence in sentences:
        len_sentence = len(sentence.split())
        if len_sentence > max_count_words:
            max_count_words = len_sentence

    return max_count_words
