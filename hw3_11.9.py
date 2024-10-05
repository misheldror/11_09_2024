# START

height: float = float(input("enter your height: "))

while 0.4 > height or height > 2.5:
    print("wrong input")
    height: float = float(input("enter your height: "))

# END

# START

num1: int = int(input("enter your number: "))
num2: int = int(input("enter your number: "))

for i in range(num1, num2 + 1) or range(num2, num1 - 1, -1):
    print(i, end=" ")

# END

# START

pie: float = 3.14
tries = 0
user_attempt: float = float(input("what is pie?"))
while user_attempt != pie and tries < 3:
    print("wrong input")
    tries += 1
    user_attempt: float = float(input("try again: "))

if user_attempt == pie:
    print("correct!")
else:
    print(f"pie is {pie}")

# START

beers_given: int = 0
while beers_given < 10:
    age: int = int(input("what's your age? "))
    if age >= 18:
        print("here is your beer")
        beers_given += 1
    else:
        print("too young")

# END