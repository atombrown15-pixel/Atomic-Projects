# Initialize account balance
balance = 5000

while True:
    # Display Options
    print("\n--- Atomic ATM Machine ---")
    print(f"Current Balance: #{balance}")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Exit")

    choice = input("Select an option (1-3): ")

    # Handle Deposit
    if choice == '1':
        amount = int(input("Enter deposit amount: "))
        if amount > 0:
            balance += amount
            print(f"#{amount} deposited successfully.")
        else:
            print("Invalid amount. Must be greater than 0.")

    # Handle Withdrawal
    elif choice == '2':
        amount = int(input("Enter withdrawal amount: "))
        if amount <= balance:
            if amount > 0:
                balance -= amount
                print(f"#{amount} withdrawn successfully.")
            else:
                print("Invalid amount.")
        else:
            print("Insufficient funds!")

    # Handle Exit
    elif choice == '3':
        print("Thank you for using Atomic ATM. Goodbye!")
        break

    # Handle Invalid Menu Choice
    else:
        print("Invalid choice. Please select 1, 2, or 3.")