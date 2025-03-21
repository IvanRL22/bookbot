from stats  import count_words
from stats import count_all_characters
from stats import sort_dict

def get_book_text(path):

    print('Analyzing book found at', path, '...')

    with open(path, 'r') as f:
        file_contents = f.read()

    return file_contents


def main():

    print('============ BOOKBOT ============')

    book_content = get_book_text('books/frankenstein.txt')

    word_count = count_words(book_content)
    print('----------- Word Count ----------')
    print('Found', word_count, 'total words')

    print('--------- Character Count -------')
    for d in sort_dict(count_all_characters(book_content)):
        if str(d['character']).isalpha():
            print(d['character'], d['count'], sep=': ')

    print('============= END ===============')


main()
