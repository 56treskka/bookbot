def main():
    path = "books/frankenstein.txt"
    text = get_text(path)
    words = count_words(text)
    chars = count_chars(text)
    print_chars(chars)

def count_words(text):
    words = text.split()

    return len(words)

def count_chars(text):
    lower_text = text.lower()
    chars = {}

    for char in lower_text:
        if char in chars:
            chars[char] += 1
        else:
            chars[char] = 1

    return chars

def sort_func(dict):
    return dict["num"]

def print_chars(chars):
    chars_arr = [{"char": char, "num": count} for char, count in chars.items()]
    chars_arr.sort(reverse=True, key=sort_func)

    for i in range(0, len(chars_arr)):
        if chars_arr[i]["char"].isalpha():
            print(f"The '{chars_arr[i]["char"]}' character was found {chars_arr[i]["num"]} times")

def get_text(path):
    with open(path) as f:
        file_contents = f.read()
        return file_contents

main()
