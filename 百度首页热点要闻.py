from requests_html import HTMLSession
session = HTMLSession()

r = session.get('http://news.baidu.com/')
# r.html.render()  # 首次使用，自动下载chromium
# print(r.html.html)

#两个语法中间使用‘|’连接
news = r.html.xpath('//div[@class="mod-tab-content"]/div/div/ul/li | //div[@class="mod-tab-content"]/div/ul/li')
# news = r.html.find('.mod-tab-content>div>div>ul>li')
print(news)
# print(d.html.absolute_links)
for aa in news:
    print(aa.text)
    print(aa.absolute_links)
    print('\n')