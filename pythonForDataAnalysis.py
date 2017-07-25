# 
"""
    《Python for Data Analysis》，作者：Wes McKinney
    数据源：http://www.grouplens.org/node , MovieLens用户提供的电影评分数据
"""

import pymongo
conn = pymongo.MongoClient(host='112.74.161.9', port=28010)
conn.BJDdb.authenticate('writeuser','51write')
try:
    db = conn.BJDdb
    coll = db.BJD_User
except expression as identifier:
    print(identifier)

db = conn.BJDdb
coll = db.BJD_User
rec = [i for i in coll.find(limit=500, sort=[('_id', pymongo.DESCENDING),])] # 从数据库中取出最后的500条用户记录
conn.close()

# 按nativename分组计数
t_nativename = [i['nativename'] for i in rec]
def get_counts(sequence):
    """基础计数方法"""
    counts = {}
    for x in sequence:
        if x in counts:
            counts[x] += 1
        else:
            counts[x] = 1
    return counts

def get_counts(sequence):
    """使用defaultdict进行计数"""
    counts = defaultdict(int)  # 所有值初始化为0
    for x in sequence:
        counts[x] += 1
    return dict(counts)

def get_counts(sequence):
    """使用collections.Counter进行计数"""
    from collections import Counter
    t = Counter(sequence)
    print (dict(t))
    print (t.most_common(10))  # 打印top10
    return t

def get_counts(sequence,countfield):
    """使用pandas.DataFrame的数据框处理方法进行计数"""
    from pandas import DataFrame
    from matplotlib import pyplot as plt
    frame = DataFrame(sequence) # 将数据对象转换为DataFrame数据框
    t = frame[countfield].value_counts() # 使用value_counts()方法计数
    print(t[:10])   # 打印出TOP10
    t[:10].plot(kind='barh', rot=0) # 对TOP10生成绘图对象，横向条形图
    plt.show()   # 使用matplotlib绘图
    return t

import pandas as pd
unames = ['user_id', 'gender', 'age', 'occupation', 'zip']
users = pd.read_table('E:/MyDownload/ml-1m/users.dat', sep='::', header=None, names=unames)

rnames = ['user_id', 'movie_id', 'rating', 'timestamp']
ratings = pd.read_table('E:/MyDownload/ml-1m/ratings.dat', sep='::', header=None, names=rnames)

mnames = ['movie_id', 'title', 'genres']
movies = pd.read_table('E:/MyDownload/ml-1m/movies.dat', sep='::', header=None, names=mnames)