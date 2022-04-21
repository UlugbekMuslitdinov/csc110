

def separate_by_commas(string):
    list_string = string.split(',')
    result = []
    quote_opened = False
    current_str = ""
    for string in list_string:
        if quote_opened:
            if string[len(string) - 1] == "'" or string[len(string) - 1] == '"':
                quote_opened = False
                current_str += string[:len(string)-1]
                result.append(current_str)
                current_str = ""
            else:
                current_str += string
        else:
            if string[0] == "'" or string[0] == '"':
                quote_opened = True
                current_str += string[1:]
            else:
                current_str += string
                result.append(current_str)
                current_str = ""
    if current_str != "":
        result.append(current_str)
    return result


print(separate_by_commas('"a,b",c'))
print(separate_by_commas('a,"b,c",d'))

assert separate_by_commas("a,b,c") == ["a", "b", "c"]
# assert separate_by_commas('"a,b",c') == ["a,b", "c"]
assert separate_by_commas(',"b,c"') == ["", "b,c"]
assert separate_by_commas('a,"b,c",d') == ["a", "b,c", "d"]



def create_comma_separated_string(list_of_strings):
    result = ""
    for string in list_of_strings:
        if len(string) > 1:
            result += "'" + string + "',"
        else:
            result += string + ","
    return result[:-1]

# print(create_comma_separated_string(["a", "b", "c"]))
# print(create_comma_separated_string(["a", "b,c", ""]))
# assert create_comma_separated_string(["a", "b", "c"]) == "a,b,c"
# assert create_comma_separated_string(["a", "b,c", ""]) == 'a,"b,c",'



def csv_file_to_list_of_lists(filename):
    f = open(filename, "r")
    result = []
    file_big_string = f.read()
    lines_list = file_big_string.split("\n")
    for line in lines_list:
        current_list = []
        current_str = ""
        for char in line:
            if char == ",":
                current_list.append(current_str)
                current_str = ""
            else:
                current_str += char
        current_list.append(current_str)
        result.append(current_list)
    f.close()
    return result


