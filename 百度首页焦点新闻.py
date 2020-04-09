from requests_html import HTMLSession
session = HTMLSession()

r = session.get('http://news.baidu.com/')
# r.html.render()  # 首次使用，自动下载chromium
# print(r.html.html)
news = r.html.find('#pane-news>.hotnews>ul>li')
print(news)
# print(d.html.absolute_links)
for aa in news:
    print(aa.text)
    print(aa.absolute_links)
    print('\n')