def get_num_words(filepath):
    content = get_book_text(filepath)
    num_words = len(content.split())
    return print(f"Found {num_words} total words")

def get_book_text(filepath):
    with open(filepath) as f:
        content = f.read()
    return content

def count_char(filepath):
    content = get_book_text(filepath).lower()
    freq = {}
    for i in set(content):
        freq[i] = content.count(i)
    return freq

def dic_sort(freq):
    sorting = []
    for k in list(freq.keys()):
        sorting.append({"character": k , "count": freq.get(k)})
    sorting.sort(reverse = True, key= sort_on)
    return sorting

def sort_on(dict):
    return dict["count"]


