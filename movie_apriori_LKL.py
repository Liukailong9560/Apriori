# -*- coding: utf-8 -*-
import csv
from efficient_apriori import apriori

file_path = u'E:\工作\数据分析\课程项目\关联规则挖掘\宁浩.csv'
ori_data = csv.reader(open(file_path, 'r', encoding='utf-8-sig'))

data = []
for line in ori_data:
    name_new = []
    for item in line:
        name_new.append(item.strip())
    data.append(name_new[1:])

itemsets, rules = apriori(data, min_support=0.3, min_confidence=1)
print(itemsets, rules)