def count_words(content: str):

    return len(content.split())


def count_all_characters(content: str) -> dict:

    word_count = {}
    for letter in content.lower():
        word_count[letter] = word_count.setdefault(letter, 0) + 1

    return word_count
