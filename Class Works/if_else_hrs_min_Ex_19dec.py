hrs,mins = tuple(map(int,input("Enter the hours and mins: ").split()))
if 0<=hrs<4 and 0<=mins<=59:
    print("Its high time. Better go to sleep")
elif 4<=hrs<12 and 0<=mins<=59:
    print("Good Morning. Have a great day")
elif 12<=hrs<16 and 0<=mins<=59:
    print("Good afternoon. Have a great lunch")
elif 16<=hrs<21 and 0<=mins<=59:
    print("Good evening. Have a great dinner")
else:
    print("Good night. Scroll Reels")
