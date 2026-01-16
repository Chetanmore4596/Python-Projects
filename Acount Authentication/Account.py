import mysql.connector                                       #Devloped By Sj AND CM

def login(my_cur):
    print("....Enter mobile no for Sign in....\n")
    u_mobile=int(input("Enter your mobile no : "))
    u_password=input("Enter your password : ")
    query='SELECT * FROM users where mobile=%s and password=%s'
    values=(u_mobile,u_password)
    my_cur.execute(query,values)
    my_cur.fetchall()
    count=my_cur.rowcount
    if count==0:
        print("!!..Wrong Mobile no OR password..!!")
    else:
        print("....Succesfull Login....")
        print("\n1.press 1 for display Account details")
        print("2.press 2 for delete Account")
        print("3.press 3 for update Account details")
        print("4.Exit")
        ch=int(input("Enter the choice : "))
        if ch==1:
            u_mobile=int(input("Enter the mobile Number : "))
            u_password=input("Enter your password : ")
            query='SELECT * FROM users where mobile=%s and password=%s'
            values=(u_mobile,u_password)
            my_cur.execute(query,values)
            for r in my_cur.fetchall():
                print("................\nYour Account Details\n................")
                print("Accountent id : ", r[0])
                print("Accountent Name :", r[1])
                print("Accountent address : ", r[2])
                print("Accountent email : ", r[3])
                print("Accountent  mobile no: ", r[4])
                print("Accountent  mobile no Current password is : ", r[5])
            
            print("\nYour Accounts Succesfully display..!!")
        elif ch==2:
            u_mobile=int(input("Enter your mobile no : "))
            u_password=input("Enter your password : ")
            query='SELECT * FROM users where mobile=%s and password=%s'
            values=(u_mobile,u_password)
            my_cur.execute(query,values)
            my_cur.fetchall()
            count=my_cur.rowcount
            if count==1:
                print("\n....Re-enter mobile no and password....")
                u_mobile=int(input("Enter your mobile no : "))
                u_password=input("Enter your password : ")
                sql = 'delete from users where mobile=%s and password=%s'
                values=(u_mobile,u_password)
                my_cur.execute(sql,values) 
                my_con.commit()
                print("\n",my_cur.rowcount,"Account are deleted") 
            else:
                print("Enter Valid Account..!!")

        elif ch==3:
            u_mobile=int(input("Enter your mobile no : "))
            u_password=input("Enter your password : ")
            query='SELECT * FROM users where mobile=%s and password=%s'
            values=(u_mobile,u_password)
            my_cur.execute(query,values)
            my_cur.fetchall()
            count=my_cur.rowcount
            if count==1:
                print("..........UPDATE..........")
                print("press 1 to update name")
                print("press 2 to update address")
                print("press 3 to update mobile no")
                print("press 4 to update password no")
                print("press 5 to Exit")
                print(".........................")
                c=int(input("Enter the choice what operation you perform to update : "))
                if c==1:
                    name=input("Enter new name : ")
                    mob=int(input("Ente mobile no : "))
                    sql = 'update users set name=%s where mobile=%s'
                    values=(name,mob)
                    my_cur.execute(sql)
                    my_con.commit()
                    print("\n!!..Name is Succesfully updated..!!")
                
                elif c==2:
                    address=int(input("Enter new address : "))
                    mob=int(input("Ente mobile no : "))
                    sql = 'update users set age=%s where mobile=%s'
                    values=(address,mob)
                    my_cur.execute(sql,values)
                    my_con.commit()
                    print("!!..address is Succesfully updated..!!")
                elif c==3:
                    email=int(input("Enter new email : "))
                    mob=int(input("Ente mobile no : "))
                    sql = 'update users set email=%s where mobile=%s'
                    values=(email,mob)
                    my_cur.execute(sql,values)
                    my_con.commit()
                    print("!!..email is Succesfully updated..!!")
                elif c==4:
                    passw=input("Enter new password : ")
                    mob=int(input("Ente mobile no : "))
                    sql = 'update users set password=%s where mobile=%s'
                    values=(passw,mob)
                    my_cur.execute(sql,values)
                    my_con.commit()
                    print("!!..password is Succesfully updated..!!")   
                
            else:  
                exit()
        
def register(my_con,my_cur):
    try:
        u_mobile=int(input("Enter the mobile Number : "))
        query='SELECT * FROM users where mobile=%s'
        Values=[u_mobile]
        my_cur.execute(query,Values)
        my_cur.fetchall()
        count=my_cur.rowcount
        if count==1:
            print("!!..Your Account is Alredy exist..!!")
        else:
            print("....Enter details....")
            u_id=int(input("Please enter your id : "))
            u_name=input("Please enter your name : ")
            u_address=input("Please enter your address  :")
            u_email=input("Please enter your email : ")
            u_mobile=int(input("Please enter your  mobile : "))
            u_password=input("Please enter your password : ")
            gen=input("Enter your gendar(sir,mam,other) : ")
            if gen=="sir":
                sql='insert into users values(%s,%s,%s,%s,%s,%s)'
                Values=(u_id,u_name,u_address,u_email,u_mobile,u_password)
                my_cur.execute(sql,Values)
                my_con.commit()
                print("Congratulation !",gen,"your Amazon Account has been Succesfully Created..!!")
            elif gen=="mam":
                sql='insert into users values(%s,%s,%s,%s,%s,%s)'
                Values=(u_id,u_name,u_address,u_email,u_mobile,u_password)
                my_cur.execute(sql,Values)
                my_con.commit()
                print(gen,"your Account is Succesfully Registor..!!")
            elif gen=="other":
                sql='insert into users values(%s,%s,%s,%s,%s,%s)'
                Values=(u_id,u_name,u_address,u_email,u_mobile,u_password)
                my_cur.execute(sql,Values)
                my_con.commit()
                print(gen,"your Account is Succesfully Registor..!!")
            else:  
                exit()
    except mysql.connector.Error as e:
        print(e)
try:
    #DataBase connectivity
    my_con=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Chetan~45",
    database="login_registration"
    )
    my_cur=my_con.cursor()
    #choices are Display
    while True:
        print("\n***********WELCOME TO AMAZON***********\n")
        print("PRESS 1 for Sign in")
        print("PRESS 2 for Sign up")
        print("PRESS 3 for Exit\n")
        ch=int(input("Enter the choice : "))
        if ch==1:
            login(my_cur)
        elif ch==2:
            register(my_con,my_cur)
        else:
            print("\n*******THANKS*******\n")
            exit()
   
except mysql.connector.Error as e:
    print(e)
    