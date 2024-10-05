# START

min: int = int(input("how many minutes? "))
hour: int = min // 60
left: int = min % 60

print(f"{hour} hours and {left} minutes.")

# END