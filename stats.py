with open("books/frankenstein.txt") as f:
	get_book_text = f.read()

get_num_words = len(get_book_text.split())

def get_num_chars():
	counts = {}
	for char in get_book_text.lower():
		counts[char] = counts.get(char, 0) + 1
	return counts

def sorted_report():
	