import os
import codecs


def display_title_bar():
    os.system('cls')

    print("\n**********************************************")
    print("***************** Zipf Laws ******************")
    print("**********************************************")


def quit():
    print("\nThanks for your work!")


def get_user_choice():
    print("\n[1] Define article key words.")
    print("[2] Define if article refers to the selected topic.")
    print("[q] Quit.")

    return input("What would you like to do? ")


def show_available_articles():
    print("\nSelect one of the following Articles:")
    i = 0
    for text in texts:
        i += 1
        print("[" + str(i) + "] " + text)
    print("[m] Menu")
    return input("Your choice: ")


def show_available_topics():
    print("\nSelect one of the following topics:")
    i = 0
    for topic in topics:
        i += 1
        print("[" + str(i) + "] " + topic)
    print("[m] Menu")
    return input("Your choice: ")


def find_key_words():
    article = show_available_articles()
    if article == 'm':
        display_title_bar()
    else:
        print('\nHere we will define article key words!\n')
        file_path = diff_texts_path + texts[int(article)-1]
        print("File path: " + file_path)
        file_obj = codecs.open(file_path, "r", "utf_8_sig")
        file_text = file_obj.read()
        file_obj.close()

        # for line in file_text:
        #    print(line)
        print(file_text)


def define_topic():
    article = show_available_articles()
    if article == 'm':
        display_title_bar()
    else:
        topic = show_available_topics()
        if topic == 'm':
            display_title_bar()
        else:
            print('\nHere we will define article topic!\n')


texts = [
    'planetary_system_ru.txt'
]


topics = [
    'astronomy',
    'healthy lifestyle',
    'olympic games'
]

diff_texts_path = '.\data\diff_texts\\'


def main():
    choice = ''
    article = ''
    topic = ''

    while choice != 'q':
        display_title_bar()
        choice = get_user_choice()

        if choice == '1':
            find_key_words()

        elif choice == '2':
            define_topic()

        elif choice == 'q':
            quit()


if __name__ == '__main__':
    main()
