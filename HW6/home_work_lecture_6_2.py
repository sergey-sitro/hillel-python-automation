def get_file_path():
    path = input(r"Enter file path: ")  # r - для возможности запуска на Windows
    return path


def open_file() -> str:
    with open(get_file_path()) as file:
        file_content = file.read()

    return file_content


def get_list_of_words(string) -> list:
    return string.lower().replace("\n", " ").split(" ")


def create_words_dict(lst):
    words_dict = {}

    for i in lst:
        words_dict.setdefault(i, 0)
        words_dict[i] += 1
    print(words_dict)

    return words_dict


def get_most_occurent_word(dct):
    most_occurent_word = max(dct, key=dct.get)
    most_occurent_word_count = dct[most_occurent_word]

    return most_occurent_word, most_occurent_word_count


def get_less_occurent_word(dct):
    less_occurent_word = min(dct, key=dct.get)
    less_occurent_word_count = dct[less_occurent_word]

    return less_occurent_word, less_occurent_word_count


def main():
    content = open_file()
    list_of_words = get_list_of_words(content)
    dict_of_words = create_words_dict(list_of_words)
    most_occurent_word, most_occurent_word_count = get_most_occurent_word(dict_of_words)
    less_occurent_word, less_occurent_word_count = get_less_occurent_word(dict_of_words)

    print(most_occurent_word, f"is the most occurent, found {most_occurent_word_count} time(s)")
    print(less_occurent_word, f"is the less occurent, found {less_occurent_word_count} time(s)")


if __name__ == "__main__":

    try:
        main()
    except FileNotFoundError:
        print("File not found! End of script!")
