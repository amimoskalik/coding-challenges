"""
One Away: There are three types of edits that can be performed on strings: insert a character,
remove a character, or replace a character. Given two strings, write a function to check if they are
one edit (or zero edits) away.
EXAMPLE
pale, ple -> true
pales, pale -> true
pale, bale -> true
pale, bake -> false
"""

def one_edit_away(string1, string2):
    if len(string1) >= len(string2):
        str1 = string1
        str2 = string2
    else:
        str1 = string2
        str2 = string1
    
    index = 0
    number_of_changes = 0

    for str1_character in str1:
        try:
            str2_character = str2[index]
        except IndexError:
            number_of_changes += 1
            if number_of_changes > 1:
                return False
            continue

        print(str1_character + " vs " + str2_character)
        if str1_character != str2_character:
            number_of_changes += 1
            if number_of_changes > 1:
                return False
            try:
                # When we encounter different character we need to check
                # the next one if it's the same in both
                # We possibly deal with the replace edit
                if str1[index+1] == str2[index+1]:
                    print("Replace character happened?")
                    index += 1
                    continue
            except IndexError:
                pass
            # If it's different it's a remove event
            # on the shorter string (we always assume remove, not add)
            # Try to skip one index
            # without incrementing index of the shorter string
            print("Insert character happened?")
            continue
        index += 1

    return True
        

test_cases = [
    ('pale', 'ple', True),
    ('pales', 'pale', True),
    ('pale', 'bale', True),
    ('pale', 'bake', False),
    ('', 'bake', False),
    ('eloeleoleo', 'bake', False),
    ('123', 'bake', False)
]

for test_case in test_cases:
    print("*** TESTING ***")
    print(test_case[0] + " AND " + test_case[1])
    assert one_edit_away(test_case[0], test_case[1]) == test_case[2]
    print(test_case[1] + " AND " + test_case[0])
    assert one_edit_away(test_case[1], test_case[0]) == test_case[2]