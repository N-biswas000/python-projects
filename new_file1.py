name,char=input("Enter Your Name and a charecter (You have to put comma in middle)").split(",")
print(f"Your names length is{len(name)}")
print(f"Your Selected Charecter is{name.strip().lower().count(char.strip().lower())}")

#Aakash---aakash
#A--a

#name.lower().count()
#char.lower()

#"Aakash  "------>"Aakash"------>"aakash"
#"  A "------>"A"------>"a"

#name.strip.lower().count()
#char.strip.lower()

