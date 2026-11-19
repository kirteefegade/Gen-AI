products = ['Mango', 'Chair', 'Bike', 'Pen', 'Mobile', 'Bag']
categories_set = {'Fruits', 'Furniure', 'Vehicle', 'Writing', 'Electronic', 'Travel'}
print("Before adding new category", categories_set)  
categories_set.add('Fruits')
print("After adding category, no duplicates",categories_set)
print('Fruits' in categories_set)
print('Pen' in categories_set)