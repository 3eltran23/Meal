from views.consoleUI import opt1,print_mainMenu


def main():
    while(True):
        print_mainMenu()
        option = int(input('Enter your choice: '))
        if option == 1:
            print("1")
            opt1()
        elif option ==2:
            print("2 - List all Meals by Category")
        else:
            break
        

if __name__ == "__main__":
    main()