# Chad Scott
# 09/21/18
# This is an assignment where the Chatbot is able to speak with the user to find out information about buying a car.

user = input("Hello, Whats your name?")
print("Hello",user)
print("Its nice to meet you. My name is Dan")
location = input("Where are you from?")
print("Sounds like a great place to be from!")
number = float(input("What is your favorite number?"))
print("my favorite number is 4 .")
print("Your number plus my number is", number + 4)
car = input("What is your dream car?")
print("Wow! ive always wanted a", car)
cost = float(input("What is the price of the car?"))
print("That is pretty expensive!")
loan = float(input("How many years would it take to pay out a loan for the car?"))
rate = float(input("What is the annual interest rate expected for the car?"))
rate = rate / 100 / 12
monthly_pay = (rate * cost) / (1 - (1 + rate) ** (-loan * 12))
print(monthly_pay)
print(monthly_pay * loan)
print("If you bought a ", car, "you would have a monthly payment of", monthly_pay, "I hope it fits your budget")
print("The total would be", monthly_pay * loan, "I hope you can purchase it. Anyways i have to go. Goodbye.")



