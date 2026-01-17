#Calculate the average of 3 numbers
def calculate_average(num1: int, num2: int, num3: int):
    average = (num1 + num2 + num3) / 3
    return average

#adds ten percent sales tax
def add_tax(bill_total: int):
    total = bill_total*1.1
    return total

#super cool ai that says hi to user
def greet_user(name):
    return "Hello " + name