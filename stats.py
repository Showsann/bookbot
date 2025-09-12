#with open("books/") as f:
#	get_book_text = f.read()
#
#get_num_words = len(get_book_text.split())

def get_num_chars(text):
    counts = {}
    for char in text.lower():
        if char.isalpha():
            counts[char] = counts.get(char, 0) + 1
    return counts

def sort_on(item):
    return item["num"]

def sorted_report(text):
    char_counts = get_num_chars(text)
    char_list = [{"char": ch, "num": count} for ch, count in char_counts.items()]
    char_list.sort(key=sort_on, reverse=True)
    return char_list

def print_report(book_path):
    with open(book_path) as f:
        book_text = f.read()

    num_words = len(book_text.split())

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in sorted_report(book_text):
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")
