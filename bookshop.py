# Bookshop.org Affiliate & Inventory Tracker

# 1. STRING (Text data)
book_title = "Superposition"
author = "David Walton"
shop_name = "My Curated Bookshop"

# 2. INTEGER (Whole numbers)
pages = 384
copies_sold = 12

# 3. FLOAT (Decimal numbers)
book_price = 18.99
commission_rate = 0.10

# 4. BOOLEAN (True/False switches)
is_in_stock = True

# Calculate total earnings
total_earned = copies_sold * book_price * commission_rate

if is_in_stock:
    print("Welcome to", shop_name)
    print("Book:", book_title, "by", author)
    print("Pages:", pages)
    print("Total Affiliate Earnings: $", round(total_earned, 2))
else:
    print("Sorry, this book is currently out of stock.")
