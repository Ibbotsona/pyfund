Exercise Brief:

    Take 2 strings s1 and s2 including only letters from ato z. Return a new sorted string, the longest possible, 
    containing distinct letters,

    * each taken only once - coming from s1 or s2. #Examples: ``` a = "xyaabbbccccdefww" b = "xxxxyyyyabklmopq" 
    longest(a, b) -> "abcdefklmopqwxy"
    a = "abcdefghijklmnopqrstuvwxyz" longest(a, a) -> "abcdefghijklmnopqrstuvwxyz" ```
    
Explanation:

    * Given the brief above the python script to perform this action comprises of 7 functions:
        *   convert_strings_to_list - which takes in 2 parameters of type string and returns a list of each 
            character within the string
        *   remove_illegal_characters - this function takes in a list and removes any characters that are not listed 
            within the legal letters list.
        *   filter_duplicates - this function takes a list as a parameter and returns a new list with any duplicates of
            the original list removed.
        *   sort_new_list - this function takes a list as a parameter and returns a new list sorted in alphabetical
            order.
        *   list_to_string - this function takes in a list object and returns a string object containg the 
            concatentated contents of the parameter.
        *   convert_two_strings - this function takes in two strings and runs the above functions in tandem to achieve
            the required result.
        *   main - this function prints the result of the convert_two_strings function.
    
Usage:

    *   `python3 "somestringhere", "containinganycharacters"`
    *   In order to run the function as a bash script the permissions must be changed
        to allow it to be executable, this can be achieved with `chmod u+x`
    *   Once the script has been given the permissions to be executable it can be run with: 
        `./two_to_one.py "str1", "str2"`
    
    