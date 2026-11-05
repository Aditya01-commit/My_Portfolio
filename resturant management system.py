import pandas as pd
import matplotlib.pyplot as mb

# Menu data
item = {
    "ItemID": [1, 2, 3, 4, 5, 6, 7, 8, 9],
    "ItemName": [
        "Chicken Naan", "Chicken Kabab", "Paneer and butter roti ", "Veg Platter",
        "Ice Cream", "Sweet Lassi", "Gulab Jamoon", "chicken Biryani", "Veg Pulav"
    ],
    "Price": [200, 150, 180, 150, 100, 80, 120, 220, 120],
    "Available": ["yes", "yes", "yes", "no", "yes", "no", "yes", "yes", "yes"],
    "Category": ["main", "main", "main", "starter", "dessert", "dessert", "dessert", "main", "starter"],
    "OrdersLastMonth": [24, 25, 30, 20, 40, 33, 28, 19, 22],
    'review_list':[[5],[5],[4],[4],[3],[5],[4],[4],[5]]
}

# Create DataFrame
a = pd.DataFrame(item)

# Main loop
while True:
    print('-' * 30)
    print('K-IIT THE DHABA')
    print('-' * 30)
    print('1. Show Menu')
    print('2. Order')
    print('3. add item')
    print('4. Add Review')
    print('5. Exit')
    print('6. show graph')
    
    print('-' * 30)

    try:
        choice = int(input("Enter your choice (1-5): "))
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 5.")
        continue

    if choice == 1:

        print("\n--- MENU ---")
        a['AvgRating'] = a['review_list'].apply(
    lambda x: round(sum(x)/len(x), 1) if isinstance(x, list) and len(x) > 0 else 0
)
        print(a[['ItemID', 'ItemName', 'Price', 'Available', 'AvgRating']])
        print('-' * 70)

    elif choice == 2:
        order_item = {}
        print("Enter your orders (ItemID and Quantity). Type 'done' to finish.")
        while True:
            entry = input("ItemID Quantity (e.g., 2 3): ")
            if entry.lower() == 'done':
              break
            try:
                item_id, qty = map(int, entry.strip().split())
                if item_id in order_item:
                    order_item[item_id] += qty
                else:
                    order_item[item_id] = qty
            except ValueError:
                print("Invalid input. Please enter in format: ItemID Quantity")

        print('-' * 30)
        total_bill = 0
        for item_id, qty in order_item.items():
          if item_id in a['ItemID'].values:
            row = a[a['ItemID'] == item_id].iloc[0]
            if row['Available'].lower() == 'yes':
               print(f"You ordered: {row['ItemName']} x{qty} - ₹{row['Price']} each")
               total_bill += row['Price'] * qty
            else:
               print(f"Sorry, {row['ItemName']} is currently not available.")
        else:
             print('ordered_items')

        print('-' * 30)
        print(f"Total amount: ₹{total_bill}")

        
    elif choice == 3:
        name = input('Enter item name: ')
        try:
            item_price = int(input('Enter the price: '))
        except ValueError:
           print("Invalid price. Please enter a number.")
           continue

        category = input('Enter category (main, starter, or dessert): ').lower()
        if category not in ['main', 'starter', 'dessert']:
            print("Invalid category. Please choose from main, starter, or dessert.")
            continue

        try:
            orders = int(input('Enter number of orders: '))
        except ValueError:
            print("Invalid number. Please enter an integer.")
            continue

        new_id = a['ItemID'].max() + 1
        a.loc[len(a)] = {
        'ItemID': new_id,
        'ItemName': name,
        'Price': item_price,
        'Available': 'yes',
        'Category': category,
        'OrdersLastMonth': orders
        }
        print(f"Item '{name}' added successfully!")

    
        print("\nUpdated Menu (New Item):")
        print(a[['ItemID', 'ItemName', 'Price', 'Available']].tail(1))
        print('-' * 30)
 

    
    elif choice == 4:
     
        Item_id = int(input('Enter your ItemID: '))
        review = int(input("Enter your review (1-5): "))
        if review < 1 or review > 5:
            print("Invalid review. Please enter a number between 1 and 5.")
            continue

        if Item_id in a['ItemID'].values:
            idx = a[a['ItemID'] == Item_id].index[0]
            a.at[idx, 'review_list'].append(review)
            print("Thank you for your feedback!")
        else:
            print("ItemID not found.")
        
            print("Thank you for your feedback!")

    
    

    elif choice == 5:
        print("Thank you for visiting K-IIT THE DHABA!")
        break

    elif choice == 6:
        mb.plot(a['ItemName'], a['OrdersLastMonth'], marker='o', linestyle='-', color='green')
        mb.title('Orders Last Month per Item')
        mb.xlabel('Item Name')
        mb.ylabel('Number of Orders')
        mb.xticks(rotation=45, ha='right')
        mb.grid(True)
        mb.tight_layout()
        mb.show()

    else:
        print("Invalid choice. Please select a number between 1 and 5.")

    

    
