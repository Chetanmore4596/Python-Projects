#Developed by Chetan More
# Quiz Competition

#correct answers list
answers=[3,3,2,1,2,1,3,4,3,1]

#Student registration form
print("\t\t\t\t_______________________")
print("\t\t\t\tStudent Registration")
print("\t\t\t\t_______________________")
name = input("Enter your name : ")
Class = input("Enter your class : ")
roll_no = int(input("Enter your roll no : "))
email_id = input("Enter email id : ")
mob_no = int(input("Enter your mobile no : "))
print("____________________")

#Function for Displaying Instructions
def instruction():
    print("\t\t\t\t__________________________")
    print("\n\t\t\t\tImportant Instruction")
    print("\t\t\t\t__________________________")
    print("\n1)All questions are compulsory")
    print("2)Mobile is not allowed")
    print("3)Complete Quiz within 10 minutes")
    print("4)Enter choice in number format")
    print("5)Calculator is not allowed")
    print("____________________")

#Function for starting or stoping Quiz   
def ready():
    print("\t\t\t\t__________________________________")
    print("\n\t\t\t\tARE YOU READY FOR QUIZ ?")
    print("\t\t\t\t(enter in yes or no)")
    print("\t\t\t\t__________________________________")
    option = input("Enter your option : ")

    if(option=="yes" or option=="YES"):
        Quiz()
    else:
        exit()
        
#Function for Quiz Questions and answers
def Quiz():
    marks = 0
    correct=0
    incorrect=0
    
    #Question 1
    print( "\nQ1)What is the latest generation of intel processor ?")
    print("1)8th Generation\n2)10th Generation\n3)12th Generation\n4)none of the above")
    choice = int(input("Enter your choice : "))

    if choice == answers[0]:
        print("\nCongratulation ! your answer is correct")
        marks=marks+2
        correct = correct+1
    else:
        print("\nOPPS ! your answer is incorrect")
        incorrect=incorrect+1
    print("____________________")    
    #Question 2
    print( "\nQ2)What is the full form of GPU ?")
    print("1)Grand power unit\n2)Graphic portal unit\n3)Graphical processing unit\n4)none of the above")
    choice = int(input("Enter your choice : "))

    if choice == answers[1]:
         print("\nCongratulation ! your answer is correct")
         marks=marks+2
         correct = correct+1
   
    else:
        print("\nOPPS ! your answer is incorrect")
        incorrect=incorrect+1
    print("____________________")

    #Question 3
    print( "\nQ3)What is the full form of ios ?")
    print("1)Indian open system\n2)Iphone operating system\n3)Inter operating system\n4)none of the above")
    choice = int(input("Enter your choice : "))

    if choice == answers[2]:
         print("\nCongratulation ! your answer is correct")
         marks=marks+2
         correct = correct+1
   
    else:
        print("\nOPPS ! your answer is incorrect")
        incorrect=incorrect+1
    print("____________________")
    
    #Question 4
    print( "\nQ4)Which language is used to make ios application ?")
    print("1)Swift\n2)Java\n3)C\n4)none of the above")
    choice = int(input("Enter your choice : "))

    if choice == answers[3]:
         print("\nCongratulation ! your answer is correct")
         marks=marks+2
         correct = correct+1
   
    else:
        print("\nOPPS ! your answer is incorrect")
        incorrect=incorrect+1
    print("____________________")
    
    #Question 5   
    print( "\nQ5)Which country manufactures SAMSUNG Smartphones ?")
    print("1)North Korea\n2)South Korea\n3)Japan\n4)none of the above")
    choice = int(input("Enter your choice : "))

    if choice == answers[4]:
         print("\nCongratulation ! your answer is correct")
         marks=marks+2
         correct = correct+1
   
    else:
        print("\nOPPS ! your answer is incorrect")
        incorrect=incorrect+1
    print("____________________")
    
    #Question 6   
    print( "\nQ6)What is latest version of Android ?")
    print("1)Android 13\n2)Android 12\n3)Android 10\n4)none of the above")
    choice = int(input("Enter your choice : "))

    if choice == answers[5]:
         print("\nCongratulation ! your answer is correct")
         marks=marks+2
         correct = correct+1
   
    else:
        print("\nOPPS ! your answer is incorrect")
        incorrect=incorrect+1
    print("____________________")
    
    #Question 7   
    print( "\nQ7)Who is the CEO of google ?")
    print("1)Satya Nadella\n2)Narayan Murthi\n3)Sundar Pichai\n4)none of the above")
    choice = int(input("Enter your choice : "))

    if choice == answers[6]:
         print("\nCongratulation ! your answer is correct")
         marks=marks+2
         correct = correct+1
   
    else:
        print("\nOPPS ! your answer is incorrect")
        incorrect=incorrect+1
    print("____________________")
    
     #Question 8   
    print( "\nQ8)Who developed Java ?")
    print("1)Guido van rossum\n2)Dennis Ritchie\n3)Albert Einstein\n4)none of the above")
    choice = int(input("Enter your choice : "))

    if choice == answers[7]:
         print("\nCongratulation ! your answer is correct")
         marks=marks+2
         correct = correct+1
   
    else:
        print("\nOPPS ! your answer is incorrect")
        incorrect=incorrect+1
    print("____________________")
    
    #Question 9   
    print( "\nQ9)Which mobile Processor has most ratings in india ?")
    print("1)Helio g\n2)MediaTech\n3)Snapdragon\n4)none of the above")
    choice = int(input("Enter your choice : "))

    if choice == answers[8]:
         print("\nCongratulation ! your answer is correct")
         marks=marks+2
         correct = correct+1
   
    else:
        print("\nOPPS ! your answer is incorrect")
        incorrect=incorrect+1
    print("____________________")
    
    #Question 10   
    print( "\nQ10)What is the Full form of GTA ?")
    print("1)Grand theif auto\n2)Gate thor andreas\n3)Gyno theif auto\n4)none of the above")
    choice = int(input("Enter your choice : "))

    if choice == answers[9]:
         print("\nCongratulation ! your answer is correct")
         marks=marks+2
         correct = correct+1
   
    else:
        print("\nOPPS ! your answer is incorrect")
        incorrect=incorrect+1
    
    print("____________________")
    print("Dear ",name," from ",Class," You have successfully completed Quiz competition")
    print("Roll No : ",roll_no)
    print("Mobile No : ",mob_no)
    print("____________________")
    print("\nTotal marks obtained out of 20 : ",marks)
    print("Total count of correct answers : ",correct)
    print("Total count of incorrect answers : ",incorrect)

    if(marks>=18):
        print("You got Exellent! Grade")
    elif(marks>=15 and marks<18):
        print("You got Very Good! Grade")
    elif(marks>=7 and marks<15):
        print("You got Good! Grade")
    else:
        print("Opps! You Falied")
    print("____________________")
    print("\nCorrect answers of All quetions : ",answers)
    
instruction()
ready()

print("\n*****THANK-YOU*****")



