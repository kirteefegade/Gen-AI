products = ['Mango', 'Chair', 'Bike', 'Pen', 'Mobile', 'Bag']
sampleProduct = ('Chair', 800, 'Furniture')
print(products[1])
print(products[len(products)-1])
products.extend(['Laptop', 'Sugar'])
print(products)
sampleProductList = list(sampleProduct)
sampleProductList[1] = 1000
sampleProduct = tuple(sampleProductList)
print(sampleProduct)


