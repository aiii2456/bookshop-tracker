import csv

shop_name = "My Curated Bookshop"
commission_rate = 0.10
total_earned = 0.0

print(f"--- {shop_name} Inventory & Earnings Report ---\n")

with open("books.csv", mode="r", newline="") as file:
    reader = csv.DictReader(file)
    for row in reader:
        title = row["Title"]                  # String
        author = row["Author"]                # String
        price = float(row["Price"])           # Float
        sold = int(row["Copies_Sold"])        # Integer
        in_stock = row["In_Stock"] == "True"  # Boolean

        book_earned = price * sold * commission_rate
        total_earned += book_earned
        status = "In Stock" if in_stock else "Out of Stock"

        print(f"{title} by {author}")
        print(f"  Status: {status} | Sold: {sold} | Commission: ${book_earned:.2f}\n")

print(f"Total Affiliate Earnings: ${total_earned:.2f}")
