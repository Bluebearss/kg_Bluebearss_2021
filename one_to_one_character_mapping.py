# File to contain function for one to one character mapping


def check_one_to_one_mapping(str1: str, str2: str) -> str:
    # check equal length strings
    if len(str1) != len(str2):
        return "false"

    one_to_one_hash = {}

    for i in range(len(str1)):
        if not(str1[i] in one_to_one_hash):  # check if in hash
            one_to_one_hash[str1[i]] = str2[i]
        elif one_to_one_hash[str1[i]] != str2[i]:  # check if same value in hash
            return "false"
        else:
            continue

    return "true"
