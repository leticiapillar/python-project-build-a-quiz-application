# Example file for LinkedIn Learning Course "Python: Build a Quiz App" by Joe Marini
# pyquiz.py -- Main starting point of the program


class QuizApp:
    def __init__(self):
        self.username = ""

    def startup(self):
        # print the greeting at startup
        self.greeting()

        # TODO: ask the user for their name
        self.username = input("What's your name? ")
        print(f"Welcome, {self.username}!")
        print()

    def greeting(self):
        print("-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~")
        print("~~~~~~ Welcome to PyQuiz! ~~~~~~")
        print("-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~")
        print()

    def menu_header(self):
        print("--------------------------------")
        print("Please make a selection:")
        print("(M): Repeat this menu")
        print("(L): List quizzes")
        print("(T): Take a quiz")
        print("(E): Exit program")

    def menu_error(self):
        print("That's not a valid selection. Please try again.")

    def goodbye(self):
        print("-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~")
        print(f"Thanks for using PyQuiz, {self.username}!")
        print("-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~")

    def menu(self):
        self.menu_header()

        # TODO: get the user's selection and act on it. This loop will
        # run until the user exits the app
        selection = ""
        while(True):
            selection = input("Selection? ")
            if len(selection) == 0:
                self.menu_error()
                continue

            selection = selection.capitalize()
            match selection[0]:
                case 'E':
                    self.goodbye()
                    break
                case 'M':
                    self.menu_header()
                    continue
                case 'L':
                    print("\nAvailable quizzes are: ")
                    # TODO list the quizzes
                    print("--------------------------------")
                    continue
                case 'T':
                    try:
                        quiznum = int(input("Quiz number: "))
                        print(f"You have select the quiz {quiznum}")
                        # TODO star the quiz
                    except:
                        self.menu_error()
                case _:
                    self.menu_error()


    # This is the entry point to the program
    def run(self):
        # Execute the startup routine - ask for name, print greeting, etc
        self.startup()
        # Start the main program menu and run until the user exits
        self.menu()


if __name__ == "__main__":
    app = QuizApp()
    app.run()
