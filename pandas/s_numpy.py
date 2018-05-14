#coding:utf-8

# 创建一维数组
np.array([1,2,3])

# 创建二维数组
np.array([11,11],[22,22],[33,33])

# 创建占位数组，内容全部为float(64)
np.zeros([3,4])  # 创3*4的二维数组，每个元素的值都为0.
np.ones([3,4])  # 元素值为1.
np.empty([3,4]) # 元素值随机且依赖于内存状态

# 查看数组的数据类型
t = np.zeros([3,4], dtype=int)  # 数据类型为int
t.dtype # 查看数据类型
t.dtype.itemsize    # 查看每个元素占用的字节数

# 创建数列
np.arange(3,10,.5)  # 创建数列，起始值为3，结束值为10，步长0.5。数列不包含结束值
