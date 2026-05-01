print("Welcome to ClimbSmart")

name = input("Enter your name: ")
session_type = input("Type of climbing (bouldering/sport): ")
duration = input("How long did you climb (minutes): ")
intensity = input("Rate the session intensity from 1-10: ")
pain = input("Did you feel pain? (yes/no): ")
area = ""

if pain.lower() == "yes":
    area = input("Where is the pain (fingers/wrist/elbow): ")
    print("Pain recorded in", area)
else:
    print("No pain recorded")

file = open("sessions.txt", "a")
file.write(name + "," + session_type + "," + duration + "," + intensity + "," + pain + "," + area + "\n")
file.close()

print("\n--- SESSION SUMMARY ---")
print("Name:", name)
print("Type:", session_type)
print("Duration:", duration)
print("Intensity:", intensity)
print("Pain:", pain)
if area != "":
    print("Pain Area:", area)

print("Session logged for", name)