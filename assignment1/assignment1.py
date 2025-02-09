import re


def reverse_words(input_str):
    # Match letters and digits only
    regex_str = "[A-z0-9]+"
    subs_to_be_reversed = re.findall(regex_str, input_str)

    print(subs_to_be_reversed)

    # Reverse each matching substring in input_str iteratively
    reversed_str = input_str
    for substr in subs_to_be_reversed:
        reversed_str = re.sub(substr, substr[::-1], reversed_str)

    return reversed_str


def main():
    test_str = "String; 2be reversed..."
    assert reverse_words(test_str) == "gnirtS; eb2 desrever..."


if __name__ == "__main__":
    main()
