class Vehicles:
    def __init__(self,name="NONE",color="black",price=0.00):
        self.price=price;
        self.name=name;
        self.color=color;
    def printData(self):
        print("{0} is a {1} convertible worth ${2}.".format(self.name,self.color,self.price));
obj=Vehicles("Fer","red",60000.00)
obk=Vehicles("Jump","blue",10000.00);
obj.printData();
obk.printData();
format(obk.name);
