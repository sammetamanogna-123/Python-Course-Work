ct = int(input("Enter the votor id: "))
id={123,345,456,678,987}
age=int(input("Enter the age: "))
if ct in id:
    if age>=18:
        print("Congrats, You can vote")
    else:
        print("You are under age")
else:
    print("You need to be indian to vote")
