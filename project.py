import os # Import OS module 

print(("ATENAS FRATERNITY").center(50))

def Data_Entry(option):
    # Append "a" mode is used to Enter the Data 
    if option == 'a':
        file = open(f"{os.getcwd()}/{sc_name}/Aviation_data.txt","a")
        content = file.write(f"\nEntry No. {entry} \nNAME: {name}   MOBILE NO. {phno}   EMAIL-ID: {email}")
        file.close()
    elif option == 'b':
        print("\n(1) Data Science & Analytics with Artificial Intelligence & Machine Learning \n(2) Full Stack Web Development")
        opt = int(input("> "))
        if opt == 1:
            course = "Data Science & Analytics with Artificial Intelligence & Machine Learning"
        elif opt == 2:
            course = "Full Stack Web Development"
        file = open(f"{os.getcwd()}/{sc_name}/IT_data.txt","a")
        content = file.write(f"\nEntry No. {entry} \n\nNAME: {name}   MOBILE NO. {phno}   EMAIL-ID: {email} \nCOURSE: {course}\n")
        file.close()
    elif option == 'c':
        file = open(f"{os.getcwd()}/{sc_name}/DigitalM_data.txt","a")
        content = file.write(f"\nEntry No. {entry} \nNAME: {name}   MOBILE NO. {phno}   EMAIL-ID: {email} ")
        file.close()
    else:
        print("Choose Appropriate Option !!!")

while True:
    # Main Menu
    print("\n1: To Enter The Student Data \n2: To Create School/College Directory \n3: To Rename The Directory \n4: To Read the Data \n5: To Remove The Directory \n")
    opt = int(input("> "))
    
    # To Enter the Student Data using Data_Entry
    if opt == 1:
        entry = input("Enter the Entry No. ")
        name = input("Enter the Name: ").title()
        phno = int(input("Enter the phone No. "))
        email = input("Enter the Email-ID: ").lower()
        sc_name = input("Enter the School/college Name: ")
        print("Choose the Interested Course: \n(a) Aviation   (b)  Information Technology   (c) Digital Marketing " )
        option = input("> ").lower()
        
        Data_Entry(option) # User-Defined Function
        
    # To Create School/College Directory              
    elif opt == 2:
        # os.getcwd Built- In Function to print current path 
        print(f"Current Directory Path: {os.getcwd()}") 
        folder = input("Enter the School/College Name: ").upper()
        os.mkdir(folder) # Built-In Function to create Directory 
        print(f"{folder} Directory created successfully !!")

    # To Rename the Directory 
    elif opt == 3:
        oldname = input("Enter the Current Folder Name: ")
        newname = input("Enter the New Name for the pervious Folder: ").upper()
        os.rename(oldname, newname) # Built-In Function to Rename the Directory
        print(f"{oldname} directory renamed to {newname} successfully !!")

    # To Read the Data 
    elif opt == 4:
        sc_name = input("Enter the School/College Name to read the data:  ").upper()
        option = int(input("Select Department: 1: Aviation    2: Information Tech.    3: Digital Marketing \n> "))
        if option == 1:
            dept = "Aviation_data.txt"
        elif option == 2:
            dept = "IT_data.txt"
        elif option == 3:
            dept = "DigitalM_data.txt"
        else:
            print("Select Valid Option !!")
        # Read "r" mode is used to Read the Data 
        file = open(f"{os.getcwd()}/{sc_name}/{dept}","r")  
        print("Student Data: \n",file.read())
        file.close()

    # To Remove the Directory
    elif opt == 5:
        folder = input("Enter the Directory Name: ")
        os.rmdir(folder) # Built-In Function to Remove the Directory
        print(f"Directory {folder} has been removed successfully !!")

    # To Exit the Program
    elif opt == 6:
        break
    else: 
        print("Entered Wrong Option...")
        
        
