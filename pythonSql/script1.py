# class Solder:
#     def __init__(self, name, tagNumber, role):
#         self.name = name
#         self.tagNumber = tagNumber
#         self.role = role
        
#     def getDetails(self):
#         print(f"Solder name: {self.name}\nTagNumber: {self.tagNumber}\nPost: {self.role}")
    
    


# solder1 = Solder("Dave", 45765, "Sargent")
# solder1.getDetails() 

class User:
    def __init__(self, name, message):
        self.name = name
        self.message = message
    
    def say_hi_to(self, user):
        print(f"Sending message to {user.name}: hi {user.name}!. it is {self.name}")
        


user1 = User("dumindu", "hey man")
user2 = User("shakthi", "yo let's eat")

user1.say_hi_to(user2)
print("")
print(user1.name)
print(user1.message)
user1.name = "Dave"
user1.message = "how are you?"
print(user1.name)
print( user1.message)