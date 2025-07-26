import sys
if len(sys.argv) != 2:
    print(f'Usage: python3 main.py <path_to_book>')
    sys.exit(1)
book_path = sys.argv[1]

from stats import get_num_words,count_letters

def get_book_text(filepath):
    with open(filepath) as f:
        file_content = f.read()
    return file_content





def analyze_book(filepath):
    print("============ BOOKBOT ============")
    print(f'Analyzing book found at {filepath}...')
    print('----------- Word Count ----------')
    number_of_words = get_num_words(filepath)
    print(number_of_words)
    print('--------- Character Count -------')
    number_of_letters = count_letters(filepath)
    for letter,count in sorted(number_of_letters.items()):
        print(f'{letter}: {count}')
    print('============= END ===============')  




analyze_book(book_path)



