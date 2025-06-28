# ~/dev/github.com/wizardidminor/bookbot/main.py
import sys
from stats import word_count, char_count, char_report

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book = get_book_text(sys.argv[1])
    count = word_count(book)
    chars = char_count(book)
    report = char_report(chars)

    print("=" * 12 + " BOOKBOT " + "=" * 12)
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("-" * 11 + " Word Count " + "-" * 11)
    print(f"Found {count} total words")
    print("-" * 11 + " Character Count " + "-" * 11)
    for item in report:
        print(f"{item['char']}: {item['num']}")
        

if __name__ == "__main__":
    main()
