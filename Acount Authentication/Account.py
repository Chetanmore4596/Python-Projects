import mysql.connector   # Developed By CM


# ---------------- LOGIN FUNCTION ----------------
def login(my_cur, my_con):
    print("\n.... Enter mobile number for Sign In ....\n")

    u_mobile = int(input("Enter your mobile number : "))
    u_password = input("Enter your password : ")

    query = "SELECT * FROM users WHERE mobile=%s AND password=%s"
    values = (u_mobile, u_password)

    my_cur.execute(query, values)
    records = my_cur.fetchall()

    if my_cur.rowcount == 0:
        print("!! Wrong mobile number OR password !!")
        return

    print(".... Successful Login ....")

    while True:
        print("\n1. Display Account Details")
        print("2. Delete Account")
        print("3. Update Account Details")
        print("4. Exit")

        ch = int(input("Enter your choice : "))

        # -------- DISPLAY ACCOUNT --------
        if ch == 1:
            my_cur.execute(query, values)
            for r in my_cur.fetchall():
                print("\n******** Account Details ********")
                print("ID       :", r[0])
                print("Name     :", r[1])
                print("Address  :", r[2])
                print("Email    :", r[3])
                print("Mobile   :", r[4])
                print("Password :", r[5])

            print("\nAccount details displayed successfully!")

        # -------- DELETE ACCOUNT --------
        elif ch == 2:
            sql = "DELETE FROM users WHERE mobile=%s AND password=%s"
            my_cur.execute(sql, values)
            my_con.commit()

            if my_cur.rowcount == 1:
                print("Account deleted successfully!")
                break
            else:
                print("Invalid account details!")

        # -------- UPDATE ACCOUNT --------
        elif ch == 3:
            print("\n******** UPDATE MENU ********")
            print("1. Update Name")
            print("2. Update Address")
            print("3. Update Email")
            print("4. Update Password")
            print("5. Exit")

            c = int(input("Enter your choice : "))

            if c == 1:
                name = input("Enter new name : ")
                sql = "UPDATE users SET name=%s WHERE mobile=%s"
                my_cur.execute(sql, (name, u_mobile))

            elif c == 2:
                address = input("Enter new address : ")
                sql = "UPDATE users SET address=%s WHERE mobile=%s"
                my_cur.execute(sql, (address, u_mobile))

            elif c == 3:
                email = input("Enter new email : ")
                sql = "UPDATE users SET email=%s WHERE mobile=%s"
                my_cur.execute(sql, (email, u_mobile))

            elif c == 4:
                password = input("Enter new password : ")
                sql = "UPDATE users SET password=%s WHERE mobile=%s"
                my_cur.execute(sql, (password, u_mobile))

            elif c == 5:
                break

            else:
                print("Invalid choice!")

            my_con.commit()
            print("Account updated successfully!")

        # -------- EXIT --------
        elif ch == 4:
            break

        else:
            print("Invalid choice!")


# ---------------- REGISTER FUNCTION ----------------
def register(my_con, my_cur):
    try:
        u_mobile = int(input("Enter mobile number : "))

        my_cur.execute("SELECT * FROM users WHERE mobile=%s", (u_mobile,))
        my_cur.fetchall()

        if my_cur.rowcount == 1:
            print("Account already exists!")
            return

        print("\n.... Enter Registration Details ....")

        u_id = int(input("Enter ID : "))
        u_name = input("Enter name : ")
        u_address = input("Enter address : ")
        u_email = input("Enter email : ")
        u_password = input("Enter password : ")
        gen = input("Enter gender (sir/mam/other) : ")

        sql = "INSERT INTO users VALUES (%s,%s,%s,%s,%s,%s)"
        values = (u_id, u_name, u_address, u_email, u_mobile, u_password)

        my_cur.execute(sql, values)
        my_con.commit()

        print(f"Congratulations {gen}! Your Amazon account has been created successfully!")

    except mysql.connector.Error as e:
        print("Database Error:", e)


# ---------------- MAIN PROGRAM ----------------
try:
    my_con = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Chetan~45",
        database="login_registration"
    )

    my_cur = my_con.cursor()

    while True:
        print("\n*********** WELCOME TO AMAZON ***********\n")
        print("1. Sign In")
        print("2. Sign Up")
        print("3. Exit")

        ch = int(input("Enter your choice : "))

        if ch == 1:
            login(my_cur, my_con)

        elif ch == 2:
            register(my_con, my_cur)

        elif ch == 3:
            print("\n******* THANK YOU *******\n")
            break

        else:
            print("Invalid choice!")

except mysql.connector.Error as e:
    print("Database connection failed!")
    print("Error:", e)
