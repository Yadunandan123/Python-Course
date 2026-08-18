t=int(input("What is temperature today? "))
if t<20: 
    outfit="jacket"
    print("today we need to wear a ",outfit)
else:
    outfit= "t-shirt and shorts"
    print("today you need to wear a ",outfit)
r=str(input("Is it raining today?"))
if r=="yes":
    print("Bring an Umbrella")
else: 
    print("No, you are fine as of right now!")
w=int(input("What is the Wind Speed today?"))
if w>30:
    wb="yes"
    print("Wear a windbreaker jacket over your ",outfit)
else:
    wb="no"
    print("No need to wear windbreaker jacket")

has_puddles = input("Are there puddles on the ground? (yes/no): ")
if has_puddles == "yes":
    shoes = "boots"
    print("The ground is wet.")
    print("Wear", shoes)
else:
    shoes = "sneakers"
    print("The ground is dry.")
    print("Wear", shoes)

print("===== WEATHER OUTFIT PICKER =====")
print("Temperature:", t)
print("Outfit Chosen:", outfit)
print("Raining:", r)
print("Windbreaker Needed:", wb)
print("Shoes Chosen:", shoes)
print("===================================")
