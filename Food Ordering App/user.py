from admin import Restuarant


def register(self):
        self.full_name=input("Enter your name :")
        self.phone_number=int(input("Enter your phone number :"))
        self.Email=input("Enter your Email id :")
        self.Address=input("Enter your full address :")
        self.username=input("Enter user name")
        self.password=input("Enter your new passward :")
        self.user_dict={"name":self.full_name,"phone_number":self.phone_number,"Email":self.Email,"Address":self.Address,"username":self.username,"Password":self.password}
        self.user_id=len(self.user)+1
        self.user[self.user_id] = self.user_dict
        print("You are successfully registered your account")


def login(self):
    while True:
        username=input("enter your username")
        password=input("enter your password")
        if username==self.username:
            if password==self.password:
                print("successfully login")
                break
            else:
                print("Incorrect detail")
        else:
            print("Incorrect details")

def place_order(self):
    list_of_foods=[{"name":"Tandoori Chicken","price":250,"quantity":"4 pieces"},{"name":"Truffle Cake","price":900,"quantity":"500gm"},{"name":"Veg Burger","price":320,"quantity":"1 piece"}]
    print("This is the menu :")
    for i in list_of_foods:
        print(f"{list_of_foods.index(i)+1}. {i['name']} [{i['quanity']}] (INR{i['price']})")
    user_input=int(input("select the items you want to order \n1. Tandoori Chicken\n2. Veg Burger\n3. TruffleCake\n "))
    if user_input==1:
        self.ordered_items.append(list_of_foods[0])
        print(list_of_foods[0])
    elif user_input==2:
        self.orderd_items.append(list_of_foods[1])
        print(list_of_foods[1])
    elif user_input==3:
        self.ordered_items.append(list_of_foods[2])
        print(list_of_foods[2])
    else:
        print("choose the item from the menu")
    order=int(input("Do you want to confirm the order?\n1. yes\n2. no\n"))
    if order==1:
        print("order placed successfully")
    else:
        print("order cancelled")



def order_history(self):
    for i in self.ordered_items:
        print("previous orders\n ",i)
def edit_personal_details(self):
    for i in self.personal_details:
        self.personal_details[i]=input(f"enter the {i} you want to update : ")
    print("personal details updated successfully \n ",self.personal_details)


res=Restuarant()
print("Welcome to the food Ordering app")
while True:
    role=int(input("Please select the role of food ordering app"))
    if role==1:
        while True:
            admin_input=int(input("Enter your preference\n1. Add food items\n2. Edit food items\n3. Remove food items\n4.Show all food items\n0. Exit from the application"))
            if admin_input==1:
                res.food_items()
                new_item=int(input("Add more items \n1. yes\n2. no\n"))
                if new_item==1:
                    res.food_itemsss()
            elif admin_input==2:
                res.edit_food_items()
            elif admin_input==3:
                res.remove_items()
            elif admin_input==4:
                res.all_food_items()
            elif admin_input==0:
                print("Exit from the application")
                break
            else:
                print("Invalid input, Please select from the option")
    elif role==2:
        print("Rigster your account\n")
        res.register()
        print("Please login into your account\n")
        res.login()
        while True:
            options=int(input("Take the option below \n1. Place the order\n2. Show order history\n3. Edi personal details\n0. logout"))
            if options==1:
                res.place_order()
                add_orders=int(input("order more items \n1. yes\n2. NO\n"))
                if add_orders==1:
                    res.place_order()
            elif options==2:
                res.order_history()
            elif options==3:
                res.edit_personal_details()
            elif options==0:
                break
            print("Exit")
    elif role==0:
        break
    print("Thank You.")
x=res()   
x.register()
x.login()
x.place_order()
x.order_history()
x.edit_personal_details()

