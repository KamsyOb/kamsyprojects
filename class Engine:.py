class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower

    def start(self):
        print(f"Engine with {self.horsepower} horsepower started.")

class Car:
    def __init__(self, brand, engine):
        self.brand = brand
        self.engine = engine  # Aggregation: Car "has-a" Engine

    def drive(self):
        print(f"{self.brand} is driving.")
        self.engine.start()

# Creating an Engine instance
engine1 = Engine(150)

# Creating a Car instance and associating it with the Engine instance
car1 = Car("Toyota", engine1)

# Using the car
car1.drive()
# Output:
# Toyota is driving.
# Engine with 150 horsepower started.

# The engine object exists independently
engine1.start()
# Output: Engine with 150 horsepower started.
