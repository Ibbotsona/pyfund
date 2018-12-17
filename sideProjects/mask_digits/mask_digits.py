def mask_digits(cc):

    """
    A function which takes in a string, converts
    every character of the string to a #
    except the last four digits.

    args:
        String input
    returns:
        String value with all characters except the last four set as #
    """

    # convert string to list
    # find length of list
    # loop through list
    # if letter = " " then append to new masked list
    # if letter is up to the last 4 digits of list
        # then append "#" to the new list in original numbers place
    # every other letter, set to #

    list_cc = list(cc)
    list_len = len(list_cc)
    masked_list = []

    for counter, letter in enumerate(list_cc):

        if counter <= list_len - 5:
            if letter == " ":
                masked_list.append(letter)
            else:
                masked_list.append("#")
        elif counter >= list_len - 5:
            masked_list.append(letter)

    masked_list = "".join(masked_list)
    return masked_list


print(mask_digits("4444 4444 4444 4444"))
