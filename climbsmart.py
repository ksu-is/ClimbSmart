print("Welcome to ClimbSmart")

name = input("Enter your name: ")
session_type = input("Type of climbing (bouldering/sport): ")
duration = input("How long did you climb (minutes): ")

pain = input("Did you feel pain? (yes/no): ")

if pain.lower() == "yes":
    area = input("Where is the pain (fingers/wrist/elbow): ")
    print("Pain recorded in", area)
else:
    print("No pain recorded")

print("Session logged for", name)