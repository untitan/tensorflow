import pandas

print('--------读取文件----------')
food = pandas.read_csv('food_info.csv')
print(type(food))
# print(food)
# 从头取几条
print(food.head(1))
# 从尾取几条
print(food.tail(1))
# 取列头
print(food.columns)
# 取索引
print(food.index)

# 取第几行
print(food.loc[1])
# 从第几行取到第几行
print(food.loc[0:2])

# 按列取
print(food[['Shrt_Desc', 'NDB_No']])

print('------------取列结尾(g)的列数据---------------')

def columns_g_list(food):
	print(food.columns.tolist())
	g_list = []
	for c in food.columns:
		if c.endswith('(g)'):
			g_list.append(c)
	print(food[g_list].head(1))

columns_g_list(food)
