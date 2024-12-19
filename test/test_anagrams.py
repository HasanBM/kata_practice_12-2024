
from src.anagrams import converts_file_to_word_list 
from src.anagrams import creates_dict_with_anagram_occurrences



def test_strips_newline_characters():
    list_of_words = converts_file_to_word_list()
    assert isinstance(list_of_words, list)

def test_creates_dict_with_anagram_occurrences():
    result = creates_dict_with_anagram_occurrences(['and', 'dna'])
    expected = 'and dna'
    assert result == expected

# def test_compares_two_dictionaries():
#     result = compares_two_dictionaries({'a': 1, 'n': 1, 'd': 1}, {'d': 1, 'n': 1, 'a': 1})
#     expected = True
#     assert result == expected



    
