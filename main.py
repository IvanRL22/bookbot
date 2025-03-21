from stats import count_words
from stats import count_all_characters

def get_book_text(path):

    with open(path, 'r') as f:
        file_contents = f.read()

    return file_contents



def main():
    book_content = get_book_text('books/frankenstein.txt')
    word_count = count_words(book_content)
    print(word_count, 'words found in the document')
    print(count_all_characters(book_content))


main()
