from requests_html import HTMLSession
session = HTMLSession()

# for page in range(0,199,20):
#     print("#" * 30, page)
#     url = 'https://china.huanqiu.com/api/list2?node=/e3pmh1nnq/e7tl4e309&offset=' + str(page) + '&limit=20'
    # url =url + str(page)
    # url = url + '&limit=20'
    # print(url)
url = 'https://china.huanqiu.com/focus'
r = session.get(url)

news = r.html.xpath('//*[@id="recommend"]/li[@class="list-item-onepic"]')
# print(news)
# print(d.html.absolute_links)
for aa in news:
    print(aa.attrs('href'))
    # print(aa.absolute_links)
    print('\n')
