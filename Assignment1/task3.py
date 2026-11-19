price_dict = {'Mango' : 10.6, 
              'Chair' : 500, 
              'Bike' : 40000, 
              'Pen' : 5, 
              'Mobile' : 56000, 
              'Bag' : 300 }
price_dict['Rose'] = 20
print("After adding Rose in dictionary ", price_dict)
price_dict['Mobile'] = 51000
print("After updating price of mobile ", price_dict)
price_dict.pop('Chair')
print(price_dict)
avg = sum(price_dict.values())/len(price_dict)
print("Average is  :- ",avg)
maxProduct = max(price_dict, key= price_dict.get)
print("Product ", maxProduct, " has maximum price ", price_dict.get(maxProduct))
minProduct = min(price_dict, key= price_dict.get)
print("Product ", minProduct, " has Minimum price ", price_dict.get(minProduct))