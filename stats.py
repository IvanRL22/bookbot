def count_words(content: str):

    return len(content.split())


def count_all_characters(content: str) -> dict[str, int]:

    word_count = {}
    for letter in content.lower():
        word_count[letter] = word_count.setdefault(letter, 0) + 1

    return word_count


def sort_dict(input_dict: dict[str, int]) -> list[dict]:

    all_dicts = list()
    for letter in input_dict.keys():
        all_dicts.append({'character': letter, 'count': input_dict[letter]})

    all_dicts.sort(key=lambda d: d['count'], reverse=True)
    return all_dicts

