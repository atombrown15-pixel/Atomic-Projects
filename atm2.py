# Initialize account balance and tracking stats
balance = 500000.00  # Stored as a float to allow kobo/decimals
transfer_count = 0
daily_transfer_total = 0.00  # Stored as a float to track accurate limits

while True:
    # Display Options
    free_left = 3 - transfer_count if transfer_count < 3 else 0
    print("\n--- Atomic ATM Machine ---")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Transfer")
    print("5. Exit")

    choice = input("Select an option (1-5): ")

    # Handle Check Balance
    if choice == '1':
        print("\n=====================================")
        print("          ACCOUNT BALANCE REPORT     ")
        print("=====================================")
        print(f"Current Available Balance: #{balance:.2f}") # 💡 :.2f prints clean decimals (kobo)
        print(f"Transfers Sent Today:      {transfer_count} ({free_left} free left)")
        print(f"Daily Limit Utilization:   #{daily_transfer_total:.2f} / #50,000.00")
        print("=====================================")

    # Handle Deposit
    elif choice == '2':
        try:
            amount = float(input("Enter deposit amount: #")) # 💡 Changed from int to float
            if amount >= 100:
                balance += amount
                print(f"#{amount:.2f} deposited successfully.")
            else:
                print("Invalid amount. Must be greater than 100.")
        except ValueError:
            print("⚠️ Error: Please enter a valid number (decimals allowed), not text.")

    # Handle Withdrawal
    elif choice == '3':
        try:
            amount = float(input("Enter withdrawal amount: #")) # 💡 Changed from int to float
            if amount <= balance:
                if amount >= 1000:
                    balance -= amount
                    print(f"#{amount:.2f} withdrawn successfully.")
                else:
                    print("Amount must be greater than 1000.")
            else:
                print("Insufficient funds!")
        except ValueError:
            print("⚠️ Error: Please enter a valid number, not text.")

    # Handle Transfer with Fee, Daily Limit Tracker, and 10-Digit validation
    elif choice == '4':
        # 💡 NEW: 10-digit NUBAN Account Number Validation Loop
        while True:
            account_number = input("Enter 10-digit destination account number: ").strip()
            if account_number.isdigit() and len(account_number) == 10:
                break # Code moves forward only if it's exactly 10 numeric digits
            print("❌ Invalid! Account number must contain only numbers and be exactly 10 digits long.")

        try:
            amount = float(input("Enter amount to transfer: #")) # 💡 Changed from int to float

            # Calculate fee based on the number of transfers done
            if transfer_count >= 3:
                fee = 10.00
                print("💡 Notice: You have used your 3 free daily transfers. A #10.00 fee applies.")
            else:
                fee = 0.00

            total_deduction = amount + fee

            # Transfer Limit Rules
            if daily_transfer_total + amount > 50000:
                remaining_limit = 50000.00 - daily_transfer_total
                print(f"❌ Transfer Blocked! This transaction exceeds your #50,000 daily limit.")
                print(f"👉 You can only transfer up to #{remaining_limit:.2f} more for the rest of the day.")
                continue

            if amount >= 100:
                if total_deduction <= balance:
                    balance -= total_deduction
                    transfer_count += 1
                    daily_transfer_total += amount
                    print(f"\n✅ #{amount:.2f} transferred successfully to {account_number}!")
                    print(f"Fee charged: #{fee:.2f}")
                else:
                    print(f"Insufficient funds! You need #{total_deduction:.2f} (including fees) but only have #{balance:.2f}.")
            else:
                print("Invalid amount. Minimum transfer is #100.")
        except ValueError:
            print("⚠️ Error: Please enter a valid transfer number, not text.")

    # Handle Exit
    elif choice == '5':
        print("Thank you for using Atomic ATM. Goodbye!")
        break

    # Handle Invalid Menu Choice
    else:
        print("Invalid choice. Please select 1, 2, 3, 4, or 5.")

