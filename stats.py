def count_words(text):
    total_words = len(text.split())
    
    return total_words

def character_count(text):
    total_characters = {}

    for char in text:
        next_char = char.lower()

        if next_char not in total_characters:
            total_characters[next_char] = 1
        else:
            total_characters[next_char] += 1

    return total_characters

def sort_dict(char_count):
    char_list = []

    for char, count in char_count.items():
        char_list.append({"char": char, "count": count})

    def sort_on(dict):
        return dict["count"]

    char_list.sort(reverse=True, key=sort_on)

    return char_list
