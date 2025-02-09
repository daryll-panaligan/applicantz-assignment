import assignment1


def test_reverse_digits():
    assert assignment1.reverse_words("0123456789") == "9876543210"


def test_reverse_letters():
    assert assignment1.reverse_words("AZaz") == "zaZA"


def test_reverse_combined():
    pass


def test_ignore_other_characters():
    other_characters = ",./; '[]"
    assert assignment1.reverse_words(other_characters) == other_characters
