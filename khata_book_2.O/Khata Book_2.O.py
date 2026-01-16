# Contact Book Management System (Khata Book 2.O)
# Developers : Chetan More

import mysql.connector as mc

try:
    # ---------------- DATABASE CONNECTION ----------------
    mydb = mc.connect(
        host="localhost",
        user="root",
        password="",
        database="khata_book"
    )
    print("Database connected successfully!")

    mycur = mydb.cursor()

    # ---------------- MAIN MENU ----------------
    while True:
        print("\n_______________________________________")
        print("***** Welcome to Khata Book 2.O *****")
        print("_______________________________________")
        print("1. Create Account")
        print("2. Login")
        print("3. About Developer")
        print("4. Exit")

        choice = int(input("\nEnter your choice : "))

        # ---------------- ACCOUNT CREATION ----------------
        if choice == 1:
            print("\n***** Account Creation *****")

            name = input("Enter name : ")
            mobile_no = input("Enter mobile number : ")
            address = input("Enter address : ")
            dob = input("Enter date of birth : ")
            email_id = input("Enter email id : ")
            password = input("Enter password : ")

            query = """
                INSERT INTO users
                (name, mobile_number, address, date_of_birth, email_id, password)
                VALUES (%s,%s,%s,%s,%s,%s)
            """
            values = (name, mobile_no, address, dob, email_id, password)

            mycur.execute(query, values)
            mydb.commit()

            print("Account created successfully!")

        # ---------------- LOGIN ----------------
        elif choice == 2:
            print("\n***** Login *****")

            l_email = input("Enter email id : ")
            l_pass = input("Enter password : ")

            query = "SELECT * FROM users WHERE email_id=%s AND password=%s"
            mycur.execute(query, (l_email, l_pass))
            result = mycur.fetchall()

            if mycur.rowcount == 0:
                print("No account found!")
            else:
                print("Login successful!")

                mycur.execute(
                    "SELECT user_id FROM users WHERE email_id=%s AND password=%s",
                    (l_email, l_pass)
                )
                current_user_id = mycur.fetchone()[0]

                # ---------------- USER DASHBOARD ----------------
                while True:
                    print("\n1. Manage Contacts\n2. Manage Profile\n3. Logout")
                    option = int(input("Enter choice : "))

                    # ---------- CONTACT MANAGEMENT ----------
                    if option == 1:
                        print("\n1. Create Contact\n2. Update Contact\n3. Delete Contact\n4. Display Contacts")
                        c_choice = int(input("Enter choice : "))

                        # CREATE CONTACT
                        if c_choice == 1:
                            cname = input("Name : ")
                            cmobile = input("Mobile : ")
                            cemail = input("Email : ")
                            cdob = input("DOB : ")
                            caddress = input("Address : ")

                            query = """
                                INSERT INTO contacts
                                (name, mobile_number, email_id, date_of_birth, address, user_id)
                                VALUES (%s,%s,%s,%s,%s,%s)
                            """
                            mycur.execute(query, (cname, cmobile, cemail, cdob, caddress, current_user_id))
                            mydb.commit()
                            print("Contact added successfully!")

                        # UPDATE CONTACT
                        elif c_choice == 2:
                            cmobile = input("Enter contact mobile number : ")
                            new_name = input("Enter new name : ")

                            query = "UPDATE contacts SET name=%s WHERE mobile_number=%s AND user_id=%s"
                            mycur.execute(query, (new_name, cmobile, current_user_id))
                            mydb.commit()

                            if mycur.rowcount == 1:
                                print("Contact updated!")
                            else:
                                print("Contact not found!")

                        # DELETE CONTACT
                        elif c_choice == 3:
                            cmobile = input("Enter contact mobile number : ")

                            query = "DELETE FROM contacts WHERE mobile_number=%s AND user_id=%s"
                            mycur.execute(query, (cmobile, current_user_id))
                            mydb.commit()

                            if mycur.rowcount == 1:
                                print("Contact deleted!")
                            else:
                                print("Contact not found!")

                        # DISPLAY CONTACTS
                        elif c_choice == 4:
                            query = "SELECT * FROM contacts WHERE user_id=%s"
                            mycur.execute(query, (current_user_id,))
                            records = mycur.fetchall()

                            if not records:
                                print("No contacts found!")
                            else:
                                for r in records:
                                    print(r)

                        else:
                            print("Invalid choice!")

                    # ---------- PROFILE MANAGEMENT ----------
                    elif option == 2:
                        print("\n1. Update Profile\n2. Delete Profile")
                        p_choice = int(input("Enter choice : "))

                        if p_choice == 1:
                            name = input("New Name : ")
                            mobile = input("New Mobile : ")
                            address = input("New Address : ")
                            dob = input("New DOB : ")
                            email = input("New Email : ")
                            password = input("New Password : ")

                            query = """
                                UPDATE users SET
                                name=%s, mobile_number=%s, address=%s,
                                date_of_birth=%s, email_id=%s, password=%s
                                WHERE user_id=%s
                            """
                            mycur.execute(query, (name, mobile, address, dob, email, password, current_user_id))
                            mydb.commit()
                            print("Profile updated successfully!")

                        elif p_choice == 2:
                            mycur.execute("DELETE FROM users WHERE user_id=%s", (current_user_id,))
                            mydb.commit()
                            print("Profile deleted!")
                            exit()

                    elif option == 3:
                        print("Logged out successfully!")
                        break

        # ---------------- ABOUT DEVELOPER ----------------
        elif choice == 3:
            print("\n***** About Developer *****")
            print("Developers : Sahil Jadhav & Chetan More")
            print("Email      : chetanmore45@gmail.com")
            print("Location   : Sangola, Solapur, Maharashtra")

        # ---------------- EXIT ----------------
        elif choice == 4:
            print("Thank you for using Khata Book 2.O!")
            break

        else:
            print("Invalid choice!")

except mc.Error as e:
    print("Database error:", e)

