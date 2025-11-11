import sys
sys.dont_write_bytecode = True

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')

import django
django.setup()

from db.models import User, Product

# ------------------- Populate Tables -------------------
if User.objects.count() == 0:
    User.objects.create(name="Dan")
    User.objects.create(name="Robert")

if Product.objects.count() == 0:
    Product.objects.create(upc="111", name="Apple", price=0.99)
    Product.objects.create(upc="222", name="Milk", price=3.49)
    Product.objects.create(upc="333", name="Bread", price=2.25)

print("\nUsers in System:")
for u in User.objects.all():
    print(f"{u.id} - {u.name}")

print("\nProducts Loaded:")
for p in Product.objects.all():
    print(f"{p.upc} - {p.name} - ${p.price}")

# ------------------- Scanning Input -------------------
print("\n--- Cash Register Scan Mode ---")
while True:
    scan = input("\nEnter UPC code (or 'exit'): ").strip()

    if scan.lower() == "exit":
        print("Closing Register.")
        break

    item = Product.objects.filter(upc=scan).first()
    
    if item:
        print(f"Item Found: {item.name} - ${item.price}")
    else:
        print("No product with that UPC.")
