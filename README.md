# 关联规则挖掘：导演如何选择演员

先使用爬虫在豆瓣上面抓取导演电影的数据。
- 浏览器模拟：selenium和webdriver工具包(后来好像被反扒机制识别出，不过爬到的数据已经够用。)

## 使用Apriori工具包

使用efficient-apriori这个包，因为sklearn中没有关联规则算法，而且这个轮子算法与输入顺序无关，其他的大部分考虑了输入数据的先后关系

## 挖掘导演是如何选择演员总结
1、注意知识点
- APriori算法的核心是理解频繁项集和关联规则。
- 在算法的运算的过程中，还要重点掌握支持度和置信度和提升度的理解。
- 在工具的使用上，可以使用efficient_apriori这个工具包，它会把每一条数据中的项（item）放到一个集合（篮子）里面来处理，不考虑（item）之间的先后顺序。

2、在实际的运用中需要灵活处理，比如导演如何选择演员的这个案例，虽然工具的使用会很方便，但是重要的还是数据挖掘前的数据准备过程，也就是获取某个导演的电影数据集。

3、Apriori实战
- 工具包
    - efficient_apriori工具包
        - itemsets,rules = apriori(data, min_support, min_confidence)
        - 每一条数据中的项，不考虑其先后顺序，按照集合的方式来处理
    - 如何找到工具包：https://pypi.org
- 导演如何选择演员
    - 数据采集
        - CSV文件读取：CSV工具包
        - Xpath解析：lxml工具包
        - 浏览器模拟：selenium和webdriver工具包
    - 关联规则挖掘
        - Apriori算法：efficient-apriori工具包

