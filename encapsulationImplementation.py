class Computer:
    
    def __init__(self):
        self.__maxprice = 900
        
    def sell(self):
        print("Selling price of the computer is {}".format(self.__maxprice))
    
    def setMaxPrice(self, price):
        self.__maxprice = price
        
comp = Computer()

comp.sell()

comp.__maxprice = 1000
comp.sell()

comp.setMaxPrice(1200)
comp.sell()