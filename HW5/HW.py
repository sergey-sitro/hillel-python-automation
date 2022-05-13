try:
    with open('example.txt') as file:
        words_dict = {}

        for line in file:
            print(line)

        words = line.split(" ")
        for i in words:
            words_dict.update({i: words.count(i)})

    most_occurent_word = max(words_dict, key=words_dict.get)
    most_occurent_word_count = words_dict[most_occurent_word]

    less_occurent_word = min(words_dict, key=words_dict.get)
    less_occurent_word_count = words_dict[less_occurent_word]

    print(most_occurent_word, f"is the most occurent, found {most_occurent_word_count} time(s)")
    print(less_occurent_word, f"is the less occurent, found {less_occurent_word_count} time(s)")

    try:
        with open("spam.txt", "x") as spam:
            spam.write(" ".join(words).replace(most_occurent_word, less_occurent_word))
    except FileExistsError:
        raise FileExistsError("File already exists!")


except FileNotFoundError:
    raise FileNotFoundError("File not found! Script finished!")
