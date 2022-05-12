# -*- coding: utf-8 -*-
"""
Created on Mon May  9 15:07:13 2022

@author: Kitti Korosi

"""

# implement the classes listed below 
class FoodItem(object):
    def __init__(self, price, name):
        self.price = price
        self.name = name
    def set_price(self, price):
        self.price = price
    def set_name(self, name):
        self.name = name
    def get_name(self):
        return self.name
    def get_price(self):
        return self.price
        
        
class Burger(FoodItem):
    def __init__(self, price, name):
        super(Burger, self).__init__(price, name)
        self.extra_cheese = FoodItem(1.5, "cheese")
        self.extra_mayo = FoodItem(0.5, "mayo")
        self.cheese_added = False
        self.mayo_added = False
        
    def customize(self):
        while True:
            print("Do you want some fancy extra staff? (cheese or mayo?)(Press done, if you do not wish to order anything else or exit if you want to cancel your order)")
            extra = input()            
            if extra.lower() == 'mayo' and not self.mayo_added:
                self.mayo_added = True
                print(self.extra_mayo.get_name() + ' added')
            elif extra.lower() == 'cheese' and not self.cheese_added:
                self.cheese_added = True
                print(self.extra_cheese.get_name() + ' added')
            elif extra.lower() == 'done':
                return 
            elif extra.lower() == 'no':
                return
            elif extra.lower() == 'exit':
                raise SystemExit()
            else:
                print("I'm sorry, we don't serve that.")
            continue
        
    def get_price(self):
        total_price = self.price + self.get_extra_price()
        return total_price
    
    def get_extra_price(self):
        total_price = 0
        if self.mayo_added:
            total_price += self.extra_mayo.get_price()
        if self.cheese_added:
            total_price += self.extra_cheese.get_price()
        return total_price
        
    def get_name(self):
        full_name = self.name
        if self.mayo_added:
            full_name += ' with ' + self.extra_mayo.get_name()
        if self.cheese_added:
            full_name += ' with ' + self.extra_cheese.get_name()
        return full_name
        
    
class Drink(FoodItem):
    def __init__(self, price, name):
        super(Drink, self).__init__(price, name)
        self.extra_ice = FoodItem(0, 'Super cool ice cube')    
        self.ice_added = False
        
    def customize(self):
        while True:
            print("Do you want to add ice?")
            ice = input()            
            if ice.lower() == 'yes' :
                self.ice_added = True
                print(self.extra_ice.get_name() + ' added')
            if ice.lower() == 'no' :
                self.ice_added = False
                print(self.extra_ice.get_name() + ' not added')
            if ice.lower() == 'done' or ice.lower() == 'no' or ice.lower() == 'yes':
                return
            else:
                print("No match")
                continue
            
    def get_name(self):
        full_name = self.name
        if self.ice_added:
            full_name += ' with ' + self.extra_ice.get_name()
        return full_name
    
    
class Side(FoodItem):
    def __init__(self, price, name):
        super(Side, self).__init__(price, name)
        self.side_added = False

        
    def customize(self):
        while True:
            print("What can I get for you? Chips or Fruit? (Press done, if you do not wish to order anything else or exit if you want to cancel your order)")
            choosen_side = input()            
            if choosen_side.lower() == 'chips':
                self.side_added = True
                self.name = 'chips'
                print(self.get_name() + ' added')
            elif choosen_side.lower() == 'fruit':
                self.side_added = True
                self.name = 'fruit'
                print(self.get_name() + ' added')

            elif choosen_side.lower() == 'done':
                return 
            elif choosen_side.lower() == 'no':
                return
            elif choosen_side.lower() == 'exit':
                raise SystemExit()
            else:
                print("I'm sorry, we don't serve that.")
            if self.side_added:
                return
            continue
            
    def get_name(self):
        full_name = self.name

        return full_name
    
        
class Combo(FoodItem):
    def __init__(self, price, name):
        super(Combo, self).__init__(price, name)
        self.combo = FoodItem(8, "Combo")
        self.combo_added = False
        self.burger = Burger(5, 'Burger')
        self.drink = Drink(2, 'Cola')
        self.side=Side(1.5, 'Side')

    def customize(self):
        print("First, Burger: ")
        self.burger.customize()
        print("Second, Drink: ")
        self.drink.customize()
        print("Third, Side: ")
        self.side.customize()
        
    def get_name(self):
        full_name = self.name
        full_name += ' with ' + self.burger.get_name()
        full_name += ' with ' + self.side.get_name()
        full_name += ' with ' + self.drink.get_name()
        return full_name
    
    def get_price(self):
        return self.price + self.burger.get_extra_price()

class Order:
    def __init__(self):
        self.items = []
        
    def add_burger(self, burger):
        burger.customize()
        self.items.append(burger)
    def add_drink(self, drink):
        self.items.append(drink)
        drink.customize()
    def add_side(self, side):
        self.items.append(side)
        side.customize()
    def add_combo(self, combo):
        self.items.append(combo)
        combo.customize()
        
    def get_recepie(self):
        total_price = 0
        for i in self.items:
            total_price += i.get_price()
            print('%s, %.2f' % (i.get_name(), i.get_price()))
        print('Total price: %.2f' % total_price)
 

def take_order(o:Order): 
    print('Welcome in our shop!')
    while True:
        print('What can I get for you? Burger, Side, Drink or Combo')
        selection = input() 
        if selection.lower() == 'burger':
            o.add_burger(burger=Burger(5, 'Burger'))
        elif selection.lower() == 'drink':
            o.add_drink(drink=Drink(2, 'Cola'))
        elif selection.lower() == 'side':
            o.add_side(side=Side(1.5, 'Side'))    
        elif selection.lower() == 'combo':
            o.add_combo(combo=Combo(8, 'Combo')) 
        elif selection.lower() == 'done':
            return
        else:
            print("I'm sorry, we don't serve that. ")
        
    
if __name__ == '__main__':
    o = Order()
    take_order(o)
    o.get_recepie()    