from Methods import *


def Main():
    print("Welcome to our cinema!")
    print("There are the options you can choose: \n1. Add a movie " \
    "\n2. View movies \n3. Book tickets \n4. Cancel tickets \n5. Exit programm")

    chosenOption = 0

    while chosenOption != 5:
        print("What service would you prefer?")
        chosenOption = input() 
        if chosenOption == "1":

            print("Enter movie name:")
            addMovie = input()

            print("Enter prise of ticket:")
            addPrize = int(input())

            addSeats = 55
            while addSeats > 50:
                print("Enter number of free seats:")
                addSeats = int(input())
                if addSeats > 50:
                    print("You can't have more than 50 free seats!")
                else:
                    AddMovie(addMovie, addPrize, addSeats)
                    break

            print("Your movies list was updated.")

        elif chosenOption == "2":
            print("Here is your movies list:")
            ToString()

        elif chosenOption == "3":
            print("Now you can book tickets.")
            print("Choose a movie:")
            chosenMovie = input()
            BookTickets(chosenMovie)
 
        elif chosenOption == "4":
            print("Select a movie which you want to cancel tickets:")
            movieTitle = input()
            CancelTickets(movieTitle)

        elif chosenOption == "5":
            print("Thank you for visiting our cinema, see you again!")
            break


if __name__ == '__main__':
    Main()
