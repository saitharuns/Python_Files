print("TONI BANK OF INDIA")
balance = 1000.00 


while True:
    print("ATM Menu:")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")
    
    # Get user choice
    choice = input("Enter your choice (1-4): ")

    if choice == "1":  # Check Balance
        print(f"\nYour current balance is: Rs.",balance)

    elif choice == "2":  # Deposit Money
        deposit_amount = float(input("\nEnter the amount to deposit: Rs"))
        if deposit_amount > 0:
            balance += deposit_amount
            print(deposit_amount,": has been deposited. Your new balance is: Rs",balance)
        else:
            print("\nPlease enter a valid amount greater than 0.")
        

    elif choice == "3":  # Withdraw Money
        try:
            withdraw_amount = float(input("\nEnter the amount to withdraw: Rs"))
            if withdraw_amount > 0:
                if withdraw_amount <= balance:
                    balance -= withdraw_amount
                    print(f"\nYou have withdrawn Rs",withdraw_amount,". Your new balance is: Rs",balance)
                else:
                    print("\nInsufficient balance!")
            else:
                print("\nPlease enter a valid amount greater than 0.")
        except ValueError:
            print("\nInvalid input. Please enter a numeric value.")

    elif choice == "4":  # Exit
        print("\nThank you for using the ATM. Goodbye!")
        break

    else:
        print("\nInvalid choice! Please enter a number between 1 and 4.")
