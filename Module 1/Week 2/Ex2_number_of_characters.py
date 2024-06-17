def count_character(string):
    char_count = {}

    for char in string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count


# Test
test_string = 'huynhnguyennhunguyen'
expected_output = {
    'h': 3,
    'u': 4,
    'y': 3,
    'n': 6,
    'g': 2,
    'e': 2
}

assert count_character(test_string) == expected_output