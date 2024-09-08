def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    char_count = get_character_count(text)
    print_report(text)


def get_character_count(text):
    text = text.lower()
    
    char_dict = {}
    
    for char in text:
        if char.isalpha():
            if char in char_dict:
                char_dict[char] += 1
            else:
                char_dict[char] = 1
    
    return char_dict

def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()

def print_report(text):
    report_data = get_character_count(text)
    
    # Sort the dictionary by values (character counts) in descending order
    sorted_data = sorted(report_data.items(), key=lambda item: item[1], reverse=True)
    
    # Print the report
    for char, count in sorted_data:
        print(f"The '{char}' character was found {count} times")

main()