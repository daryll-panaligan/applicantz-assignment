import assignment1


def test_reverse_digits():
    assert assignment1.reverse_words("0123456789") == "9876543210"


def test_reverse_letters():
    assert assignment1.reverse_words("AZaz") == "zaZA"


def test_ignore_other_characters():
    other_characters = ",./; '[]"
    assert assignment1.reverse_words(other_characters) == other_characters


def test_combination():
    test_str = "String; 2be \\[]^_` reversed...String"
    assert assignment1.reverse_words(test_str) == "gnirtS; eb2 \\[]^_` desrever...gnirtS"
