with open("books/frankenstein.txt") as f:
	get_book_text = f.read()

get_num_words = len(get_book_text.split())

def get_num_chars():
	counts = {}
	for char in get_book_text.lower():
		if char.isalpha():
			counts[char] = counts.get(char, 0) + 1
	return counts

def sort_on(item):
	return item["num"]

def sorted_report():
	char_counts = get_num_chars()
	char_list = [{"char": ch, "num": count} for ch, count in char_counts.items()]
	char_list.sort(key=sort_on, reverse=True)
	return char_list

def print_report():
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {get_num_words} total words")
    print("--------- Character Count -------")
    for item in sorted_report():
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")