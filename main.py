from stats import count_char, dic_sort , get_num_words
import sys
import os


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path = sys.argv[1]
    number_of_char = count_char(path)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}")
    print("----------- Word Count ----------")
    get_num_words(path)
    print("--------- Character Count -------")
    sorted_list = dic_sort(number_of_char)
    for i in range(len(sorted_list)):
        if sorted_list[i]["character"].isalpha() == True:
            print(f"{sorted_list[i]['character']}: {sorted_list[i]['count']}")   
    print("============= END ===============")
    print(sys.argv)