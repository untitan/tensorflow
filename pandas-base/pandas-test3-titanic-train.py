import numpy as np
import pandas as pd

tt = pd.read_csv('titanic_train.csv')

age = tt['Age']
# print(age)

# 判读列数据是否为null（NaN）

age_is_null = pd.isnull(age)
# print(pd.isnull(age))
# print(age.isnull())
# print(age_is_null)
# print(age[age_is_null])

# 判断null个数
print('age_null个数', len(age[age_is_null]))
# 调用计算公式时，元素不能为null，必须填充数据
# print(tt[tt['Age'] > 50].head(10))
# 过滤掉age=null的数据
# print(tt['Age'][tt['Age'].isnull() == False])

# 平均值

# 第一种自己计算（数据不能为null才能计算，否则结果为NaN）
not_null_age = tt.Age[tt.Age.isnull() == False]
# print(not_null_age)
mean_age = sum(not_null_age) // len(not_null_age)
print(mean_age)
# pandas提供的方法（自动过滤null数据）
print(age.mean())

print('------------去重复-----------')
# drop_duplicates根据某列去重复后的行
data = tt.drop_duplicates('Pclass')
# 去重复后，取列
print(data['Pclass'])
# print(data['Pclass'].tolist())

print('------------根据船票等级，计算[平均]价----------')
# 方法一
fare_by_pclass = {}
for d in data['Pclass'].tolist():
	# 根据船票等级取所属行
	d_rows = tt[tt['Pclass'] == d]
	fare_by_pclass[d] = d_rows['Fare'].mean()
print(fare_by_pclass)

# 方法二
# pandas透视表pivot_table(默认求均值),index分组,values操作的数据,aggfunc调用的函数
fare_mean = tt.pivot_table(index='Pclass', values='Fare', aggfunc=np.mean)
fare_mean = tt.pivot_table(index='Pclass', values='Fare')
print(fare_mean)

print('------------根据船票等级，计算年龄----------')
age_mean = tt.pivot_table(index='Pclass', values='Age')
print(age_mean)

print('------------根据船票等级，计算地域票价/获救率----------')
# 地域计算：总票价/总获救率
emb_fare_sur = tt.pivot_table(index='Embarked', values=['Fare', 'Survived'], aggfunc=np.sum)
print(emb_fare_sur)
emb_fare_sur = tt.pivot_table(index='Embarked', values=['Fare', 'Survived'], aggfunc=np.mean)
print(emb_fare_sur)

print('----------缺失值数据处理------------')
# 丢掉包含缺失值的列
dropna = tt.dropna(axis=1)
# print(dropna)
print(dropna.size)
# 丢掉包含缺失值的行
dropna = tt.dropna(axis=0)
# print(dropna)
print(dropna.size)

# 每行的固定列包含缺失值则丢掉
dropna = tt.dropna(axis=0, subset=['Age', 'Cabin', 'Embarked'])
# print(dropna)
print(dropna.size)

print('------------排序--------------')
tt_age = tt['Age']
tt_age = tt_age.sort_values(ascending=False)
print(tt_age.head(10))
# 索引重新排序
tt_age_reset = tt_age.reset_index(drop=True)
print(tt_age_reset.head(10))

print('------------取值--------------')
age_ = tt.loc[1, 'Age']
pclass_ = tt.loc[1, 'Pclass']
print(age_, pclass_)

print('------------自定义函数：1---------------')


def custom_1(column):
	# 根据列：获取所有null值的索引集合
	is_null_column_index = pd.isnull(column)
	# 根据列：取索引==True的数据
	# column[is_null_column_index]
	# len计算集合个数
	return len(column[is_null_column_index])


# 调用自定义函数
is_null_column_count = tt.apply(custom_1)
print(is_null_column_count)

print('------------自定义函数：2---------------')


def custom_2(row):
	row_pclass = row['Pclass']
	return row_pclass


tt_custom_2 = tt.apply(custom_2, axis=1)

print('------------自定义函数：根据年龄分组并计算个数---------------')


def age_level(row):
	age_ = row['Age']
	if (age_ > 18 and age_ < 50):
		return '成人'
	elif (age_ >= 50):
		return '老年人'
	else:
		return '青少年'


# 返回Series:
age_lv = tt.apply(age_level, axis=1)

# 根据pandas父类方法value_counts(),根据value分组并计算个数
print(pd.value_counts(age_lv))
