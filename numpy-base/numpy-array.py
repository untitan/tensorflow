from builtins import print

import numpy

print('----------numpy-base.array-------------')
# 一维
array1 = numpy.array(range(5))
print(array1)
print(array1.shape)

# 多维
array2 = numpy.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
print(array2)
# shape 显示结构-2维-每个3个元素
print(array2.shape)
print('----------dtype-------------')
# array的元素结构必须一致
print(array2.dtype)

# 取整列
print(array2[:, 1:3])

print('------------array==10-----------')
# array == xxx 代表：遍历每个元素与xxx比较。返回bool类型ndarray
array3 = numpy.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])
print(array3 == 5)
equal_to_five = (array3 == 5)
print(array3[equal_to_five])
# 根据True/False取行/列
array4 = numpy.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
equal_5 = (array4[:, 1] == 5)
print(array4 == 5)
print(array4[equal_5, :])
# 余数
array5 = numpy.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
print(array4 % 2)
print(array4 % 2 == True)
print('----------sum-------------')
# array.sum()
# axis = 1 行求和，axis=2 列求和
print(array5.sum(axis=1))
print(array5.sum(axis=0))

print('----------reshape-------------')
# 构建ndarray
array6 = numpy.arange(15)
array6 = array6.reshape(5, 3)

print(array6)

print('-----------ones------------')
# 生成ndarray
print(numpy.ones((2, 3, 4), dtype=numpy.int32))

print(numpy.arange(1, 100, 5).reshape(4, 5))

print('----------random-------------')
# 随机生成ndarray
print(numpy.random.random((4, 5)))

print(numpy.random.randint(0, 100, 3))

print('----------linspace-------------')
# 0-100之间，平均取10个元素
print(numpy.linspace(0, 100, 100, dtype=int))

print('----------array减法-------------')
a1 = numpy.arange(0, 100, 10)
a2 = a1
print('a1:', a1)
print('a2:', a2)
print(a1 - a2)
print(a2 ** 2)
print(a1 - a2 // 2)
print(a1 * a2)
print(a1 > 50)

print('----------array矩阵乘法-------------')
a1 = numpy.array([[1, 1],
                  [0, 1]])
a2 = numpy.array([[2, 0],
                  [3, 4]])
print(a1)
print(a2)
# 每个元素按照索引值相乘
print('----a.dot(b)-----')
# [(a1.行1-1 * a2.列1-1 + a1.行1-2 * a2.列1-2) , (a1.行1-1 * a2.列2-1 + a1.行1-2 * a2.列2-2)]
# [(1 * 2 + 1 * 3, 1 * 0 + 1 * 4), (0 * 2 + 1 * 3, 0 * 0 + 1 * 4)]
print((1 * 2 + 1 * 3, 1 * 0 + 1 * 4), (0 * 2 + 1 * 3, 0 * 0 + 1 * 4))
print(a1.dot(a2))

print('----------array矩阵操作-------------')
a1 = numpy.int32(10 * numpy.random.random((3, 4)))
print(a1)
# ndarray转成数组
print(a1.ravel())
a1.shape = (6, -1)  # -1 代表自动分配,实际=12/6
print(a1)
print(a1.T)

print('----------array矩阵操作：拼接-------------')
a = numpy.int32(10 * numpy.random.random((2, 6)))
b = numpy.int32(10 * numpy.random.random((2, 6)))

# 拼接
print(a)
print(b)
print('------')
print('横向', numpy.hstack((a, b)))  # 横向拼接
print('纵向', numpy.vstack((a, b)))  # 纵向拼接

print('----------array矩阵操作：切分-------------')
a = numpy.random.randint(0, 101, 16).reshape((4, 4))
print(a)
print('横向', numpy.hsplit(a, 2))  # 横向切分
print('纵向', numpy.vsplit(a, 2))  # 纵向切分

print('----------array矩阵操作：复制-------------')
# copy() 指向新的内存地址，view指向内存同一数据(数据同时变更)
a = numpy.arange(10)
b = a.copy()
print(a, b)
print('b copy a ?', b is a)
print('a.id', id(a))
print('b.id', id(b))

print('----------array矩阵操作：排序-------------')
a = numpy.random.randint(0, 16, 16).reshape(4, 4)
print(a)
# 列最大值的索引
print(a.argmax(axis=0))
# 行最大值的索引
print(a.argmax(axis=1))

print('----------array矩阵操作：排序（根据索引取值）-------------')
# 根据索引取值
c = numpy.random.randint(0, 16, 16).reshape(4, 4)
print('原数据\n', c)
h_max_index = c.argmax(axis=1)
print('行最大数的索引', h_max_index)

print(c[h_max_index, range(c.shape[1])])

print('----------array矩阵操作：排序（根据索引取值）-------------')

# a = numpy-base.random.randint(0, 100, 20).reshape(1, -1)
a = numpy.array([3, 1, 2, 5, 7, 9]) * 10
print('orig_array:', a)
sort_index = a.argsort()
print('sort_index:', sort_index)
print('sort_array:', a[sort_index])
