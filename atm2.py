# Initialize account balance
balance = 5000
transfer_count = 0

while True:
    # Display Options
    free_left = 3 - transfer_count if transfer_count < 3 else 0
    print("\n--- Atomic ATM Machine ---")
    print(f"Current Balance: #{balance}")
    print(f"Transfers sent today: {transfer_count} (Free transfers left today: {free_left})")

    print("1. Deposit")
    print("2. Withdraw")
    print("3. Transfer")
    print("4. Exit")

    choice = input("Select an option (1-4): ")

    # Handle Deposit
    if choice == '1':
        try:
            # 💡 FIX: Shifted these lines 4 spaces to the right
            amount = int(input("Enter deposit amount: "))
            if amount >= 100:
                balance += amount
                print(f"#{amount} deposited successfully.")
            else:
                print("Invalid amount. Must be greater than 100.")
        except ValueError:
            print("⚠️ Error: Please enter a valid number, not text.")

    # Handle Withdrawal
    elif choice == '2':
        amount = int(input("Enter withdrawal amount: "))
        if amount <= balance:
            if amount >= 1000:
                balance -= amount
                print(f"#{amount} withdrawn successfully.")
            else:
                print("Amount must be greater than 1000.")
        else:
            print("Insufficient funds!")

    # Handle Exit
    elif choice == '4':
        print("Thank you for using Atomic ATM. Goodbye!")
        break

    # Handle Transfer with Fee
    elif choice == '3':
        amount = int(input("Enter amount to transfer: "))

        # Calculate fee based on the number of transfers done
        if transfer_count >= 3:
            fee = 10
            print("💡 Notice: You have used your 3 free daily transfers. A #10 fee applies.")
        else:
            fee = 0

        total_deduction = amount + fee

        if amount >= 100:
            if total_deduction <= balance:
                balance -= total_deduction
                transfer_count += 1  # Increment the transfer counter
                print(f"#{amount} transferred successfully. Fee charged: #{fee}")
            else:
                print(f"Insufficient funds! You need #{total_deduction} (including fees) but only have #{balance}.")
        else:
            print("Invalid amount. Minimum transfer is #100.")

    # Handle Invalid Menu Choice
    else:
        print("Invalid choice. Please select 1, 2, 3, or 4.")
