# class Car:
#     def __init__(self, name, year, detail):
#         self.name = name
#         self.year = year
#         self.detail = detail
    
# class Details:
#     def __init__(self, color, model):
#         self.color = color
#         self.model = model

# detail1 = Details("Green", "GTR")
# car1 = Car("BMW", "2015", detail1)
# car1.detail
# print(car1.detail.model)




class User:
    def __init__(self, name, accountNumber, balance):
        self.name = name
        self.accountNumber = accountNumber
        self.balance = balance
        
        
    def deposit(self, amount):
        self.balance += amount
    
    def withdraw(self, much):
        self.balance -= much
    
    
    
    
    def message(self):
        print(f"User: {self.name}. AccountNumber: {self.accountNumber}. Your balance $: {self.balance}")

class Investments(User):
    
    def __init__(self, name, accountNumber, investmentAmount):
        super().__init__(name, accountNumber, balance=None)
        self.investmentAmount = investmentAmount
        self.remain = 0
        
        
    def stock(self, name):
        if self.investmentAmount <= 10000:
            print(f"{self.name}Invested in stocks successfully.Invested amount $: {self.investmentAmount}.00")
        else:
            self.remain = self.investmentAmount - 10000
            print(f"{self.name}, $: 10000.00 invested in stocks remain ${self.remain}.00 send to the bond account")
        
    def bond(self):
        print(f"$: {self.remain}.00 invested in bonds")
        
        
        
    def bond():
        
        

user1 = User("smith", "23",34)
user1.message()
user1.deposit(45)
user1.message()


user2 = Investments(user1, "Dave", 56777)
user2.stock()
user2.bond()




# Inheriting from another Class
# When inherit from class, the New considered a "type of Parent Class"  #
# You can reuse the code from the Parent Class with out Rewriting it #
# "And also Can Override Methods if want to Change Behavior" #

# if you want some data from parent class no inheritance needed #
