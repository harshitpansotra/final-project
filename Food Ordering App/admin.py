import json
class Restuarant:
    def __init__(self):
        self.foods={}
        self.food_id=len(self.foods)+1
        self.ordered_items=[]
        self.user={}
        self.user_id=len(self.user)+1

    def add_food_items(self):
        self.name=input("Enter the Food Item name :")
        self.Quantity=int(input("Enter Food Quantity : (kg) "))
        self.Price=int(input("Enter Food Price :"))
        self.Discount=int(input("Enter Discount :"))
        self.Stock=int(input("Enter Stock Value :"))
        self.item={"name":self.name,"Quantity":self.Quantity,"Price":self.Price,"Discount":self.Discount,"Stock":self.Stock}
        self.food_id=len(self.foods)+1
        self.foods[self.food_id] = self.item
        print(self.item)
        print(self.foods)
        with open("food_data.json","w") as f:
            json.dump(self.foods,f)
        print("Items added successfully ")

    def remove_food_items(self):
        x = input("Enter the Food id which you want to delete :")
        del self.foods[x]
        print("Remaining items available :",self.foods)

    def edit_food_items(self):
        f_id=int(input("Enter food id you want:"))
        for i in self.foods[f_id]:
            self.foods[f_id][i]=input(f"enter the {i} you want :")
        print("Food details updated successfully \n",self.foods)

    def all_food_items(self):
        print("list of all food items are")
        for i in self.foods:
            print("food id : ",i,"\n*******")
            for j in self.foods[i]:
                print(j,":",self.foods[i][j])

x=Restuarant()
x.add_food_items()
x.add_food_items()
x.add_food_items()
x.remove_food_items()
x.edit_food_items()
x.all_food_items()
