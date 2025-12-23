# Real-time Example: Online Shopping Product Details

# Taking inputs
product_id = int(input("Enter Product ID: "))
product_name = input("Enter Product Name: ")
price = float(input("Enter Price: "))

# List: categories separated by commas
categories = list(input("Enter Categories (comma-separated): ").split(","))

# Tuple: stock details
available_stock = int(input("Enter Available Stock: "))
sold_items = int(input("Enter Sold Items: "))
stock_details = (available_stock, sold_items)

# Discount percentage
discount = float(input("Enter Discount Percentage: "))

# Set: unique features
features = set(input("Enter Product Features (comma-separated): ").split(","))

# Dictionary: supplier details
supplier_name = input("Enter Supplier Name: ")
supplier_contact = input("Enter Supplier Contact Number: ")
supplier_location = input("Enter Supplier Location: ")
print()

# 1. Using Comma Separation (sep=',')

print("Product ID, Name, Price:", product_id, product_name, price, sep=" ")
print()

# 2. Using Percentage Formatting (% operator)

print("Product Discount: %.2f%%" % discount)
print()

# 3. Using f-strings

print(f"Product Name: {product_name}")
print(f"Price: ₹{price}")
print(f"Discount: {discount}%")
print(f"Stock Available: {available_stock} units")
print()

# 4. Using .format() method

print("Supplier Details: Name - {}, Contact - {}, Location - {}".format(
    supplier_name, supplier_contact, supplier_location
))
