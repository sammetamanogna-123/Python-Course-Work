amount = int(input("Enter the amount: "))

if amount > 10000:
    print("Trip to Goa")
elif 8000 <= amount < 10000:
    print("Clubings")
elif 5000 <= amount <8000:
    print("Go for Cafe")
elif 3000 <= amount < 5000:
    print("Shopping")
elif 1000 <= amount < 3000:
    print("Visit local places")
elif 500 <= amount < 1000:
    print("Order something")
else:
    print("Go for chai and sleep")
