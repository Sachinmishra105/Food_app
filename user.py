
import json
class User:
    def __init__(self):
        self.user_data = {}
        self.ordered_item = {}

    def Register(self):
        name = input("Enter your Name: ")
        Mobile_no = int(input("Enter your Mobile Number: "))
        self.Email = input("Enter your Email Address: ")
        Address = input("Enter your Address: ")
        self.Password = input("Enter your Password: ")
        Details = {"User_name":name,"User_Mobile_no":Mobile_no,"User_Email":self.Email,"User_Address":Address,"User_Password":self.Password}
        self.user_data[self.Email] = Details
        with open("user_data.json","w") as f:
            json.dump(self.user_data,f,indent=4)
        return self.user_data
    
    def login(self):
        print("********** Welcome To Login Page **********")
        with open("user_data.json","r") as f:
            data = json.load(f)

        Email = input("Enter your email address : ")
        key = input("Enter your Password: ")
        if Email==self.Email:
            if key==self.Password:
                return True                    
            else:
                return False
        else:
            return False
        

    def place_order(self):
        order_id = 0
        order_id +=1
        self.order_food = []
        food_list =[{"name":"Tandoori Chicken","Quantity":"4 Pieces","Price":240},
                    {"name":"Vegan Burger","Quantity":"1 Pieces","Price":320},
                    {"name":"Truffle","Quantity":"500gm","Price":900}
                    ]

        print("Menu : ")
        for i in food_list:
            print(i)   

        user_input = int(input("Select food items : "))
        if user_input ==0:
            self.order_food.append(food_list[0])

        elif user_input ==1:
            self.order_food.append(food_list[1])

        elif user_input ==2:
            self.order_food.append(food_list[2])

        else:
            print("Select items from Menu")

        print("Press 1 to Confir the order : ")
        print("Press 2 for cancellation : ")
        option = int(input("Enter choice : "))
        self.ordered_item[order_id] = self.order_food
        if option ==1:
            print("********** Order Placed Successfully **********")
            with open("order_history.json","w") as f:
                json.dump(self.ordered_item,f,indent=4)
        else:
            print("********** order cancelled **********")
          
        return self.order_food 

    def Order_History(self):
        for k,v in self.ordered_item.items():
            print(f"Order Id : {k}   || order details : {v}" )



    def Edit_profile(self):
        with open("user_data.json","r") as f:
            data = json.load(f)

        for k,v in data.items():
            print(f"User Phone No : {k} , User Details : {v} ") 

        mobile = int(input("EnterThe user Mobile No which you want to update : "))
        category = input("Enter the category which you want to update : ")
        updated_value = input("Enter updated value : ")
        data[mobile][category] = updated_value
        with open("user_data.json","w") as f:
            json.dump(data,f,indent=4)
        return data    
        
            
               



                    


           

            


        

      
            

        
