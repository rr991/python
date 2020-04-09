from requests_html import HTMLSession
session = HTMLSession()

r = session.get("https://www.baidu.com/")

#获取页面上所有的链接
# all_links = r.html.links
all_html = r.html.html
print(all_html)
with open("baidu.html","w",encoding="utf-8") as f:
    f.write(all_html)

