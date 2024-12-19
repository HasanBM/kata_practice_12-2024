
def converts_file_to_word_list(file_path='data/Word_list.txt'):
    with open(file_path, 'r') as f:
        word_list = [line.rstrip() for line in f]
    return word_list


def creates_dict_with_anagram_occurrences(word_list):
    anagram_dict={}
    for word in word_list:
        sorted_word = ''.join(sorted(word))
        if sorted_word in anagram_dict:
            anagram_dict[sorted_word].append(word)
        else:
            anagram_dict[sorted_word] = word
    return anagram_dict

def print_anagrams(anagram_dict):
    for k, v in anagram_dict.items():
        if len(v) > 1:
            print(' '.join(v))


