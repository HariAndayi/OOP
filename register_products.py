from main import Product


try:
    product_price = input("Enter product price \n")
    product_quantity = input("Enter product quantity \n")
    product_description = input("Enter product description \n")
    product_color = input("Enter product color \n")

    Product.create(prod_price=product_price, prod_quantity=product_quantity, prod_description=product_description, prod_color=product_color)
    print("Product created succesfully")
except:
    print("Failed to create product")