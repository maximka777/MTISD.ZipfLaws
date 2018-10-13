import os


def display_title_bar():
    os.system('cls')

    print("\t**********************************************")
    print("\t***************** Zipf Laws ******************")
    print("\t**********************************************")


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
        print("[" + str(i+1) + "] " + text)
        i += 1
    print("[m] Menu")
    return input("Your choice: ")


def show_available_topics():
    print("\nSelect one of the following topics:")
    i = 0
    for topic in topics:
        print("[" + str(i+1) + "] " + topic)
        i += 1
    print("[m] Menu")
    return input("Your choice: ")


texts = [
    'planetary_system_ru.txt'
]


topics = [
    'astronomy',
    'healthy lifestyle',
    'olympic games'
]


def main():
    choice = ''
    article = ''
    topic = ''

    while choice != 'q':
        display_title_bar()
        choice = get_user_choice()

        if choice == '1':
            article = show_available_articles()
            if article == 'm':
                display_title_bar()
            else:
                print('\nHere we will define article key words!\n')

        elif choice == '2':
            article = show_available_articles()
            if article == 'm':
                display_title_bar()
            else:
                topic = show_available_topics()
                if topic == 'm':
                    display_title_bar()
                else:
                    print('\nHere we will define article topic!\n')

        elif choice == 'q':
            quit()


if __name__ == '__main__':
    main()
