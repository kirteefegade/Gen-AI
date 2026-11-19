product_list = [('Mango', 'Fruits'), ('Chair', 'Furniure'), ( 'Bike', 'Vehicle'), ('Truck', 'Vehicle'), ('Mobile', 'Electronic'), ('Laptop', 'Electronic'), ('TV', 'Electronic') ]
price_dict = {'Mango' : 10.6, 
              'Chair' : 500, 
              'Bike' : 40000, 
              'Truck' : 500000, 
              'Mobile' : 56000, 
              'Laptop' : 63000,
              'TV' : 39000}
catalog = [(product, price_dict.get(product, 0), category) for product, category in product_list]
category_to_product = dict()
for tup in catalog:
    if category_to_product.get(tup[2], None):
        products = category_to_product.get(tup[2])
        products.append(tup[0])
    else:
        category_to_product[tup[2]] = [tup[0]]
maxProductCategory = max(category_to_product, key = category_to_product.get)
print(maxProductCategory , " category has maximum products ")
print("Products are ", category_to_product[maxProductCategory])

