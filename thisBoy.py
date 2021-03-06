
def display_menu():
    print("COMMAND MENU")
    print("List")
    print("Add")
    print("Delete")
    print("Exit")
    print()

def list(movie_list):
    if len(movie_list) == 0:
        print("There are no movies in the list\n")
    else:
        i = 1
        for row in movie_list:
            print(str(i) + ". " + row[0] + " (" + str(row[1]) + ")")
            #print(i, row[0], row[1])
            i+=1
        print()

def add(movie_list):
    name = input("Name of Movie: ")
    year = input("Year Published: ")
    movie = []
    movie.append(name)
    movie.append(year)
    movie_list.append(movie)
    print(movie[0] + " was added.\n")

def delete(movie_list):
    try:
        number = int(input("Number: "))
        if number < 1 or number > len(movie_list):
            print("Invalid number.\n")
        else:
            movie = movie_list.pop(number -1)
            print(movie[0] + " was deleted.")
    except:
        print("You must enter an integer.\n")

def main():
    movie_list = [["Monty Python and the Holy Grail", 1975],
                    ["On the Waterfront", 1954],
                    ["Cat on a Hot Tin Roof", 1958]]
    display_menu()

    while True:
        display_menu()
        command = input("Command: ")
        if command.lower() == "list":
            list(movie_list)
        elif command.lower() == "add":
            add(movie_list)
        elif command.lower() == "delete":
            delete(movie_list)
        elif command.lower() == "exit":
            break
        else:
            print("Not a valid command. Please try again.\n")
    print("Bye")

if __name__ == "__main__":
    main()
