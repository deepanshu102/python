class ComplexNumber:
    ###################################
    #   def _ _ init__ (self) is the constructor  parameterise
    ####################################
    def __init__(self,r=0,i=0):
        self.real=r;##->Self act as an This pointer
        self.img=i;
    def getData(self):
        print("{0}+{1}j".format(self.real,self.img));
    def printData(self):
        print("Real:-{0}\nImg:-{1}".format(self.real,self.img));
obj=ComplexNumber(10,3);
obj.getData();
obk=ComplexNumber();
obk.getData();
print("Class ID IS ",(id(ComplexNumber)));
print("Object id is ",(id(obj)));
obj.printData();
obk.printData();
