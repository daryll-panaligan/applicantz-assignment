import re


def reverse_words(input_str):
    # Match letters and digits only
    reg = re.compile(r"[A-Za-z\d]+")
    subs_to_be_reversed = set(reg.findall(input_str))

    # Reverse each matching substring in input_str iteratively
    reversed_str = input_str
    for substr in subs_to_be_reversed:
        reversed_str = reversed_str.replace(substr, substr[::-1])

    return reversed_str


def main():
    test_str = "String; 2be reversed..."
    assert reverse_words(test_str) == "gnirtS; eb2 desrever..."


if __name__ == "__main__":
    main()
