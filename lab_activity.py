# Rice Market System
# Processes a customer's rice purchase and prints a receipt.
TAX_RATE = 0.15
LINE = "=" * 44
DASH = "-" * 44

print("RICE MARKET SYSTEM")
print()

# 1-4: Collect customer and purchase details
customer_name = input("Enter customer name: ")
rice_variety = input("Enter rice variety: ")
price_per_kg = float(input("Enter price per kilogram: "))
kilograms = float(input("Enter kilograms to purchase: "))

# 5: Compute subtotal, tax, and total
subtotal = price_per_kg * kilograms
tax = subtotal * TAX_RATE
total = subtotal + tax

print()
print(f"{'Subtotal:':<26}PHP {subtotal:>6.2f}")
print(f"{'Tax (15%):':<26}PHP {tax:>6.2f}")
print(f"{'Total amount due:':<26}PHP {total:>6.2f}")
print()

# 6-7: Accept payment and compute change
payment = float(input("Enter payment: "))
change = payment - total

# 8: Display the receipt
print()
print(LINE)
print(" " * 13 + "RICE MARKET RECEIPT")
print(LINE)
print(f"{'Customer name:':<26}{customer_name}")
print(f"{'Rice variety:':<26}{rice_variety}")
print(f"{'Price per kilogram:':<26}PHP {price_per_kg:>6.2f}")
print(f"{'Kilograms purchased:':<26}    {kilograms:>5.2f} kg")
print(DASH)
print(f"{'Subtotal:':<26}PHP {subtotal:>6.2f}")
print(f"{'Tax (15%):':<26}PHP {tax:>6.2f}")
print(f"{'Total amount due:':<26}PHP {total:>6.2f}")
print(f"{'Payment:':<26}PHP {payment:>6.2f}")
print(f"{'Change:':<26}PHP {change:>6.2f}")
print(LINE)
print(" " * 7 + "Thank you for your purchase!")