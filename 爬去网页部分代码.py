from requests_html import HTMLSession

session = HTMLSession()
url = 'https://cpppatterns.com/patterns/copy-range-of-elements.html'
r = session.get(url)
data=r.html.find('tr > td:nth-child(2) > code>span')#这种是find通过css选择器方式获取元素
# data = r.html.xpath('//tr/td[2]/code/span')  # 此种通过xpath方法获取元素

for c in data:  # 通过循环方法猎取
    cc = c.text
    print(cc)
