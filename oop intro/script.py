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
        self.balance = much
    
    
    
    
    def message(self):
        print(f"User: {self.name}. AccountNumber: {self.accountNumber}. Your balance $: {self.balance}")

class Investments(User):
    
    def __init__(self, name, accountNumber, investmentAmount):
        super().__init__(name, accountNumber)
        self.investmentAmount = investmentAmount
        
        
    def stock(self):
        if self.investmentAmount <= 10000:
            self.remain  = self.investmentAmount
            print(f"Invested in stocks successfully.Invested amount $: {self.investmentAmount}")
            
        
    def bond():
        
        

user1 = User("pakaya", "23",34)
user1.message()
user1.deposit(45)
user1.message()