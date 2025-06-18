def word_count(text):
    words = text.split()
    num_words = len(words)
    return num_words

def char_count(text):
    char_dict = {}
    for c in text:
        char = c.lower()
        if char not in char_dict:
            char_dict[char] = 1
        else:
            char_dict[char] += 1
    return char_dict

def sort_on(dict):
    return dict["num"]

def sort_dict(dict):
    sorted_list = []
    for item in dict:
        dict_item = {}
        dict_item["char"] = item
        dict_item["num"] = dict[item]
        sorted_list.append(dict_item)
    
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

