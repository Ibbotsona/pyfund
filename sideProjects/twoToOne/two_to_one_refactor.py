def longest(s1, s2):
    string = "".join(sorted(set(s1 + s2)))
    legal_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
                     'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                     'v', 'w', 'x', 'y', 'z']
    a_to_z_only = [letter for letter in string if letter in legal_letters]

    return "".join(a_to_z_only)
