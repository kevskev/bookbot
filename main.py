from stats import word_count, char_count, sort_dict, sort_on
import sys

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_content = f.read()
    return file_content

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    path = sys.argv[1]
    char_result = sort_dict(char_count(get_book_text(path)))

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    total_words = word_count(get_book_text(path))
    print(f"Found {total_words} total words")
    print ("--------- Character Count -------")
    for item in char_result:
        print(f"{item["char"]}: {item["num"]}")

main()