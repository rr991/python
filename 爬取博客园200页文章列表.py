from requests_html import HTMLSession
import os
'''
https://www.cnblogs.com/sticker0726/articles/10917087.html
'''
session = HTMLSession()
for page in range(1,200):
    print("#"*30,page)
    data = {
        "CategoryType": "SiteHome",
        "ParentCategoryId": 0,
        "CategoryId": 808,
        "PageIndex": page,
        "TotalPostCount": 4000,
        "ItemListActionName": "AggSitePostList"
            }

    r = session.get('https://news.cnblogs.com/n/recommend',data=data)
    # r.html是一个HTML对象 <HTML url='https://www.python.org/'>
    # 查看页面的源代码
    # h = r.html.html

    #获取页面上的所有的链接（包括绝对路径和相对路径），以集合的形式显示
    # all_links = r.html.links

    #页面上所有可被获取到的超链接，都会被转成绝对路径形式。以集合的形式显示用list方法进行取值
    # all_absolute_links = r.html.absolute_links

    #find接收css选择器返回元素列表
    news = r.html.find('div.news_block div.content h2.news_entry')
    # print(about)
    # print(type(news))
    for aa in news:
        print(aa.text)
        print(aa.absolute_links)
        print('\n')



# for i in range(0,9):
#     news = r.html.find('div.news_block div.content h2.news_entry a ')[i]
# # 获得元素文本
#     print(news.text)
#     print(news.absolute_links)



#获得标签的所有属性，返回一个字典
# attr = news.attrs
#得到一个标签的源代码  #结果<a href="/n/625717/" target="_blank">国内首个北斗三号全芯片解决方案发布</a>
# html_=news.html