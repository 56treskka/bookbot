def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        print_report(file_contents)
        

def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    chars = {}
    lower_text = text.lower()
    for char in lower_text:
        if char in chars:
            chars[char] += 1
        else:
            chars[char] = 1
    return chars

def sort_on(dict):
    return dict["count"]

def print_report(text):
    word_count = count_words(text)
    char_count = count_characters(text)
    chars = []
    for char, count in char_count.items():
        if char.isalpha():
            chars.append({"character": char, "count": count})
    chars.sort(key=sort_on, reverse=True)

    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words found in the document:")
    print()

    for char in chars:
        print(f"The '{char["character"]}' character was found {char["count"]} times")
    print("--- End of report ---")

main()
