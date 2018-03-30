import pandas as pd

food = pd.read_csv('test2.csv')

print(food[['name', 'weight_kg']])

food['weight_g'] = food['weight_kg'] * 1000

print('-------列乘法-------')
print(food['name'], food['price'] * food['weight_kg'])

print(food['price'].min())

print('-------排序--------')
# print(food.sort_values('price'))
# 升序降序
print(food.sort_values('price', ascending=False))
