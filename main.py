import sys
from one_to_one_character_mapping import check_one_to_one_mapping

# Main Method File
if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("false")
    else:
        print(check_one_to_one_mapping(sys.argv[1], sys.argv[2]))
