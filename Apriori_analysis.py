# -*- coding:utf-8 -*-
# 下载某个导演的电影数据
from efficient_apriori import apriori
import csv
director = u'宁浩'
file_name = './' + director + '.csv'
lists = csv.reader(open(file_name, 'r', encoding='utf-8-sig'))
# 数据加载
data = []
for names in lists:
    name_new = []
    for name in names:
        # 去掉演员数据中的空格
        name_new.append(name.strip())
    data.append(name_new[1:])
# 挖掘频繁项集和关联规则,这里的最小支持度是0.5，最小置信度为1
itemsets, rules = apriori(data, min_support=0.5, min_confidence=1)
print(itemsets)
print(rules)