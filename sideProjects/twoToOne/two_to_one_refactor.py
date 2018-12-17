import string


def longest(s1, s2):
    sorted_str = sorted(set(s1 + s2))
    # removes duplicates and sorts list
    a_to_z_only = "".join([letter for letter in sorted_str if
                           letter in string.ascii_lowercase])
    # creates new list with only characters a to z
    return a_to_z_only


print(longest("sdsafsadslnsdnc34", "dvnlkdJJSDKD87"))
