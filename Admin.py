
import json
class Admin:
    def __init__(self):
        self.food_id = 0
        self.food_item = {}
        
    def Add_food_items(self):
        self.food_id +=1
        food_name = input("Enter food name: ")
        Quantity = input("Enter Quantity: ")
        price = float(input("Enter Price:" ))
        discount = float(input("Enter Discount: "))
        stock = int(input("Enter Stock: " ))
        food_item = {"Food_id":self.food_id,"Food_Name":food_name,"Food_Quantity":Quantity,"Food_Price":price,"Food_discount":discount,"Food_Stock":stock,}
        self.food_item[self.food_id] = food_item
        with open("food_item.json","w") as f:
            json.dump(self.food_item,f,indent=4)
        print("********** Food Item added Successfully **********")    
        return self.food_item
    
    def Edit_Food_items(self):
        with open("food_item.json","r") as f:
            ele = json.load(f)
        for k,v in ele.items():
            print("Food Id :",k,"Food Item : ",v)
        id = (input("Enter food id which you want to edit :"))
        category = input("Enter a category which you want to update :")
        updated_value = input("Enter updated value :")
        ele[id][category] = updated_value
        with open("food_item.json","w") as f:
            json.dump(ele,f,indent=4)
        print("********** Food Item Updated Successfully **********")    
        return ele
    
    def View_Food_items(self):
        with open("food_item.json","r") as f:
            ele = json.load(f)
        for k,v in ele.items():
            print("Food Id :",k,"Food Item : ",v)
        return ele    

    
    def Remove_Food_item(self):
        with open("food_item.json","r") as f:
            ele = json.load(f)
        for k,v in ele.items():
            print("Food Id :",k,"Food Item : ",v)
        id = (input("Enter food id which you want to delete :"))
        del ele[id]
        with open("food_item.json","w") as f:
            json.dump(ele,f,indent=4)
        return ele    
    
   
