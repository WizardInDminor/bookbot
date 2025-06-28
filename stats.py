# ~/dev/github.com/wizardindminor/bookbot/stats.py

def word_count(book_string):
    """Count the number of words in a string"""
    return len(book_string.split())

def char_count(book_string):
    """Count occurrences of each character in the string, case-insensitive"""
    chars = {}
    for char in book_string.lower():
        chars[char] = chars.get(char, 0) + 1 
    return chars

def sort_on(item):
    """Return the value used for sorting: the count."""
    return item["num"]

def char_report(char_dict):
    """
    Convert character frequency dict into a sorted list of dicts
    sorted by frequency descending.
    """
    char_list = [{"char": char, "num": count} for char, count in char_dict.items()]
    char_list.sort(reverse=True, key=sort_on)
    return char_list
