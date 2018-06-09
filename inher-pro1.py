'''
#############################################
->      class <P-class-name>:
            parent-class body
--->  class <child-class>(p-class-name):
            child-class  body
|___________|           |________________|
|parentclass|<------- |child-class     |
|___________|           |________________|               

##################################################'''

class Vehicle:
        def genral_usage(self):
            print("Genral use: Transporation");
class Car(Vehicle):
    def __init__(self):
        print("I am car");
        self.wheels=4;
        self.has_roof=True;
        
    def specific_usage(self):
        #self.genral_usage();
        print("Specific use: commute to work,vacation with family");
class MotorCycle(Vehicle):
    def __init__(self):
        print("I'm motor cycle");
        self.wheels=2;
        self.has_roof=False;
    def specific_usage(self):
      #########################################################
        self.genral_usage();#vehicle class function invoked
        ########################################################
        print("specific use: road Trip,racing");
car=Car();
car.specific_usage();
car.genral_usage();##Calling vehicle class function
Honda=MotorCycle();
Honda.specific_usage();
######################################################################

print("Car is the object  of Vehicle class",isinstance(car,Vehicle));
print("Car object is not the child of MotorCycle",isinstance(car,MotorCycle));
print("Car is the object of CAR class ",isinstance(car,Car));
'''
isinstance():- 

    -> isinstance(object,class-name) check that object of that class or not
    ->class-name:- class,type,tuple of classes and types
    ->object:- object to be checked
    ->bool isinstance(object,class-name)
    
'''
###########################################################################
'''
issubclass():-
        ->issubclass(object,classinfo)
         object=class to be checked
         classinfo=class,type,or tuple of classes and types
        ->
            IT'S RETURN BOOLEAN VALUE 
            ITS CHECK 2 CLASS ONE IS CHILD AND ONE IS PARENT
'''
print("CAR is the Child class of Vehicle",issubclass(Car,Vehicle));
print("Vehicle is not the child class CAR",issubclass(Vehicle,Car));
print("Motorcycle is not child of CAR ",issubclass(MotorCycle,Car))
