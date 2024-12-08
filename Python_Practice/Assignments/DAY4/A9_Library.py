print("Welcome to SAI's LIBRARY")
books = ["Wings of Fire", "Icon of Millions", "Ponniyin Selvan",]

# Main program loop
while True:
    print("____________________")
    print("Library Menu:")
    print("1. View Available Books")
    print("2. Borrow a Book")
    print("3. Return a Book")
    print("4. Exit")
    print("____________________")
    choice = input("Enter your choice (1-4): ")


    if (choice == "1"):  # View Available Books
        if books:
            print("____________________")
            print("Available Books:")
            for book in books:
                print(book)
            
        else:
            print("No books are currently available.")

    elif (choice == "2"):  # Borrow a Book
        book_name = input("Enter the name of the book you want to borrow: ")
        if book_name in books:
            books.remove(book_name)
            print("You have borrowed ",book_name,". Please return it on time.")
        else:
            print("Sorry, the book ",book_name," is not available.")

    elif (choice == "3"):  # Return a Book
        book_name = input("Enter the name of the book you want to return: ")
        books.append(book_name)
        print("Thank you for returning ",book_name)

    elif (choice == "4"):  # Exit
        print("Thank you for using the library system. Goodbye!")
        break

    else:
        print("Invalid choice! Please enter a number between 1 and 4.")
