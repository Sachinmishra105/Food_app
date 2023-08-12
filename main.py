from Admin import *
from user import *
import sys

admin = Admin()
user = User()
print("*************** Welcome to Food Ordering App ***************")
while True:
    print("Press 1 for Admin Login")
    print("Press 2 for User Login")
    print("Press 3 for Exit")
    option = int(input("Enter your choice : "))
    if option ==1:
        print("********** Welcome to Admin Login Page **********")
        print("Press 1 for Add Food Items")
        print("Press 2 for Edit Food Items")
        print("Press 3 for View Food Items")
        print("Press 4 for Remove Food Items")
        choice = int(input("Enter your choice : "))
        if choice ==1:
            admin.Add_food_items()
        elif choice == 2:
            admin.Edit_Food_items()
        elif choice ==3:
            admin.View_Food_items()
        elif choice ==4:
            admin.Remove_Food_item()
        else:
            print("Please choose right option") 

    elif option ==2:
        print("********** Welcome to User Login Page **********")
        print("Press 1 for Register ")
        print("Press 2 for Log in ")
        choice = int(input("Enter your choice : "))
        if choice ==1:
            user.Register()
        elif choice ==2:
            temp = user.login()
            if temp:
                print("Press 1 for Place Order")
                print("Press 2 for Order History")
                print("Press 3 for update Profile")
                option = int(input("Enter your Option : "))
                if option ==1:
                    user.place_order()
                elif option ==2:
                    user.Order_History()
                elif option ==3:
                    user.Edit_profile()
                else:
                    print("Please choose correct option ") 
            else:
                print("Please provide valid information")
        else:
            print("Please input valid option")

    elif option == 3:
        print("Thanks for using this App")
        sys.exit()  
    else:
        print("Please provide valid input")                             
            




