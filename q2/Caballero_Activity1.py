#1 A GameCharacter class has a username that can be displayed and accessed by anyone.
class GameCharacter:
    def __init__(self, username, name,health, attack_power):
        self.__username = username
        self.name = name
        self.health = health
        self.attack_power = attack_power

#2 A BankAccount class has a balance that should NOT be accessed directly outside the
class BankAccount:
    def __init__(self, account_name, account_number, balance):
        self.account.name = account_name
        self.account_number = account_number
        self.__balance = balance

#3 A Vehicle class has an engineCode that should only be accessed within the class and its subclasses
class Vehicle:
    def __init__(self, make, model, engineCode):
        self.make = make
        self.model = model
        self._engineCode = engineCode

#4 A Student class has a schoolName that is safe for everyone to view and modify.
class Student:
    def __init__(self, name, age, schoolName):
        self.name = name
        self.age = age
        self.schoolName = schoolName

#5 A VotingSystem class has a voterID that must be hidden for security reasons.
class VotingSystem:
    def __init__(self, voterID):
        self.__voterID = voterID