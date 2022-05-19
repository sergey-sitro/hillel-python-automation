def get_file_path():
    path = input(r"Enter file path: ")
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


def get_write_file_path():
    write_path = input(r"Enter path to write the file: ")
    return write_path


def replace_words(lst, mow, low):
    return [i if i != mow else low for i in lst]


def prepared_list_for_writing(lst, lines=10):
    prepared_list = []

    for position, word in enumerate(lst, start=1):

        if position % lines != 0:
            prepared_list.append(word)
        else:
            prepared_list.append("\n")
    return " ".join(prepared_list).split("\n")


def write_file(path, lst, mode):
    with open(path, mode) as spam:
        print(lst)
        spam.writelines(lst)


def main():
    try:
        content = open_file()
    except FileNotFoundError:
        print("File not found, script is finished!")
    else:
        list_of_words = get_list_of_words(content)
        dict_of_words = create_words_dict(list_of_words)
        most_occurent_word, most_occurent_word_count = get_most_occurent_word(dict_of_words)
        less_occurent_word, less_occurent_word_count = get_less_occurent_word(dict_of_words)

        print(most_occurent_word, f"is the most occurent, found {most_occurent_word_count} time(s)")
        print(less_occurent_word, f"is the less occurent, found {less_occurent_word_count} time(s)")

        replaced_text = replace_words(list_of_words, most_occurent_word, less_occurent_word)
        prepared_list = prepared_list_for_writing(replaced_text)
        write_path = get_write_file_path()

        try:
            write_file(write_path, prepared_list, "x")
        except FileExistsError:
            answer = input("File exists. Do you want to overwrite the file? y/N: ")
            if answer == "y":
                write_file(write_path, prepared_list, "w")


if __name__ == "__main__":
    main()
