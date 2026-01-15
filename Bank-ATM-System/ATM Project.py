# Developer name : S.J.J and C.S.M

import time

PASSWORD_FILE = "confirm_pass.txt"

# Login Page
print("\n\t\t\t...... SJ Bank Login Page ......")
print("\n.... Insert your card in ATM machine ....\n")
time.sleep(2)

name = input("Enter your name : ")
mobile_no = int(input("Enter your mobile number : "))
balance = int(input("Enter your balance : "))

print("\n\t\t\tWELCOME to SJ & CM Bank")

password = input("\nEnter your password : ")

with open(PASSWORD_FILE, "r") as f:
    saved_password = f.read()

if password == saved_password:

    while True:
        print("""
Enter 1 for Credit
Enter 2 for Debit
Enter 3 for Balance Enquiry
Enter 4 for Change Password
Enter 5 for Exit
""")

        choice = int(input("Enter your choice : "))

        # Credit
        if choice == 1:
            amount = int(input("Enter amount to credit : "))
            balance += amount
            print(f"\nDear {name}, Rs.{amount} credited.")
            print(f"Available Balance : Rs.{balance}")

        # Debit
        elif choice == 2:
            amount = int(input("Enter amount to debit : "))
            if amount <= balance:
                balance -= amount
                print(f"\nDear {name}, Rs.{amount} debited.")
                print(f"Remaining Balance : Rs.{balance}")
            else:
                print("\nOOPS! Insufficient Balance")

        # Balance Enquiry
        elif choice == 3:
            print(f"\nDear {name}, Available Balance : Rs.{balance}")

        # Change Password
        elif choice == 4:
            old_pass = input("Enter old password : ")

            with open(PASSWORD_FILE, "r") as f:
                if old_pass == f.read():
                    new_pass = input("Enter new password : ")
                    with open(PASSWORD_FILE, "w") as f:
                        f.write(new_pass)
                    print("\nPassword changed successfully!")
                else:
                    print("\nIncorrect old password!")

        # Exit
        elif choice == 5:
            print("\nThank you for using SJ Bank ATM")
            break

        else:
            print("\nInvalid choice!")

else:
    print("\nOOPS! Invalid Password")
