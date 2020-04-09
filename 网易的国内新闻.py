from requests_html import HTMLSession
session = HTMLSession()

r = session.get('http://news.163.com/special/0001386F/rank_news.html')
# r.html.render()  # 首次使用，自动下载chromium
# print(r.html.html)
d = r.html.find()
print(d)
# print(d.html.absolute_links)