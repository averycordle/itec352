#!/usr/bin/env python3
"""Author: Avery Cordle
Description: List, Add and Delete Movies
"""

def display_menu():
    print("COMMAND MENU")
    print("List")
    print("Add")
    print("Delete")
    print("Exit")
    print()

def list(movie_list):
    i = 1 
    for movie in movie_list:
        print(str(i)+ ". "+ movie)
        i+=1
    print()

def add(movie_list):
    movie = input("Name: ")
    movie_list.append(movie)
    print(movie + " was added.\n")

def delete(movie_list):
    try:
        number = int(input("Enter a number: "))
        if number < 1 or number > len(movie_list):
            print("Invalid movie number.\n")
        else:
            movie = movie_list.pop(number -1)
            print(movie + " was deleted.\n")
    except:
        print("You must enter an integer")

def main():
    movie_list = ["Monty Python and the oly Grail",
                    "On the Waterfront",
                    "Cat on a Hot Tin Roof"]
    display_menu()

    while True:
        command = input("Give command: ")
        if command.lower() == "list":
            list(movie_list)
        elif command.lower() == "add":
            add(movie_list)
        elif command.lower() == "delete":
            delete(movie_list)
        elif command.lower() == "exit":
            break
        else:
            print("Not a valid command. Please try again.")
    
    print("Bye")

if __name__ == "__main__":
    main()
