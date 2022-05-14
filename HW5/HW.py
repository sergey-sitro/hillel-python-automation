try:
    with open('example.txt') as file:
        words_dict = {}

        words = file.read().lower().replace("\n", " ").split(" ")
        print(words)

        for i in words:
            words_dict.setdefault(i, 0)
            words_dict[i] += 1

    most_occurent_word = max(words_dict, key=words_dict.get)
    most_occurent_word_count = words_dict[most_occurent_word]

    less_occurent_word = min(words_dict, key=words_dict.get)
    less_occurent_word_count = words_dict[less_occurent_word]

    print(most_occurent_word, f"is the most occurent, found {most_occurent_word_count} time(s)")
    print(less_occurent_word, f"is the less occurent, found {less_occurent_word_count} time(s)")

    with open("spam.txt", "x") as spam:
        for position, word in enumerate(words, start=1):
            spam.write(word.replace(most_occurent_word, less_occurent_word) + " ")

            if position % 10 == 0:
                spam.write("\n")

except FileExistsError:
    raise FileExistsError("File already exists!")

except FileNotFoundError:
    raise FileNotFoundError("File not found! Script finished!")
