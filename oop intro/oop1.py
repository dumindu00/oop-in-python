# Define Class
class Cars:
    # Constructor (Initializes an Object)
    def __init__(self, brand, color, country): # Object Initialization
        self.brand = brand # Attributes
        self.color = color # Attributes
        self.country = country # Attributes
    
    def start_engine(self): # Method (behavior)
        print(f"{self.brand}  engine starting.")
    
    def stop_engine(self): # Method (behavior)
        print(f"{self.brand} engine stopped.")
        

# Creates objects (instances) of the class
car1 = Cars("BMW", "Red", "Germany")
car2 = Cars("Ford", "Blue", "USA")

# Call methods
car1.start_engine()
car1.stop_engine()

car2.start_engine()
car2.stop_engine()

# Access attributes
print(car1.brand)
print(car1.country)
