import pytest
from assert_testing_carique_BSCS3A import find_longest_word

@pytest.mark.parametrize( 
    "input_list, expected_output",
    [
        (["The quick brown fox", "jump over the lazy dog"], ["quick", "brown"]), 
        (["This is a longtest", "to find the longestt word"], ["longtest","longestt"]), 
        (["Hello world", "Python is awesome"], ["awesome"]), 
        (["The cat is black", "The dog is brown"], ["black", "brown"]), 
        (["ab", "cd"], []),
    ]
)
def test_find_longest_word(input_list, expected_output): 
    assert find_longest_word(input_list) == expected_output