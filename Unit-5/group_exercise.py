#create a class OrderManager
#Implement methods to do the following:
#- read a file called orders.json, store
#in a class variable called orderlist ...
#- get the total number of orders ...
#- get the person with the most orders
#- get the person with the largest total order value
#- ge the most expensive item ordered
#- get the most frequently ordered item
import json

class OrderManager:
    def __init__(self):
        self.orderlist = []

    def file_reader(self, input_file):
        with open(input_file, 'r') as input_file:
            self.orderlist = json.load(input_file)
        #return self.orders

    def total_orders(self):
        total_order = 0
        for item in self.orderlist: 
            total_order += len(item['orders'])
            
        return total_order

    #def most_orders(self):


o = OrderManager()

o.file_reader('orders.json')
print(o.total_orders())


    