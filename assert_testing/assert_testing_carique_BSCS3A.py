# pip install pytest

# Problem: You are given a list of strings, where each string represents a sentence. Write a function find_longest_word that takes the list of strings as input and returns the longest word among all the sentences. If there are multiple longest words, return a list containing all of them, in the order they appear. Additionally, ignore any words that are commonly used and have a length of less than 4 characters.

# For example, given the input list ["The quick brown fox", "jumps over the lazy dog"],
# the function should return ["quick", "brown", "jumps"].

def find_longest_word(sentences):
    longest_words = []
    max_length = 0
    for sentence in sentences: 
        words = sentence.split()
        for word in words:
            if len(word) > max_length and len(word) >= 4:
                longest_words = [word]
                max_length = len(word)
            elif len(word) == max_length and len(word) >= 4:
                longest_words.append(word)
    return longest_words

# expected output:
# test_assert_testing_lastname_section.py::test_find_longest_word[input_list0-expected_output0] PASSED                [ 20%]
# test_assert_testing_lastname_section.py::test_find_longest_word[input_list1-expected_output1] PASSED                [ 40%] 
# test_assert_testing_lastname_section.py::test_find_longest_word[input_list2-expected_output2] PASSED                [ 60%] 
# test_assert_testing_lastname_section.py::test_find_longest_word[input_list3-expected_output3] PASSED                [ 80%] 
# test_assert_testing_lastname_section.py::test_find_longest_word[input_list4-expected_output4] PASSED                [100%] 